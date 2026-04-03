import Subject from "../models/subject.model.js";

const importantSubjects = [
  "Data Structures",
  "Algorithms", 
  "Database Management Systems (DBMS)",
  "Operating Systems",
  "Computer Networks",
  "Object Oriented Programming (OOP)",
  "Web Development",
  "JavaScript/TypeScript",
  "Python Programming",
  "Java Programming",
  "SQL Queries",
  "Cloud Computing",
  "Docker & Kubernetes",
  "Git & Version Control",
  "REST APIs",
  "Machine Learning Basics",
  "System Design",
  "Cybersecurity Fundamentals",
  "Linux/Unix Systems",
  "DevOps Tools"
];

export const getImportantSubjectsList = async (req, res, next) => {
  try {
    res.json({
      message: "Important IT subjects",
      subjects: importantSubjects.map((s, i) => ({
        id: i + 1,
        name: s,
        importance: 8
      }))
    });
  } catch (error) {
    next(error);
  }
};

export const addSubject = async (req, res, next) => {
  try {
    const { user_id, subject_name } = req.body;

    if (!user_id || !subject_name) {
      return res.status(400).json({
        message: "Please provide user_id and subject_name"
      });
    }

    const subject = await Subject.create({
      user_id,
      subject_name,
      is_important: importantSubjects.includes(subject_name)
    });

    res.json({
      message: "Subject added",
      subject
    });

  } catch (error) {
    next(error);
  }
};

export const getUserSubjects = async (req, res, next) => {
  try {
    const { userId } = req.params;

    if (!userId) {
      return res.status(400).json({
        message: "Please provide userId"
      });
    }

    const subjects = await Subject.findAll({
      where: { user_id: userId }
    });

    res.json({
      message: "User subjects",
      total: subjects.length,
      subjects
    });

  } catch (error) {
    next(error);
  }
};

export const markSubjectImportant = async (req, res, next) => {
  try {
    const { subject_id } = req.params;

    if (!subject_id) {
      return res.status(400).json({
        message: "Please provide subject_id"
      });
    }

    const subject = await Subject.findByPk(subject_id);

    if (!subject) {
      return res.status(404).json({
        message: "Subject not found"
      });
    }

    subject.is_important = true;
    await subject.save();

    res.json({
      message: "Subject marked as important",
      subject
    });

  } catch (error) {
    next(error);
  }
};

export const filterImportantSubjects = async (req, res, next) => {
  try {
    const { user_id } = req.body;

    if (!user_id) {
      return res.status(400).json({
        message: "Please provide user_id"
      });
    }

    const subjects = await Subject.findAll({
      where: { user_id, is_important: true }
    });

    res.json({
      message: "Important subjects for user",
      total: subjects.length,
      subjects
    });

  } catch (error) {
    next(error);
  }
};