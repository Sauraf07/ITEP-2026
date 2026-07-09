// Toast Utilities
function showToast(message, type = 'info') {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = message;
    toast.className = `show ${type}`;
    setTimeout(() => {
        toast.className = '';
    }, 4000);
}

// Auth State Management
function getToken() {
    return localStorage.getItem('token');
}

function isLoggedIn() {
    return getToken() !== null;
}

function getUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    showToast('Logged out successfully', 'success');
    setTimeout(() => {
        window.location.href = '/login';
    }, 500);
}

// Tab Switching (Dashboard)
function switchTab(tabName) {
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.tab === tabName);
    });
    document.querySelectorAll('.tab-panel').forEach(panel => {
        panel.classList.toggle('active', panel.id === `tab-${tabName}`);
    });

    if (tabName === 'chat' && !chatInitialized) {
        initChatPage();
        chatInitialized = true;
    }
    if (tabName === 'feedback' && !feedbackInitialized) {
        initFeedbackPage();
        feedbackInitialized = true;
    }
}

function initDashboardTabs() {
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            switchTab(btn.dataset.tab);
        });
    });
}

// Router Guards
let chatInitialized = false;
let feedbackInitialized = false;
let activeConversationId = null;

document.addEventListener('DOMContentLoaded', () => {
    const token = getToken();
    const user = getUser();
    const path = window.location.pathname;

    const protectedRoutes = ['/dashboard', '/chat', '/feedback'];
    const authRoutes = ['/login', '/register'];

    updateNavbar(token);

    if (protectedRoutes.includes(path)) {
        if (!token) {
            window.location.href = '/login';
            return;
        }
    }

    if (authRoutes.includes(path)) {
        if (token) {
            window.location.href = '/dashboard';
            return;
        }
    }

    if (path === '/login') {
        initLoginPage();
    } else if (path === '/register') {
        initRegisterPage();
    } else if (path === '/dashboard') {
        initDashboardPage(user);
    } else if (path === '/chat') {
        initChatPage();
        chatInitialized = true;
    } else if (path === '/feedback') {
        initFeedbackPage();
        feedbackInitialized = true;
    }
});

function updateNavbar(token) {
    const nav = document.querySelector('nav');
    if (!nav) return;

    if (token) {
        const user = getUser();
        nav.innerHTML = `
            <a href="/dashboard" class="logo">SoftSkill Coach</a>
            <div class="nav-links">
                <a href="/dashboard" class="${isActive('/dashboard')}">Dashboard</a>
                <span class="user-greeting">${user ? user.username : 'User'}</span>
                <button onclick="logout()">Logout</button>
            </div>
        `;
    } else {
        nav.innerHTML = `
            <a href="/" class="logo">SoftSkill Coach</a>
            <div class="nav-links">
                <a href="/" class="${isActive('/')}">Home</a>
                <a href="/login" class="${isActive('/login')}">Login</a>
                <a href="/register" class="${isActive('/register')}">Register</a>
            </div>
        `;
    }
}

function isActive(p) {
    return window.location.pathname === p ? 'active' : '';
}

// --- Login ---
function initLoginPage() {
    const form = document.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = form.querySelector('input[type="email"]').value;
        const password = form.querySelector('input[type="password"]').value;

        if (!email || !password) {
            showToast('Please fill all fields', 'error');
            return;
        }

        try {
            const response = await fetch('/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();
            if (response.ok) {
                localStorage.setItem('token', data.access_token);
                localStorage.setItem('user', JSON.stringify(data.user));
                showToast('Login successful!', 'success');
                setTimeout(() => {
                    window.location.href = '/dashboard';
                }, 800);
            } else {
                showToast(data.detail || 'Login failed', 'error');
            }
        } catch (err) {
            showToast('Connection error. Try again.', 'error');
        }
    });
}

// --- Register ---
function initRegisterPage() {
    const form = document.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = form.querySelector('input[type="text"]').value;
        const email = form.querySelector('input[type="email"]').value;
        const password = form.querySelector('input[type="password"]').value;

        if (!username || !email || !password) {
            showToast('Please fill all fields', 'error');
            return;
        }

        try {
            const response = await fetch('/auth/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, email, password })
            });

            const data = await response.json();
            if (response.ok) {
                showToast('Registration successful! Please login.', 'success');
                setTimeout(() => {
                    window.location.href = '/login';
                }, 1500);
            } else {
                showToast(data.detail || 'Registration failed', 'error');
            }
        } catch (err) {
            showToast('Connection error. Try again.', 'error');
        }
    });
}

// --- Dashboard ---
async function initDashboardPage(user) {
    const welcomeTitle = document.getElementById('welcome-user');
    if (welcomeTitle && user) {
        welcomeTitle.innerText = `Welcome back, ${user.username}!`;
    }

    initDashboardTabs();

    const token = getToken();
    try {
        const convRes = await fetch('/conversation/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const conversations = await convRes.json();

        const fbRes = await fetch('/feedback/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const feedbacks = await fbRes.json();

        document.getElementById('stat-conv-count').innerText = conversations.length || 0;

        if (feedbacks.length > 0) {
            let sumGrammar = 0, sumConf = 0, sumVocab = 0;
            feedbacks.forEach(fb => {
                sumGrammar += fb.grammar_score;
                sumConf += fb.confidence_score;
                sumVocab += fb.vocabulary_score;
            });
            const avgGrammar = Math.round(sumGrammar / feedbacks.length);
            const avgConf = Math.round(sumConf / feedbacks.length);

            document.getElementById('stat-avg-score').innerText = `${Math.round((avgGrammar + avgConf) / 2)}%`;
            document.getElementById('stat-feedback-count').innerText = feedbacks.length;

            renderSummarySuggestions(feedbacks);
        } else {
            document.getElementById('stat-avg-score').innerText = 'N/A';
            document.getElementById('stat-feedback-count').innerText = 0;
        }
    } catch (err) {
        console.error('Failed to load dashboard statistics', err);
    }
}

function renderSummarySuggestions(feedbacks) {
    const container = document.getElementById('summary-suggestions');
    if (!container) return;

    const recent = feedbacks.slice(-3).reverse();
    const suggestions = recent.filter(fb => fb.suggestions);

    if (suggestions.length === 0) {
        container.innerHTML = '<p class="text-muted">No coaching tips yet. Start a conversation to get feedback.</p>';
        return;
    }

    container.innerHTML = '';
    suggestions.forEach(fb => {
        const item = document.createElement('div');
        item.className = 'suggestion-item';
        item.innerHTML = `<p>${escapeHtml(fb.suggestions)}</p>`;
        container.appendChild(item);
    });
}

// --- Chat ---
async function initChatPage() {
    const newConvBtn = document.getElementById('new-conv-btn');
    const msgForm = document.getElementById('chat-form');

    if (newConvBtn && !newConvBtn.dataset.bound) {
        newConvBtn.dataset.bound = 'true';
        newConvBtn.addEventListener('click', createNewConversation);
    }

    if (msgForm && !msgForm.dataset.bound) {
        msgForm.dataset.bound = 'true';
        msgForm.addEventListener('submit', sendMessageSubmit);
    }

    await loadSidebarConversations();
}

async function loadSidebarConversations() {
    const convList = document.getElementById('conv-list');
    if (!convList) return;

    const token = getToken();
    try {
        const response = await fetch('/conversation/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const conversations = await response.json();

        if (conversations.length === 0) {
            convList.innerHTML = `<div class="empty-state" style="padding: 1rem;">No conversations yet</div>`;
            showEmptyChatState("Click '+ New' to start your first practice conversation.");
            return;
        }

        convList.innerHTML = '';
        conversations.forEach(conv => {
            const btn = document.createElement('button');
            btn.className = `conv-item ${activeConversationId === conv.id ? 'active' : ''}`;
            btn.innerHTML = `
                <h4>${escapeHtml(conv.title)}</h4>
                <span>Session #${conv.id}</span>
            `;
            btn.addEventListener('click', () => selectConversation(conv.id, conv.title));
            convList.appendChild(btn);
        });

        if (!activeConversationId && conversations.length > 0) {
            selectConversation(conversations[0].id, conversations[0].title);
        }
    } catch (err) {
        showToast('Error loading conversations', 'error');
    }
}

async function createNewConversation() {
    const title = prompt('Enter a title for your new conversation:');
    if (!title || !title.trim()) return;

    const token = getToken();
    try {
        const response = await fetch('/conversation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ title: title.trim() })
        });
        const data = await response.json();

        if (response.ok) {
            activeConversationId = data.id;
            await loadSidebarConversations();
            selectConversation(data.id, data.title);
            showToast('Conversation created!', 'success');
        } else {
            showToast(data.detail || 'Failed to create conversation', 'error');
        }
    } catch (err) {
        showToast('Connection error', 'error');
    }
}

function showEmptyChatState(msg) {
    const chatBox = document.getElementById('chat-box');
    if (chatBox) {
        chatBox.innerHTML = `
            <div class="empty-state">
                <p>${msg}</p>
            </div>
        `;
    }
    const headerTitle = document.getElementById('active-chat-title');
    if (headerTitle) headerTitle.innerText = "No Conversation Selected";
}

async function selectConversation(id, title) {
    activeConversationId = id;

    document.querySelectorAll('.conv-item').forEach(item => {
        item.classList.remove('active');
        if (item.querySelector('span').innerText.includes(`#${id}`)) {
            item.classList.add('active');
        }
    });

    const headerTitle = document.getElementById('active-chat-title');
    if (headerTitle) {
        headerTitle.innerText = title;
    }

    await loadMessages(id);
}

async function loadMessages(conversationId) {
    const chatBox = document.getElementById('chat-box');
    if (!chatBox) return;

    chatBox.innerHTML = '<div class="loading-text">Loading messages...</div>';

    const token = getToken();
    try {
        const response = await fetch(`/message/${conversationId}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const messages = await response.json();

        if (messages.length === 0) {
            chatBox.innerHTML = `
                <div class="empty-state">
                    <p>Send a message to start. The coach will correct spelling and guide you to improve.</p>
                </div>
            `;
            return;
        }

        chatBox.innerHTML = '';
        messages.forEach(msg => {
            const bubbleWrapper = document.createElement('div');
            bubbleWrapper.className = `msg-bubble-wrapper ${msg.role === 'user' ? 'user' : 'coach'}`;

            bubbleWrapper.innerHTML = `
                <div class="msg-bubble">${escapeHtml(msg.content)}</div>
            `;
            chatBox.appendChild(bubbleWrapper);
        });

        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (err) {
        chatBox.innerHTML = '<div class="loading-text" style="color: var(--error);">Error loading messages</div>';
    }
}

async function sendMessageSubmit(e) {
    e.preventDefault();
    if (!activeConversationId) {
        showToast('Please select or create a conversation first', 'error');
        return;
    }

    const form = e.target;
    const textarea = form.querySelector('textarea');
    const submitBtn = form.querySelector('button[type="submit"]');
    const text = textarea.value.trim();

    if (!text) return;

    textarea.value = '';
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = '...';
    }

    const chatBox = document.getElementById('chat-box');
    if (chatBox) {
        const userBubble = document.createElement('div');
        userBubble.className = 'msg-bubble-wrapper user';
        userBubble.innerHTML = `<div class="msg-bubble">${escapeHtml(text)}</div>`;
        chatBox.appendChild(userBubble);

        const typingBubble = document.createElement('div');
        typingBubble.className = 'msg-bubble-wrapper coach';
        typingBubble.id = 'typing-indicator';
        typingBubble.innerHTML = `<div class="msg-bubble" style="color: var(--text-muted); font-style: italic;">Coach is thinking...</div>`;
        chatBox.appendChild(typingBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    const token = getToken();
    try {
        const response = await fetch(`/message/${activeConversationId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ content: text })
        });

        if (response.ok) {
            await loadMessages(activeConversationId);
        } else {
            const errData = await response.json();
            showToast(errData.detail || 'Failed to send message', 'error');
            await loadMessages(activeConversationId);
        }
    } catch (err) {
        showToast('Failed to connect to server', 'error');
    } finally {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerText = 'Send';
        }
    }
}

// --- Feedback ---
async function initFeedbackPage() {
    const token = getToken();
    try {
        const response = await fetch('/feedback/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const feedbacks = await response.json();

        const container = document.getElementById('feedback-content');
        if (!container) return;

        if (feedbacks.length === 0) {
            container.innerHTML = `
                <div class="empty-state" style="margin-top: 2rem;">
                    <p>No feedback yet. Practice in the Chat tab to get coaching scores and suggestions.</p>
                </div>
            `;
            return;
        }

        let sumGrammar = 0, sumConf = 0, sumVocab = 0;
        feedbacks.forEach(fb => {
            sumGrammar += fb.grammar_score;
            sumConf += fb.confidence_score;
            sumVocab += fb.vocabulary_score;
        });

        const avgGrammar = Math.round(sumGrammar / feedbacks.length);
        const avgConf = Math.round(sumConf / feedbacks.length);
        const avgVocab = Math.round(sumVocab / feedbacks.length);

        container.innerHTML = `
            <div class="feedback-grid">
                <div class="card feedback-card">
                    <h3>Grammar</h3>
                    <div class="score-circle">${avgGrammar}%</div>
                    <p class="feedback-desc">Spelling, punctuation, and sentence structure.</p>
                </div>
                <div class="card feedback-card">
                    <h3>Confidence</h3>
                    <div class="score-circle green">${avgConf}%</div>
                    <p class="feedback-desc">Clear and assertive communication style.</p>
                </div>
                <div class="card feedback-card">
                    <h3>Vocabulary</h3>
                    <div class="score-circle purple">${avgVocab}%</div>
                    <p class="feedback-desc">Word variety and descriptive language.</p>
                </div>
            </div>

            <div class="card">
                <h3 style="margin-top:0;">Coaching Suggestions</h3>
                <div id="suggestions-list"></div>
            </div>
        `;

        const sugList = document.getElementById('suggestions-list');
        const uniqueSuggestions = [...new Set(feedbacks.slice(-5).map(fb => fb.suggestions).reverse())];

        uniqueSuggestions.forEach(sugText => {
            if (!sugText) return;
            const item = document.createElement('div');
            item.className = 'suggestion-item';
            item.innerHTML = `<p>${escapeHtml(sugText)}</p>`;
            sugList.appendChild(item);
        });

    } catch (err) {
        showToast('Error loading feedback', 'error');
    }
}

// Helpers
function escapeHtml(text) {
    if (!text) return '';
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}
