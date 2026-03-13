import express from "express";
import { createProfile, getProfile } from "../controllers/profile.controller.js";
import { authenticate } from "../middleware/authMiddleware.js";
const router = express.Router();
router.get("/:userId", authenticate, getProfile);
router.post("/create", createProfile);

router.get("/:userId", getProfile);

export default router;