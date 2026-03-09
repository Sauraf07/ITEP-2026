import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";
import User from "./user.model.js";

const Order = sequelize.define("Order", {
  total_price: DataTypes.FLOAT
});

User.hasMany(Order);
Order.belongsTo(User);

export default Order;