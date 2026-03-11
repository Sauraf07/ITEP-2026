import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";
const Review = sequelize.define("Review", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    rating: DataTypes.INTEGER,
    comment: DataTypes.STRING
});

export default Review;