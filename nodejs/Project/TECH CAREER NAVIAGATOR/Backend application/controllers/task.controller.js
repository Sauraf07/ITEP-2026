import DailyTask from "../models/dailytask.model.js";
import Progress from "../models/Progress.model.js";

const DEFAULT_DAILY_TASKS = [
  "Review fundamentals of your selected area",
  "Complete coding challenges on LeetCode/HackerRank",
  "Study one new concept from your curriculum",
  "Work on a mini project related to today's learning",
  "Read 1 article from industry blog",
  "Practice interview questions",
  "Debug someone else's code on GitHub",
  "Document what you learned today",
  "Participate in online community discussion",
  "Review your previous day's work"
];

export const generateTasks = async (req, res, next) => {
  try {
    const { user_id, tasks } = req.body;

    if (!user_id) {
      return res.status(400).json({
        message: "Please provide user_id"
      });
    }
    const tasksToCreate = tasks && Array.isArray(tasks) && tasks.length > 0 
      ? tasks 
      : DEFAULT_DAILY_TASKS;

    const existingTasks = await DailyTask.findAll({
      where: { user_id }
    });

    if (existingTasks.length > 0) {
      return res.status(400).json({
        message: "Tasks already created for this user"
      });
    }

    const createdTasks = [];
    for (let i = 0; i < tasksToCreate.length; i++) {
      const newTask = await DailyTask.create({
        user_id,
        task_description: tasksToCreate[i],
        day_number: i + 1
      });
      createdTasks.push(newTask);
    }

    const existingProgress = await Progress.findOne({ where: { user_id } });

    if (existingProgress) {
      existingProgress.total_tasks = createdTasks.length;
      await existingProgress.save();
    } else {
      await Progress.create({
        user_id,
        completed_tasks: 0,
        total_tasks: createdTasks.length
      });
    }

    res.status(201).json({
      message: "Tasks generated successfully",
      total_tasks: createdTasks.length,
      createdTasks
    });

  } catch (error) {
    next(error);
  }
};

export const getTasks = async (req, res, next) => {
  try {
    const { userId } = req.params;

    if (!userId) {
      return res.status(400).json({
        message: "Please provide userId"
      });
    }

    const tasks = await DailyTask.findAll({
      where: { user_id: userId },
      order: [["day_number", "ASC"]]
    });

    res.json({
      message: "Tasks fetched successfully",
      total: tasks.length,
      tasks
    });

  } catch (error) {
    next(error);
  }
};

export const completeTask = async (req, res, next) => {
  try {
    const { task_id, user_id } = req.body;

    if (!task_id || !user_id) {
      return res.status(400).json({
        message: "Please provide task_id and user_id"
      });
    }

    const task = await DailyTask.findByPk(task_id);

    if (!task) {
      return res.status(404).json({
        message: "Task not found"
      });
    }

    if (task.is_completed) {
      return res.status(400).json({
        message: "Task already completed"
      });
    }

    task.is_completed = true;
    await task.save();

    const progress = await Progress.findOne({ where: { user_id } });

    if (progress) {
      progress.completed_tasks += 1;
      await progress.save();
    }

    const percentage = progress
      ? Math.round((progress.completed_tasks / progress.total_tasks) * 100)
      : 0;

    res.json({
      message: "Task completed successfully",
      task,
      progress: {
        completed: progress?.completed_tasks || 0,
        total: progress?.total_tasks || 0,
        percentage
      }
    });

  } catch (error) {
    next(error);
  }
};

export const getProgress = async (req, res, next) => {
  try {
    const { userId } = req.params;

    if (!userId) {
      return res.status(400).json({
        message: "Please provide userId"
      });
    }

    const progress = await Progress.findOne({ where: { user_id: userId } });

    if (!progress) {
      return res.status(404).json({
        message: "No progress found"
      });
    }

    const percentage = Math.round((progress.completed_tasks / progress.total_tasks) * 100);

    res.json({
      message: "Progress fetched successfully",
      progress: {
        completed_tasks: progress.completed_tasks,
        total_tasks: progress.total_tasks,
        percentage
      }
    });

  } catch (error) {
    next(error);
  }
};