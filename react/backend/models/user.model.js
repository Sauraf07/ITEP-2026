import { DataTypes, STRING } from "sequelize"
import sequelize from "../config/dbconfig.js"
const User = sequelize.define("users",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name:{
       type: DataTypes.STRING,
       allowNull: false
    },
    email:{
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password:{
        type: DataTypes.STRING,
        allowNull: false
    },
    contact:{
        type:DataTypes.STRING,
        unique: true
    },
    address: DataTypes.STRING  
});

export default User;