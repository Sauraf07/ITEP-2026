import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const Lesson = sequelize.define("Lesson", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    title: DataTypes.STRING
});

export default Lesson;