import { Lesson } from "../assoisaction/asso.js"
export const createLesson = async(req,res)=>{
    const lesson = await Lesson.create(req.body);
    res.json(Lesson)
}
export const getLesson = async (req,res)=>{
    const lesson = await Lesson.findAll();
    res.json(lesson)
}