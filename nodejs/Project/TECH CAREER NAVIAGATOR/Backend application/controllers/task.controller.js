import DailyTask from "../models/dailytask.model.js";

export const generateTasks = async (req, res) => {

  try {

    const { user_id, tasks } = req.body;

    const createdTasks = [];

    let day = 1;

    for (let task of tasks) {

      const newTask = await DailyTask.create({
        user_id,
        task,
        day_number: day
      });

      createdTasks.push(newTask);

      day++;

    }

    res.json({
      message: "Tasks generated",
      createdTasks
    });

  } catch (error) {

    res.status(500).json({
      message: "Error generating tasks"
    });

  }

};

export const getTasks = async (req, res) => {

  try {

    const { userId } = req.params;

    const tasks = await DailyTask.findAll({
      where: { user_id: userId }
    });

    res.json(tasks);

  } catch (error) {

    res.status(500).json({
      message: "Error fetching tasks"
    });

  }

};

export const completeTask = async (req, res) => {

  try {

    const { task_id } = req.body;

    const task = await DailyTask.findByPk(task_id);

    task.is_completed = true;

    await task.save();

    res.json({
      message: "Task completed"
    });

  } catch (error) {

    res.status(500).json({
      message: "Error updating task"
    });

  }

};