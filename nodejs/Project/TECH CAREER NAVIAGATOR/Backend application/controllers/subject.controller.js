import Subject from "../models/subject.model.js";

const importantSubjects = [
  "Data Structures",
  "DBMS",
  "Operating Systems",
  "Computer Networks",
  "Algorithms"
];

export const addSubject = async (req, res) => {

  try {

    const { user_id, subject_name } = req.body;

    const subject = await Subject.create({
      user_id,
      subject_name
    });

    res.json({
      message: "Subject added",
      subject
    });

  } catch (error) {

    res.status(500).json({
      message: "Error adding subject"
    });

  }

};

export const getSubjects = async (req, res) => {

  try {

    const { userId } = req.params;

    const subjects = await Subject.findAll({
      where: { user_id: userId }
    });

    res.json(subjects);

  } catch (error) {

    res.status(500).json({
      message: "Error fetching subjects"
    });

  }

};

export const filterImportantSubjects = async (req, res) => {

  try {

    const { user_id } = req.body;

    const subjects = await Subject.findAll({
      where: { user_id }
    });

    for (let subject of subjects) {

      if (importantSubjects.includes(subject.subject_name)) {

        subject.is_important = true;
        await subject.save();

      }

    }

    res.json({
      message: "Important subjects updated"
    });

  } catch (error) {

    res.status(500).json({
      message: "Error filtering subjects"
    });

  }

};