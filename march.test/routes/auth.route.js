import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import User from "../models/user.model.js";

const router = express.Router();
router.post("/signup", async (req, res) => {
  const { name, email, password } = req.body;

  const hash = await bcrypt.hash(password, 10);

  const user = await User.create({
    name,
    email,
    password: hash
  });

  res.json(user);
});
router.post("/signin", async (req, res) => {
  const { email, password } = req.body;

  const user = await User.findOne({ where: { email } });

  if (!user) return res.send("User not found");

  const ok = await bcrypt.compare(password, user.password);

  if (!ok) return res.send("Wrong password");

  const token = jwt.sign({ id: user.id }, "secret");

  res.json({ token });
});

export default router;