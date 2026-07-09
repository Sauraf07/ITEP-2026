import json
import urllib.request
import urllib.error
import asyncio
from app.config import settings
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.message import Message
from app.repository.message_repository import MessageRepository


class MessageService:

    def __init__(self):
        self.repository = MessageRepository()

    def _build_prompt(self, content: str, history: list) -> str:
        history_text = ""
        for msg in history[-10:]:
            label = "User" if msg.role == "user" else "Coach"
            history_text += f"{label}: {msg.content}\n"

        return (
            "You are SoftSkill Coach, a friendly AI communication coach.\n\n"
            "Your job:\n"
            "1. Answer the user's question or respond naturally to what they said.\n"
            "2. If they made spelling, grammar, or phrasing mistakes, gently correct them.\n"
            "3. Give short tips to improve communication (confidence, clarity, vocabulary).\n"
            "4. Be encouraging, clear, and helpful.\n\n"
            f"Conversation so far:\n{history_text if history_text else '(new conversation)'}\n"
            f"Latest user message: \"{content}\"\n\n"
            "Respond with ONLY a raw JSON object. No markdown, no extra text.\n"
            "{\n"
            "  \"grammar_score\": 90,\n"
            "  \"confidence_score\": 85,\n"
            "  \"vocabulary_score\": 88,\n"
            "  \"suggestions\": \"Short coaching tip in one sentence.\",\n"
            "  \"coach_reply\": \"Your full reply — answer their question, correct mistakes inline, and guide them.\"\n"
            "}"
        )

    def _parse_json_response(self, text_response: str) -> dict:
        text_cleaned = text_response.strip()
        if text_cleaned.startswith("```json"):
            text_cleaned = text_cleaned[7:]
        elif text_cleaned.startswith("```"):
            text_cleaned = text_cleaned[3:]
        if text_cleaned.endswith("```"):
            text_cleaned = text_cleaned[:-3]
        text_cleaned = text_cleaned.strip()
        return json.loads(text_cleaned)

    async def _call_gemini(self, prompt: str, api_key: str) -> dict:
        models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.0-flash-lite"]
        last_error = None

        for model in models:
            try:
                url = (
                    f"https://generativelanguage.googleapis.com/v1beta/"
                    f"models/{model}:generateContent?key={api_key}"
                )
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {
                        "responseMimeType": "application/json"
                    }
                }

                req_data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    url,
                    data=req_data,
                    headers={"Content-Type": "application/json"},
                    method="POST"
                )

                def make_request():
                    with urllib.request.urlopen(req, timeout=30) as response:
                        return response.read().decode("utf-8")

                res_body = await asyncio.to_thread(make_request)
                res_json = json.loads(res_body)
                text_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
                return self._parse_json_response(text_response)
            except Exception as e:
                last_error = e
                print(f"Gemini ({model}) failed: {e}")

        if last_error:
            raise last_error
        return None

    async def _call_groq(self, prompt: str, api_key: str) -> dict:
        models = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
        last_error = None

        for model in models:
            try:
                url = "https://api.groq.com/openai/v1/chat/completions"
                payload = {
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": {"type": "json_object"}
                }

                req_data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    url,
                    data=req_data,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {api_key}"
                    },
                    method="POST"
                )

                def make_request():
                    with urllib.request.urlopen(req, timeout=30) as response:
                        return response.read().decode("utf-8")

                res_body = await asyncio.to_thread(make_request)
                res_json = json.loads(res_body)
                text_response = res_json["choices"][0]["message"]["content"]
                return self._parse_json_response(text_response)
            except Exception as e:
                last_error = e
                print(f"Groq ({model}) failed: {e}")

        if last_error:
            raise last_error
        return None

    async def _get_llm_coaching(self, content: str, history: list) -> dict:
        gemini_key = settings.GEMINI_API_KEY
        groq_key = settings.GROQ_API_KEY

        if not gemini_key and not groq_key:
            return None

        prompt = self._build_prompt(content, history)
        required_keys = (
            "grammar_score", "confidence_score", "vocabulary_score",
            "suggestions", "coach_reply"
        )

        if gemini_key:
            try:
                result = await self._call_gemini(prompt, gemini_key)
                if result and all(k in result for k in required_keys):
                    print("AI response: Gemini")
                    return result
            except Exception as e:
                print(f"Gemini provider failed: {e}")

        if groq_key:
            try:
                result = await self._call_groq(prompt, groq_key)
                if result and all(k in result for k in required_keys):
                    print("AI response: Groq")
                    return result
            except Exception as e:
                print(f"Groq provider failed: {e}")

        return None

    def _rule_based_coaching(self, content: str) -> dict:
        words = content.strip().split()
        num_words = len(words)

        grammar_score = 95.0
        if content and not content[0].isupper():
            grammar_score -= 15.0
        if content and content[-1] not in [".", "!", "?"]:
            grammar_score -= 15.0
        if num_words > 20:
            grammar_score -= 10.0
        elif num_words < 3:
            grammar_score -= 10.0
        grammar_score = max(40.0, min(100.0, grammar_score))

        confidence_score = 100.0
        hesitant_words = [
            "maybe", "sorry", "just", "i think", "probably",
            "um", "uh", "actually", "sort of", "kind of"
        ]
        content_lower = content.lower()
        found_hesitant = []
        for hw in hesitant_words:
            if hw in content_lower:
                found_hesitant.append(hw)
                confidence_score -= 15.0
        confidence_score = max(40.0, min(100.0, confidence_score))

        uniq_words = set([w.lower().strip(".,!?") for w in words])
        long_words = [w for w in uniq_words if len(w) > 6]
        vocabulary_score = 70.0 + (len(long_words) * 5.0)
        vocabulary_score = max(40.0, min(100.0, vocabulary_score))

        suggestions_list = []
        if found_hesitant:
            suggestions_list.append(
                f"Try to express your thoughts more assertively by avoiding "
                f"softeners like: {', '.join(found_hesitant)}."
            )
        if grammar_score < 80.0:
            suggestions_list.append(
                "Start with a capital letter and end with proper punctuation."
            )
        if vocabulary_score < 80.0:
            suggestions_list.append(
                "Try using more descriptive and varied vocabulary."
            )
        if not suggestions_list:
            suggestions_list.append(
                "Excellent communication! Keep practicing to stay sharp."
            )

        suggestions = " ".join(suggestions_list)
        coach_reply = (
            f"Here is my coaching feedback on your message:\n\n"
            f"Scores — Grammar: {grammar_score}%, "
            f"Confidence: {confidence_score}%, "
            f"Vocabulary: {vocabulary_score}%\n\n"
            f"Tip: {suggestions}"
        )

        return {
            "grammar_score": grammar_score,
            "confidence_score": confidence_score,
            "vocabulary_score": vocabulary_score,
            "suggestions": suggestions,
            "coach_reply": coach_reply
        }

    async def create_message(
        self,
        db: AsyncSession,
        role: str,
        content: str,
        conversation_id: int
    ):
        message = Message(
            role=role,
            content=content,
            conversation_id=conversation_id
        )
        saved_msg = await self.repository.create_message(db, message)

        if role == "user":
            from app.repository.conversation_repository import ConversationRepository
            from app.model.feedback import Feedback
            from app.repository.feedback_repository import FeedbackRepository

            conv = await ConversationRepository().get_conversation_by_id(db, conversation_id)
            if conv:
                history = await self.repository.get_messages(db, conversation_id)
                llm_data = await self._get_llm_coaching(content, history)

                if llm_data:
                    grammar_score = float(llm_data["grammar_score"])
                    confidence_score = float(llm_data["confidence_score"])
                    vocabulary_score = float(llm_data["vocabulary_score"])
                    suggestions = str(llm_data["suggestions"])
                    coach_content = str(llm_data["coach_reply"])
                else:
                    fallback = self._rule_based_coaching(content)
                    grammar_score = fallback["grammar_score"]
                    confidence_score = fallback["confidence_score"]
                    vocabulary_score = fallback["vocabulary_score"]
                    suggestions = fallback["suggestions"]
                    coach_content = fallback["coach_reply"]

                feedback = Feedback(
                    grammar_score=grammar_score,
                    confidence_score=confidence_score,
                    vocabulary_score=vocabulary_score,
                    suggestions=suggestions,
                    user_id=conv.user_id
                )
                await FeedbackRepository().create_feedback(db, feedback)

                coach_message = Message(
                    role="coach",
                    content=coach_content,
                    conversation_id=conversation_id
                )
                await self.repository.create_message(db, coach_message)

        return saved_msg

    async def get_messages(
        self,
        db: AsyncSession,
        conversation_id: int
    ):
        return await self.repository.get_messages(
            db,
            conversation_id
        )
