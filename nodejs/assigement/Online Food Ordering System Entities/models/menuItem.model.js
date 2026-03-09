import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";
import Restaurant from "./restaurent.model.js";

const MenuItem = sequelize.define("MenuItem", {
  name: DataTypes.STRING,
  price: DataTypes.FLOAT
});

Restaurant.hasMany(MenuItem, { onDelete: "CASCADE" });
MenuItem.belongsTo(Restaurant);

export default MenuItem;