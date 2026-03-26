import { Sequelize } from "sequelize";

const sequelize = new Sequelize("taskmanager", "root", "root", {
  host: "localhost",
  dialect: "mysql"
});
export default sequelize;