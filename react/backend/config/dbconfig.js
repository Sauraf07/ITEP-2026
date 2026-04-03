import { Sequelize } from "sequelize";

const sequelize = new Sequelize("testdb","root","root",{
    host: "localhost",
    dialect: "mysql"
});
sequelize.sync()
.then(()=>{
    console.log("Database created...");
}).catch(err=>{
    console.log(err);
})
export default sequelize;