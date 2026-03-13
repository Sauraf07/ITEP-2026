import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const RoadmapStep = sequelize.define("RoadmapStep", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  career_id: {
    type: DataTypes.INTEGER
  },

  step_order: {
    type: DataTypes.INTEGER
  },

  step_title: {
    type: DataTypes.STRING
  }

});

export default RoadmapStep;