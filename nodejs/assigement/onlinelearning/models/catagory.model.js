import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const Category = sequelize.define("Category", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name: DataTypes.STRING
});

export default Category;