import CareerPath from "../models/careerpath.model.js";

export const getCareerPaths = async (req, res) => {

  try {

    const careers = await CareerPath.findAll();

    res.json(careers);

  } catch (error) {

    res.status(500).json({
      message: "Error fetching careers"
    });

  }

};

export const selectCareer = async (req, res) => {

  try {

    const { user_id, career_id } = req.body;

    res.json({
      message: "Career selected",
      user_id,
      career_id
    });

  } catch (error) {

    res.status(500).json({
      message: "Error selecting career"
    });

  }

};