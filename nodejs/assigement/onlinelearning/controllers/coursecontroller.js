import { Course } from "../assoisaction/asso.js"
export const createCourse = async(req,res)=>{
    const course = await Course.create(req.body);
    res.json(course);
};
export const getCourse = async (req,res)=>{
    const courses = await Course.findAll();
    res.josn(courses);
}