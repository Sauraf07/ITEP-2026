import express from "express";
import bodyParser from "body-parser";

import StudentRouter from "./routers/student.router.js"
import CourseRouter from "./routers/course.router.js"

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/user",StudentRouter);
app.use("/course",CourseRouter);


app.listen(3000,()=>{
    console.log("Server Started...");
});