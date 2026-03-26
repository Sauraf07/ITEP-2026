// ✅ NEW FILE: Progress model bilkul missing tha project mein
//    task.controller.js mein Progress import tha par model tha hi nahi

import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Progress = sequelize.define("Progress", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },

  completed_tasks: {
    type: DataTypes.INTEGER,
    defaultValue: 0,
    allowNull: false
  },

  total_tasks: {
    type: DataTypes.INTEGER,
    defaultValue: 0,
    allowNull: false
  }

});

export default Progress;