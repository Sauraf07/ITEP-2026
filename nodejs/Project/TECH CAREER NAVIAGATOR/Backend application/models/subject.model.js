import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Subject = sequelize.define("Subject", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER,
    allowNull: false   
  },

  subject_name: {
    type: DataTypes.STRING,
    allowNull: false   
  },

  is_important: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  }

});

export default Subject;