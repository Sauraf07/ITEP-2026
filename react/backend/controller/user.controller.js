import { validationResult } from "express-validator"
import User from "../models/user.model.js"
import bcrypt from "bcryptjs"
import jwt from "jsonwebtoken"
import dotenv from "dotenv"
dotenv.config();
export const signInAction = async (request,response,next)=>{
    try{
       let {email,password} = request.body;
       let dbUser = await User.findOne({where: {email}, raw: true});
       if(!dbUser)
        return response.status(400).json({error: "Bad request | Invalid email id"});
       
       let status = await bcrypt.compare(password,dbUser.password);

       return status ? response.status(200).json({message: "Sign in success",token: generateToken(dbUser),user: dbUser}) : response.status(400).json({error: "Invalid user | Credentails not matched"});
    }
    catch(err){
        console.log(err);
        return response.status(500).json({error: "Internal Server Error"});
    }
}
export const signUpAction = async (request,response,next)=>{
   try{ 
    const errors = validationResult(request);
    if(!errors.isEmpty())
        return response.status(400).json({error: errors.array()});
    let password = request.body.password;
    let saltKey = await bcrypt.genSalt(10);
    password = await bcrypt.hash(password,saltKey);
    request.body.password = password;
    let dbUser = await User.create(request.body);
    return response.status(201).json({message: "Sign up success", user: dbUser});
   }
   catch(err){
    return response.status(500).json({error: "Internal Server Error.."});
   }

}

const generateToken = (user)=>{
    let payload = {userId: user.id, email: user.email};
    return jwt.sign(payload,process.env.TOKEN_SECRET);
}