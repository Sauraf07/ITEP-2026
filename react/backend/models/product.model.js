import { DataTypes, STRING } from "sequelize";
import sequelize from "../config/dbconfig.js";

const Product = sequelize.define("products",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    title: DataTypes.STRING,
    description: DataTypes.STRING,
    category: DataTypes.STRING,
    price: DataTypes.FLOAT,
    discountPercentage: DataTypes.FLOAT,
    rating: DataTypes.FLOAT,
    stock: DataTypes.INTEGER,
    brand: DataTypes.STRING,
    availabilityStatus: DataTypes.STRING,
    shippingInformation: DataTypes.STRING,
    warrantyInformation: DataTypes.STRING,
    thumbnail: DataTypes.STRING
});
export default Product;