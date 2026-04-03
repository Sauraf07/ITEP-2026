import { useEffect, useState } from "react";
import { useAuth } from "../contex/authcontex";
import { taskAPI, seedAPI } from "../services/api";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [stats, setStats] = useState({ total: 0, completed: 0 });
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const { token, user } = useAuth();

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const tasksRes = await taskAPI.getAll(user?.id || 1);
      const tasksList = tasksRes.data.tasks || [];
      setTasks(tasksList.slice(0, 5));

      const total = tasksList.length;
      const completed = tasksList.filter((t) => t.is_completed).length;
      setStats({ total, completed });
    } catch (error) {
      console.log("No tasks yet");
    }
  };

  const handleSeedData = async () => {
    try {
      setLoading(true);
      const res = await seedAPI.seedAll();
      setMessage({
        type: "success",
        text: `✓ Data seeded successfully! ${res.data.careers} careers and ${res.data.roadmapSteps} roadmap steps created.`,
      });
    } catch (error) {
      if (error.response?.data?.message?.includes("already seeded")) {
        setMessage({
          type: "info",
          text: "✓ Data already seeded. Ready to use!",
        });
      } else {
        setMessage({
          type: "danger",
          text: error.response?.data?.message || "Error seeding data",
        });
      }
    } finally {
      setLoading(false);
    }
  };

  const progress = stats.total > 0 ? (stats.completed / stats.total) * 100 : 0;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">
        <i className="bi bi-speedometer2"></i> Dashboard - Welcome {user?.name}
      </h2>

      {message && (
        <div
          className={`alert alert-${message.type} alert-dismissible fade show`}
          role="alert"
        >
          {message.text}
          <button
            type="button"
            className="btn-close"
            onClick={() => setMessage("")}
          ></button>
        </div>
      )}

      {/* Setup Alert */}
      <div className="alert alert-warning" role="alert">
        <h4 className="alert-heading">
          <i className="bi bi-info-circle"></i> First Time Setup
        </h4>
        <p>
          Click the button below to load IT industry data (careers, subjects,
          and roadmaps):
        </p>
        <button
          className="btn btn-warning"
          onClick={handleSeedData}
          disabled={loading}
        >
          {loading ? "Loading Data..." : "Load IT Industry Data"}
        </button>
      </div>

      <div className="row">
        <div className="col-md-8">
          <div className="card mb-4">
            <div className="card-header bg-primary text-white">
              <i className="bi bi-list-task"></i> Recent Tasks
            </div>
            <div className="card-body">
              {tasks.length === 0 ? (
                <div className="text-center py-4">
                  <p className="text-muted">
                    No tasks yet. Start your journey!
                  </p>
                  <Link to="/profile" className="btn btn-primary">
                    Create Profile & Start
                  </Link>
                </div>
              ) : (
                <ul className="list-group">
                  {tasks.map((task) => (
                    <li
                      key={task.id}
                      className="list-group-item d-flex justify-content-between align-items-center"
                    >
                      <span
                        className={
                          task.is_completed
                            ? "text-decoration-line-through text-muted"
                            : ""
                        }
                      >
                        Day {task.day_number}: {task.task_description}
                      </span>
                      <span
                        className={`badge ${task.is_completed ? "bg-success" : "bg-warning"}`}
                      >
                        {task.is_completed ? "Completed" : "Pending"}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card mb-4">
            <div className="card-header bg-success text-white">
              <i className="bi bi-graph-up"></i> Progress
            </div>
            <div className="card-body">
              <h5 className="card-title">Task Completion</h5>
              <div className="progress mb-3" style={{ height: "25px" }}>
                <div
                  className="progress-bar progress-bar-striped progress-bar-animated"
                  role="progressbar"
                  style={{ width: `${progress}%` }}
                >
                  {progress.toFixed(0)}%
                </div>
              </div>
              <p className="mb-0">
                <strong>{stats.completed}</strong> of{" "}
                <strong>{stats.total}</strong> tasks completed
              </p>
            </div>
          </div>

          <div className="card">
            <div className="card-body">
              <h6 className="card-title">Quick Actions</h6>
              <div className="d-grid gap-2">
                <Link to="/profile" className="btn btn-outline-primary btn-sm">
                  <i className="bi bi-person"></i> Create/Update Profile
                </Link>
                <Link to="/subjects" className="btn btn-outline-info btn-sm">
                  <i className="bi bi-book"></i> Select Subjects
                </Link>
                <Link to="/career" className="btn btn-outline-success btn-sm">
                  <i className="bi bi-briefcase"></i> Choose Career
                </Link>
                <Link to="/tasks" className="btn btn-outline-warning btn-sm">
                  <i className="bi bi-check-square"></i> View Tasks
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Getting Started Guide */}
      <div className="card mt-4">
        <div className="card-header bg-info text-white">
          <i className="bi bi-question-circle"></i> Getting Started
        </div>
        <div className="card-body">
          <ol>
            <li>
              Click <strong>"Load IT Industry Data"</strong> to initialize the
              system
            </li>
            <li>
              Go to <strong>Profile</strong> and enter your course & semester
            </li>
            <li>
              Select <strong>Important IT Subjects</strong> you want to focus on
            </li>
            <li>
              Choose your desired <strong>IT Career Path</strong>
            </li>
            <li>
              View your <strong>Personalized Roadmap</strong>
            </li>
            <li>
              Generate <strong>Daily Tasks</strong> and track progress
            </li>
          </ol>
        </div>
      </div>
    </div>
  );
}
