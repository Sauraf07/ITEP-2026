import express from "express";
import {
  selectCareer,
  getCareerPaths
} from "../controllers/career.controller.js";

const router = express.Router();

router.get("/paths", getCareerPaths);

router.post("/select", selectCareer);

export default router;