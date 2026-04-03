import express from "express";
import {
  addSubject,
  getUserSubjects,
  filterImportantSubjects,
  markSubjectImportant,
  getImportantSubjectsList
} from "../controllers/subject.controller.js";

const router = express.Router();

router.get("/important-list", getImportantSubjectsList);
router.post("/add", addSubject);
router.get("/:userId", getUserSubjects);
router.post("/filter-important", filterImportantSubjects);
router.put("/:subject_id/mark-important", markSubjectImportant);

export default router;