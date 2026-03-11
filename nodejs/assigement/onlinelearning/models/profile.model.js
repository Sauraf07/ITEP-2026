import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const StudentProfile = sequelize.define("StudentProfile", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    address: DataTypes.STRING,
    phone: DataTypes.STRING
});

export default StudentProfile;