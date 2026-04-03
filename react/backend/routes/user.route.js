import express from "express";
import { signUpAction, signInAction } from "../controller/user.controller.js";
import { body } from "express-validator";

const router = express.Router();

router.post("/",
    body("name","name is required").notEmpty(),
    body("email","email id is required").notEmpty(),
    body("email","invalid email id").isEmail(),
    body("password","password is required").notEmpty(),
    body("password").isLength({min: 6, max: 10}),
    body("contact","only digits are allowed").isNumeric(),signUpAction);

router.post("/sign-in",signInAction);    
export default router;