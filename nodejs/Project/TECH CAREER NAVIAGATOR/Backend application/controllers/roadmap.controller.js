import RoadmapStep from "../models/roadmap.model.js";
import CareerPath from "../models/careerpath.model.js";

export const generateRoadmap = async (req, res, next) => {
  try {
    const { user_id, career_field } = req.body;

    // ✅ BUG FIX 4: career_id ki jagah career_field use karo
    // ✅ BUG FIX 5: "step_order" galat column name tha — sahi naam "step_number" hai
    if (!career_field) {
      return res.status(400).json({
        message: "Please provide career_field"
      });
    }

    const roadmap = await RoadmapStep.findAll({
      where: { career_field },
      order: [["step_number", "ASC"]]  // ✅ step_order → step_number (correct column name)
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

    // ✅ BUG FIX 6: userId param use hi nahi ho raha tha — sab ka roadmap aa raha tha
    //    Pehle: RoadmapStep.findAll()  — koi filter nahi!
    //    Ab: user ki career choice dhundho, phir uski roadmap lo

    // Pehle user ki career choice nikalo
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