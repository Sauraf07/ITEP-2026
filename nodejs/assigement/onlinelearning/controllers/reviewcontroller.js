import { Review } from "../assoisaction/asso.js";
export const constReview = async(req,res)=>{
    const review = await Review.create(req.body);
    res.json(review);
} 
export const getreview = async(req,res)=>{
    const review = await Review.findAll();
    res.json(review);
}