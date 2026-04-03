import express from "express";
import {
  selectCareer,
  getCareerPaths,
  getUserCareer
} from "../controllers/career.controller.js";

const router = express.Router();

router.get("/paths", getCareerPaths);
router.post("/select", selectCareer);
router.get("/user/:userId", getUserCareer);

export default router;