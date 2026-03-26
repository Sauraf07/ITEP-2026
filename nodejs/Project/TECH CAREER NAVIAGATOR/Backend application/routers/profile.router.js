import express from "express";
import { createProfile, getProfile } from "../controllers/profile.controller.js";
import { authenticate } from "../middleware/auth.middleware.js";
 
const router = express.Router();
 
router.get("/:userId", authenticate, getProfile);
 
router.post("/create", authenticate, createProfile);
 
export default router;