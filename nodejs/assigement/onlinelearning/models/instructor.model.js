import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const Instructor = sequelize.define("Instructor", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name: DataTypes.STRING
});

export default Instructor;