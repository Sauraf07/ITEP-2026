import CareerPath from "../models/careerpath.model.js";

export const getCareerPaths = async (req, res, next) => {
  try {
    const careers = await CareerPath.findAll({
      where: { user_id: 0 },
      attributes: ['id', 'career_field', 'description']
    });
    res.json({
      message: "All IT careers",
      careers
    });
  } catch (error) {
    next(error);
  }
};

export const selectCareer = async (req, res, next) => {
  try {
    const { user_id, career_field } = req.body;

    if (!user_id || !career_field) {
      return res.status(400).json({
        message: "Please provide user_id and career_field"
      });
    }

    const existingCareer = await CareerPath.findOne({
      where: { user_id }
    });

    if (existingCareer) {
      existingCareer.career_field = career_field;
      await existingCareer.save();
      return res.json({
        message: "Career updated successfully",
        career: existingCareer
      });
    }

    const career = await CareerPath.create({
      user_id,
      career_field,
      description: `Selected career path: ${career_field}`
    });

    res.status(201).json({
      message: "Career selected successfully",
      career
    });

  } catch (error) {
    next(error);
  }
};

export const getUserCareer = async (req, res, next) => {
  try {
    const { userId } = req.params;

    if (!userId) {
      return res.status(400).json({
        message: "Please provide userId"
      });
    }

    const career = await CareerPath.findOne({
      where: { user_id: userId }
    });

    if (!career) {
      return res.status(404).json({
        message: "No career selected yet"
      });
    }

    res.json({
      message: "User career",
      career
    });

  } catch (error) {
    next(error);
  }
};