import express from "express";
import Task from "../models/task.model.js";
import { auth } from "../middleware/auth.middleware.js";

const router = express.Router();

router.use(auth);
router.post("/", async (req, res) => {
  const task = await Task.create({
    ...req.body,
    UserId: req.userId
  });
  res.json(task);
});
router.get("/", async (req, res) => {
  const tasks = await Task.findAll({
    where: { UserId: req.userId }
  });
  res.json(tasks);
});

router.put("/:id", async (req, res) => {
  const task = await Task.findByPk(req.params.id);
  if (!task) return res.send("Not found");
  await task.update(req.body);
  res.json(task);
});

router.delete("/:id", async (req, res) => {
  const task = await Task.findByPk(req.params.id);
  if (!task) return res.send("Not found");
  await task.destroy();
  res.send("Deleted");
});

export default router;