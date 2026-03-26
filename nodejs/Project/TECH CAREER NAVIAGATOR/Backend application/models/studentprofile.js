
import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const StudentProfile = sequelize.define("StudentProfile", {

  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true
  },

  user_id: {
    type: DataTypes.INTEGER,
    allowNull: false   
  },

  course: {
    type: DataTypes.STRING,
    allowNull: false
  },
  semester: {
    type: DataTypes.INTEGER,
    allowNull: false 

}})

export default StudentProfile;