import express from "express";
import bodyParser from "body-parser";
import cors from "cors";

import restaurantRoutes from "./routes/restaurant.routes.js";
import userRoutes from "./routes/user.routes.js";
import orderRoutes from "./routes/order.routes.js";

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.use(restaurantRoutes);
app.use(userRoutes);
app.use(orderRoutes);

export default app;