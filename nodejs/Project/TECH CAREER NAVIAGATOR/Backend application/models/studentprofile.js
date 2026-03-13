import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const StudentProfile = sequelize.define("StudentProfile", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER
  },

  course: {
    type: DataTypes.STRING
  },

  semester: {
    type: DataTypes.INTEGER
  }

});

export default StudentProfile;