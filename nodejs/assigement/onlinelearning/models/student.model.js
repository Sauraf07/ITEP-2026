import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";

const Student = sequelize.define("Student",{
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name:{ 
        type:DataTypes.STRING,
        allowNull: false
    },
    email:{
    type: DataTypes.STRING(100),
    allowNull: false,
    unique: true
   },
   password:{
    type:DataTypes.STRING,
    allowNull: false
   }
});
export default Student;