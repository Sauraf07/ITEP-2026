import RoadmapStep from "../models/roadmap.model.js";

export const generateRoadmap = async (req, res) => {

  try {

    const { career_id } = req.body;

    const roadmap = await RoadmapStep.findAll({
      where: { career_id },
      order: [["step_order", "ASC"]]
    });

    res.json(roadmap);

  } catch (error) {

    res.status(500).json({
      message: "Error generating roadmap"
    });

  }

};

export const getRoadmap = async (req, res) => {

  try {

    const { userId } = req.params;

    const roadmap = await RoadmapStep.findAll();

    res.json(roadmap);

  } catch (error) {

    res.status(500).json({
      message: "Error fetching roadmap"
    });

  }

};