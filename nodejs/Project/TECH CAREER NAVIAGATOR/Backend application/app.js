import "./models/user.model.js";
import "./models/studentprofile.js";
import "./models/subject.model.js";
import "./models/careerpath.model.js";
import "./models/roadmap.model.js";
import "./models/dailytask.model.js";

import authRoutes from "./routers/auth.router.js";
import profileRoutes from "./routers/profile.router.js";
import subjectRoutes from "./routers/subject.router.js";
import careerRoutes from "./routers/career.router.js";
import roadmapRoutes from "./routers/roadmap.router.js";
import taskRoutes from "./routers/task.router.js";
import { errorHandler } from "./middleware/error.middleware.js";
import express from "express";
import bodyParser from "body-parser";
import sequelize from "./config/database.js";

const app = express();

// ⭐ Middleware FIRST
app.use(errorHandler);
app.use(bodyParser.json());
app.use(express.json());

// Routes AFTER middleware
app.use("/api/auth", authRoutes);
app.use("/api/profile", profileRoutes);
app.use("/api/subjects", subjectRoutes);
app.use("/api/career", careerRoutes);
app.use("/api/roadmap", roadmapRoutes);
app.use("/api/tasks", taskRoutes);

app.get("/", (req, res) => {
  res.send("Tech Career Navigator API is running");
});

sequelize.sync()
.then(() => {
  console.log("Database connected...");
})
.catch((err) => {
  console.log("Database connection error", err);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});