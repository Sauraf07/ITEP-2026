import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Bus = sequelize.define("Bus", {
  bus_name: DataTypes.STRING,
  bus_number: DataTypes.STRING,
  source: DataTypes.STRING,
  destination: DataTypes.STRING,
  price: DataTypes.INTEGER,
  total_seats: DataTypes.INTEGER
});

export default Bus;