import { Sequelize } from "sequelize";

const sequelize = new Sequelize(
    "tech_career_navigator",
    "root","root",{
        host: "localhost",
        dialect: "mysql"
    }
)

export default sequelize;
