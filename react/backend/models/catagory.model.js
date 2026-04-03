import { DataTypes } from "sequelize";
import sequelize from "../config/dbconfig.js";
const Category = sequelize.define("categories",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    slug:{
        type: DataTypes.STRING,
        allowNull: false
    },
    name:{
        type: DataTypes.STRING
    },
    url: DataTypes.STRING
})
export default Category;