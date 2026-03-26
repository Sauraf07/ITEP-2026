import DailyTask from "../models/dailytask.model.js";
import Progress from "../models/Progress.model.js";

export const generateTasks = async (req, res, next) => {
  try {
    const { user_id, tasks } = req.body;

    if (!user_id || !tasks || !Array.isArray(tasks) || tasks.length === 0) {
      return res.status(400).json({
        message: "Please provide user_id and a tasks array"
      });
    }

    const createdTasks = [];
    let day = 1;

    for (let task of tasks) {
      const newTask = await DailyTask.create({
        user_id,
        task_description: task,  // ✅ BUG FIX 7: "task" galat field naam tha — model mein "task_description" hai
        day_number: day
      });
      createdTasks.push(newTask);
      day++;
    }

    // ✅ BUG FIX 8: Progress track karo jab tasks generate hon
    //    Pehle: Progress table bilkul use hi nahi ho raha tha
    const existingProgress = await Progress.findOne({ where: { user_id } });

    if (existingProgress) {
      existingProgress.total_tasks += createdTasks.length;
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

    // ✅ BUG FIX 9: Koi null check nahi tha
    //    Agar task_id galat ho toh "Cannot set property of null" crash aata tha
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

    // ✅ BUG FIX 10: Progress update nahi ho raha tha task complete karne ke baad
    //    Ab completed_tasks count +1 hoga
    const progress = await Progress.findOne({ where: { user_id: task.user_id } });

    if (progress) {
      progress.completed_tasks += 1;
      await progress.save();
    }

    // Progress percentage calculate karo
    const percentage = progress
      ? Math.round((progress.completed_tasks / progress.total_tasks) * 100)
      : 0;

    res.json({
      message: "Task marked as completed",
      task_id,
      progress: {
        completed: progress?.completed_tasks || 1,
        total: progress?.total_tasks || 1,
        percentage: `${percentage}%`
      }
    });

  } catch (error) {
    next(error);
  }
};

// ✅ NEW: Progress dekho — pehle ye tha hi nahi
export const getProgress = async (req, res, next) => {
  try {
    const { userId } = req.params;

    const progress = await Progress.findOne({
      where: { user_id: userId }
    });

    if (!progress) {
      return res.status(404).json({
        message: "No progress found. Generate tasks first."
      });
    }

    const percentage = Math.round(
      (progress.completed_tasks / progress.total_tasks) * 100
    );

    res.json({
      message: "Progress fetched successfully",
      user_id: userId,
      completed_tasks: progress.completed_tasks,
      total_tasks: progress.total_tasks,
      percentage: `${percentage}%`
    });

  } catch (error) {
    next(error);
  }
};