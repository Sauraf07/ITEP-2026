import express from "express";
import {
  seedAllData,
  getImportantSubjects,
  getAllCareers,
  getCareerRoadmap
} from "../controllers/seed.controller.js";

const router = express.Router();

router.post("/seed", seedAllData);
router.get("/subjects/important", getImportantSubjects);
router.get("/careers/all", getAllCareers);
router.get("/careers/:careerField/roadmap", getCareerRoadmap);

export default router;
