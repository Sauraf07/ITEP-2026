import { useEffect, useState } from "react";
import { roadmapAPI, taskAPI } from "../services/api";
import { useAuth } from "../contex/authcontex";
import { useNavigate } from "react-router-dom";

export default function Roadmap() {
  const [roadmap, setRoadmap] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");
  const [generatingTasks, setGeneratingTasks] = useState(false);
  const { user } = useAuth();
  const navigate = useNavigate();
  const selectedCareer = localStorage.getItem("selectedCareer");

  useEffect(() => {
    if (!selectedCareer) {
      navigate("/career");
      return;
    }
    loadRoadmap();
  }, [selectedCareer]);

  const loadRoadmap = async () => {
    try {
      setLoading(true);
      const res = await roadmapAPI.getByCareer(selectedCareer);
      setRoadmap(res.data.roadmap || []);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error loading roadmap",
      });
    } finally {
      setLoading(false);
    }
  };

  const generateTasks = async () => {
    try {
      setGeneratingTasks(true);
      setMessage("");

      // Auto-generate tasks
      await taskAPI.generate({
        user_id: user?.id || 1,
      });

      setMessage({
        type: "success",
        text: "Daily tasks generated successfully!",
      });

      localStorage.setItem("tasksGenerated", "true");
      setTimeout(() => navigate("/tasks"), 1500);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error generating tasks",
      });
    } finally {
      setGeneratingTasks(false);
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

  return (
    <div className="container mt-4">
      <div className="row mb-4">
        <div className="col-md-12">
          <h2>
            <i className="bi bi-map"></i> Career Roadmap for {selectedCareer}
          </h2>
          <p className="text-muted">
            Follow this roadmap to master the required skills
          </p>
        </div>
      </div>

      {message && (
        <div className={`alert alert-${message.type}`}>{message.text}</div>
      )}

      {roadmap.length === 0 ? (
        <div className="alert alert-info">
          No roadmap available for this career. Please select another career.
        </div>
      ) : (
        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="card-body">
                <div className="timeline">
                  {roadmap.map((step, idx) => (
                    <div
                      key={step.id}
                      className="timeline-item mb-4 pb-4"
                      style={{
                        borderLeft: "3px solid #007bff",
                        paddingLeft: "20px",
                      }}
                    >
                      <div
                        className="timeline-marker"
                        style={{
                          width: "20px",
                          height: "20px",
                          backgroundColor: "#007bff",
                          borderRadius: "50%",
                          marginLeft: "-32px",
                          marginTop: "5px",
                        }}
                      ></div>
                      <h5 className="mt-2">
                        Step {step.step_number}: {step.step_title}
                      </h5>
                      <p className="text-muted">{step.description}</p>
                      {step.resources && (
                        <small className="text-secondary">
                          Resources:{" "}
                          {Array.isArray(step.resources)
                            ? step.resources.join(", ")
                            : "N/A"}
                        </small>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      <div className="row mt-4">
        <div className="col-md-12">
          <button
            className="btn btn-secondary me-2"
            onClick={() => navigate("/career")}
          >
            <i className="bi bi-arrow-left"></i> Back
          </button>
          {roadmap.length > 0 && (
            <button
              onClick={generateTasks}
              className="btn btn-success"
              disabled={generatingTasks}
            >
              <i className="bi bi-plus-circle"></i>{" "}
              {generatingTasks ? "Generating..." : "Generate Daily Tasks"}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
