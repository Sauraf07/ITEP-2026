import express from "express";
import bodyParser from "body-parser";

import authRoutes from "./routes/auth.route.js";
import taskRoutes from "./routes/task.route.js";

const app = express();

app.use(bodyParser.json());

app.use("/auth", authRoutes);
app.use("/tasks", taskRoutes);

export default app;