import express from "express";
import {
  generateTasks,
  getTasks,
  completeTask
} from "../controllers/task.controller.js";

const router = express.Router();

router.post("/generate", generateTasks);

router.get("/:userId", getTasks);

router.post("/complete", completeTask);

export default router;