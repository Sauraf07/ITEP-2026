import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const CareerPath = sequelize.define("CareerPath", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  name: {
    type: DataTypes.STRING
  }

});

export default CareerPath;