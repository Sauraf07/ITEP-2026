import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Subject = sequelize.define("Subject", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER
  },

  subject_name: {
    type: DataTypes.STRING
  },

  is_important: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  }

});

export default Subject;