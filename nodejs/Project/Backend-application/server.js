import app from "./app.js";
import sequelize from "./config/database.js";

const PORT = 3000;

sequelize.sync().then(() => {
  console.log("Database connected");

  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
});