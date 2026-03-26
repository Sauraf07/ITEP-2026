import CareerPath from "../models/careerpath.model.js";

export const getCareerPaths = async (req, res, next) => {
  try {
    const careers = await CareerPath.findAll();
    res.json(careers);
  } catch (error) {
    next(error);
  }
};

export const selectCareer = async (req, res, next) => {
  try {
    const { user_id, career_field } = req.body;

    // ✅ BUG FIX 2: career_id ki jagah career_field use karo (string-based)
    // ✅ BUG FIX 3: Career DB mein save hi nahi ho rahi thi — sirf echo ho raha tha
    //    Isiliye roadmap generate nahi hota tha — career_field exist hi nahi karta tha DB mein
    if (!user_id || !career_field) {
      return res.status(400).json({
        message: "Please provide user_id and career_field"
      });
    }

    const career = await CareerPath.create({
      user_id,
      career_field
    });

    res.status(201).json({
      message: "Career selected and saved successfully",
      career
    });

  } catch (error) {
    next(error);
  }
};