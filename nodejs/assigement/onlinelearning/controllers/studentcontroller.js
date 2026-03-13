import { Student } from "../assoisaction/asso.js";

export const createStudent = async (req, res) => {
  const student = await Student.create(req.body);
  res.json(student);
};

export const getStudents = async (req, res) => {
  const students = await Student.findAll();
  res.json(students);
};