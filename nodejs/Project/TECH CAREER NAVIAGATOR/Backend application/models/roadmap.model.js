import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const RoadmapStep = sequelize.define("RoadmapStep", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  career_field: {
    type: DataTypes.STRING,
    allowNull: false
  },

  step_number: {
    type: DataTypes.INTEGER,
    allowNull: false
  },

  step_title: {
    type: DataTypes.STRING,
    allowNull: false
  },

  description: {
    type: DataTypes.TEXT
  },

  resources: {
    type: DataTypes.JSON
  }

});

export default RoadmapStep;