import RoadmapStep from "../models/roadmap.model.js";
import CareerPath from "../models/careerpath.model.js";

export const generateRoadmap = async (req, res, next) => {
  try {
    const { user_id, career_field } = req.body;

    if (!career_field) {
      return res.status(400).json({
        message: "Please provide career_field"
      });
    }

    const roadmap = await RoadmapStep.findAll({
      where: { career_field },
      order: [["step_number", "ASC"]]  
    });

    if (roadmap.length === 0) {
      return res.status(404).json({
        message: `No roadmap found for career: ${career_field}`
      });
    }

    res.json({
      message: "Roadmap generated successfully",
      career_field,
      total_steps: roadmap.length,
      roadmap
    });

  } catch (error) {
    next(error);
  }
};

export const getRoadmap = async (req, res, next) => {
  try {
    const { userId } = req.params;

    const careerChoice = await CareerPath.findOne({
      where: { user_id: userId }
    });

    if (!careerChoice) {
      return res.status(404).json({
        message: "No career selected for this user. Please select a career first."
      });
    }

    const roadmap = await RoadmapStep.findAll({
      where: { career_field: careerChoice.career_field },
      order: [["step_number", "ASC"]]
    });

    res.json({
      message: "Roadmap fetched successfully",
      career_field: careerChoice.career_field,
      total_steps: roadmap.length,
      roadmap
    });

  } catch (error) {
    next(error);
  }
};