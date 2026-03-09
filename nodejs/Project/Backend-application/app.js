import express from "express";
import bodyParser from "body-parser";
import userRoutes from "./routers/user.routes.js";

const app = express();

app.use(bodyParser.json());

app.use("/api/users", userRoutes);

export default app;