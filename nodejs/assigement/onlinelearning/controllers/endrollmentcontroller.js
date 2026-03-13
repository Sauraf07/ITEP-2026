import { Enrollment } from "../assoisaction/asso.js"
export const genendrollment = async(req,res)=>{
    const endrollment = await Enrollment.create(req.body);
    res.json(endrollment);
};
export const getendndrollment = async(req,res)=>{
    const endrollment = await Enrollment.findAll();
    res.json(endrollment);
}