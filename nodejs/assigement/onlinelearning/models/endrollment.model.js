import { DataTypes } from "sequelize";
import sequelize from "../dbconfig.js";

const Enrollment = sequelize.define("Enrollment", {
    enroll_date: {
        type: DataTypes.DATE,
        defaultValue: DataTypes.NOW
    }
});

export default Enrollment;