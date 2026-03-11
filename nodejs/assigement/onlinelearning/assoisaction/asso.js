import Student from "../models/student.model.js";
import StudentProfile from "../models/profile.model.js";
import Instructor from "../models/instructor.model.js";
import Course from "../models/course.model.js";
import Lesson from "../models/lesson.model.js";
import Category from "../models/catagory.model.js";
import Enrollment from "../models/endrollment.model.js";
import Review from "../models/review.model.js";


Student.hasOne(StudentProfile)
StudentProfile.belongsTo(Student)


Instructor.hasMany(Course);
Course.belongsTo(Instructor);



Course.hasMany(Lesson);
Lesson.belongsTo(Course);



Student.hasMany(Review);
Course.hasMany(Review);
Review.belongsTo(Student);
Review.belongsTo(Course);



Student.belongsToMany(Course, { through: Enrollment });
Course.belongsToMany(Student, { through: Enrollment });



Course.belongsToMany(Category, { through: "CourseCategory" });
Category.belongsToMany(Course, { through: "CourseCategory" });


export {
Student,
StudentProfile,
Instructor,
Course,
Lesson,
Review,
Category,
Enrollment
};