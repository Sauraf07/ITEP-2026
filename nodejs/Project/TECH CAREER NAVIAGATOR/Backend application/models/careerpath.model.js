import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const CareerPath = sequelize.define("CareerPath", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },

  career_field: {
    type: DataTypes.STRING,
    allowNull: false
  },

  description: {
    type: DataTypes.TEXT
  }

});

export default CareerPath;