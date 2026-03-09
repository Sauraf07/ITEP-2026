import express from "express";
import User from "../models/user.model.js";

const router = express.Router();

router.post("/users", async (req, res) => {
  const user = await User.create(req.body);
  res.json(user);
});

router.get("/users/:id", async (req, res) => {
  const user = await User.findByPk(req.params.id);
  res.json(user);
});

export default router;