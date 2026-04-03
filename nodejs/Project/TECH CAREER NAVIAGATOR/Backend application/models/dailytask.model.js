import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const DailyTask = sequelize.define("DailyTask", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },

  task_description: {
    type: DataTypes.STRING,
    allowNull: false
  },

  day_number: {
    type: DataTypes.INTEGER,
    allowNull: false
  },

  is_completed: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  }

});

export default DailyTask;