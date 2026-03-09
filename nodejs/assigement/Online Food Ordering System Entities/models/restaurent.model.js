import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Restaurant = sequelize.define("Restaurant", {
  name: DataTypes.STRING,
  location: DataTypes.STRING
});

export default Restaurant;