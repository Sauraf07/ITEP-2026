import { Sequelize } from "sequelize";

const sequelize = new Sequelize("food_order_db", "root", "Saurav23@", {
  host: "localhost",
  dialect: "mysql"
});

export default sequelize;