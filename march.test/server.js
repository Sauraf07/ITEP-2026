import express from "express";
import bodyParser from "body-parser";
import sequelize from "./config/db.js";

import authRoutes from "./routes/auth.route.js";
import taskRoutes from "./routes/task.route.js";

const app = express();

app.use(bodyParser.json());

app.use("/auth", authRoutes);
app.use("/tasks", taskRoutes);

sequelize.sync().then(() => {
  app.listen(3000, () => {
    console.log("Server running on 3000");
  });
});