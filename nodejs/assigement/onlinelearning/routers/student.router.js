import express from "express";
import { createStudent, getStudents } from "../controllers/studentcontroller.js";

const router = express.Router();

router.post("/students", createStudent);
router.get("/students", getStudents);

export default router;