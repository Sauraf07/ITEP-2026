import StudentProfile from "../models/studentprofile.js";

export const createProfile = async (req, res) => {

  try {

    const { user_id, course, semester } = req.body;

    const profile = await StudentProfile.create({
      user_id,
      course,
      semester
    });

    res.json({
      message: "Profile created",
      profile
    });

  } catch (error) {

    res.status(500).json({
      message: "Error creating profile"
    });

  }

};

export const getProfile = async (req, res) => {

  try {

    const { userId } = req.params;

    const profile = await StudentProfile.findOne({
      where: { user_id: userId }
    });

    res.json(profile);

  } catch (error) {

    res.status(500).json({
      message: "Error fetching profile"
    });

  }

};