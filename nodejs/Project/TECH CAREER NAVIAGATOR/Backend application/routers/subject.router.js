import express from "express";
import {
  addSubject,
  getSubjects,
  filterImportantSubjects
} from "../controllers/subject.controller.js";

const router = express.Router();

router.post("/add", addSubject);

router.get("/:userId", getSubjects);

router.post("/filter-important", filterImportantSubjects);

export default router;