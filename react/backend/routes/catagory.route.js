import express from "express";
import { saveInBulk, fetchAll } from "../controller/catagory.controller.js";

const router = express.Router();

router.post("/save-in-bulk",saveInBulk);
router.get("/",fetchAll);
export default router;