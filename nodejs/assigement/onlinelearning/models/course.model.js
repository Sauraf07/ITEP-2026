import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const Course = sequelize.define("Course", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    title: DataTypes.STRING
});

export default Course;