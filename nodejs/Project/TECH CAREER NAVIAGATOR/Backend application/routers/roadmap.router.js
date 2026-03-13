import express from "express";
import {
  generateRoadmap,
  getRoadmap
} from "../controllers/roadmap.controller.js";

const router = express.Router();

router.post("/generate", generateRoadmap);

router.get("/:userId", getRoadmap);

export default router;