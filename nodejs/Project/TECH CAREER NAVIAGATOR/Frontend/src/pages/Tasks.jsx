import { useEffect, useState } from "react";
import { taskAPI } from "../services/api";
import { useAuth } from "../contex/authcontex";
import { useNavigate } from "react-router-dom";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    loadTasks();
    loadProgress();
  }, []);

  const loadTasks = async () => {
    try {
      const res = await taskAPI.getAll(user?.id || 1);
      setTasks(res.data.tasks || []);
    } catch (error) {
      setMessage({
        type: "warning",
        text: "No tasks generated yet. Please complete the roadmap first.",
      });
    } finally {
      setLoading(false);
    }
  };

  const loadProgress = async () => {
    try {
      const res = await taskAPI.getProgress(user?.id || 1);
      setProgress(res.data.progress);
    } catch (error) {
      console.log("Error loading progress");
    }
  };

  const markComplete = async (taskId) => {
    try {
      const res = await taskAPI.complete({
        task_id: taskId,
        user_id: user?.id || 1,
      });

      setMessage({
        type: "success",
        text: `Task completed! Progress: ${res.data.progress.percentage}%`,
      });

      // Update local state
      setTasks(
        tasks.map((t) => (t.id === taskId ? { ...t, is_completed: true } : t)),
      );

      // Reload progress
      loadProgress();

      setTimeout(() => setMessage(""), 3000);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error marking task complete",
      });
    }
  };

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  const completedCount = tasks.filter((t) => t.is_completed).length;
  const progressPercentage =
    progress?.percentage ||
    (tasks.length > 0 ? Math.round((completedCount / tasks.length) * 100) : 0);

  return (
    <div className="container mt-4">
      <div className="row mb-4">
        <div className="col-md-12">
          <h2>
            <i className="bi bi-check2-square"></i> Your Daily Learning Journey
          </h2>
          <p className="text-muted">
            Complete daily tasks to master your chosen career path
          </p>
        </div>
      </div>

      {message && (
        <div className={`alert alert-${message.type}`}>{message.text}</div>
      )}

      {/* Progress Section */}
      {progress && (
        <div className="row mb-4">
          <div className="col-md-12">
            <div className="card bg-light">
              <div className="card-body">
                <h5 className="card-title">Overall Progress</h5>
                <div className="progress mb-3" style={{ height: "30px" }}>
                  <div
                    className="progress-bar bg-success"
                    role="progressbar"
                    style={{ width: `${progressPercentage}%` }}
                    aria-valuenow={progressPercentage}
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {progressPercentage}%
                  </div>
                </div>
                <p className="mb-0">
                  <strong>
                    {progress.completed_tasks} of {progress.total_tasks} tasks
                    completed
                  </strong>
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Tasks Section */}
      {tasks.length === 0 ? (
        <div className="alert alert-info">
          No tasks yet. <strong>Generate tasks from your roadmap first!</strong>
          <button
            className="btn btn-primary ms-2"
            onClick={() => navigate("/roadmap")}
          >
            Go to Roadmap
          </button>
        </div>
      ) : (
        <div className="row">
          <div className="col-md-12">
            {tasks.map((task, idx) => (
              <div key={task.id} className="card mb-3">
                <div className="card-body">
                  <div className="row align-items-center">
                    <div className="col-md-1">
                      <span className="badge bg-primary p-2">
                        Day {task.day_number}
                      </span>
                    </div>
                    <div className="col-md-8">
                      <h6
                        className={
                          task.is_completed
                            ? "text-decoration-line-through text-muted"
                            : ""
                        }
                      >
                        {task.task_description}
                      </h6>
                      {task.is_completed && (
                        <small className="text-success">
                          <i className="bi bi-check-circle"></i> Completed
                        </small>
                      )}
                    </div>
                    <div className="col-md-3 text-end">
                      <button
                        onClick={() => markComplete(task.id)}
                        disabled={task.is_completed}
                        className={`btn ${task.is_completed ? "btn-success" : "btn-outline-success"}`}
                      >
                        {task.is_completed ? (
                          <>
                            <i className="bi bi-check-circle"></i> Done
                          </>
                        ) : (
                          <>
                            <i className="bi bi-circle"></i> Mark Complete
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Action Buttons */}
      <div className="row mt-4 mb-4">
        <div className="col-md-12">
          <button
            className="btn btn-secondary me-2"
            onClick={() => navigate("/roadmap")}
          >
            <i className="bi bi-arrow-left"></i> Back to Roadmap
          </button>
          <button
            className="btn btn-info"
            onClick={() => {
              loadTasks();
              loadProgress();
            }}
          >
            <i className="bi bi-arrow-clockwise"></i> Refresh
          </button>
        </div>
      </div>
    </div>
  );
}
