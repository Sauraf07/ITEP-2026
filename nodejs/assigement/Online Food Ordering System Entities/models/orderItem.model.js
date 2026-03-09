import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";
import Order from "./order.model.js";
import MenuItem from "./menuItem.model.js";

const OrderItem = sequelize.define("OrderItem", {
  quantity: DataTypes.INTEGER
});

Order.hasMany(OrderItem, { onDelete: "CASCADE" });
OrderItem.belongsTo(Order);

MenuItem.hasMany(OrderItem);
OrderItem.belongsTo(MenuItem);

export default OrderItem;