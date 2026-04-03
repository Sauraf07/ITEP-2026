import { useEffect, useState } from "react";
import { careerAPI } from "../services/api";
import { useAuth } from "../contex/authcontex";
import { useNavigate } from "react-router-dom";

export default function Career() {
  const [careers, setCareers] = useState([]);
  const [selected, setSelected] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    loadCareers();
  }, []);

  const loadCareers = async () => {
    try {
      setLoading(true);
      const res = await careerAPI.getPaths();
      setCareers(res.data.careers || res.data);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error loading careers",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSelect = async (careerName) => {
    setSelected(careerName);
    try {
      await careerAPI.select({
        user_id: user?.id || 1,
        career_field: careerName,
      });
      setMessage({
        type: "success",
        text: `${careerName} selected successfully!`,
      });
      localStorage.setItem("selectedCareer", careerName);
      setTimeout(() => navigate("/roadmap"), 1500);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error selecting career",
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

  return (
    <div className="container mt-4">
      <div className="row mb-4">
        <div className="col-md-12">
          <h2>
            <i className="bi bi-briefcase"></i> Select Your IT Career Path
          </h2>
          <p className="text-muted">
            Choose your desired career to get personalized roadmap and daily
            tasks
          </p>
        </div>
      </div>

      {message && (
        <div className={`alert alert-${message.type}`}>{message.text}</div>
      )}

      <div className="row">
        {careers.map((career, idx) => (
          <div className="col-md-6 mb-4" key={idx}>
            <div
              className={`card h-100 cursor-pointer transition ${selected === career.career_field ? "border-success border-3 shadow-lg" : "border-light"}`}
              onClick={() => handleSelect(career.career_field)}
              style={{ cursor: "pointer", transition: "all 0.3s" }}
            >
              <div className="card-body">
                <h5 className="card-title mb-2">
                  <i className="bi bi-star-fill text-warning"></i>{" "}
                  {career.career_field}
                </h5>
                <p className="card-text">{career.description}</p>
                <button
                  className={`btn ${selected === career.career_field ? "btn-success" : "btn-outline-primary"} w-100 mt-2`}
                  onClick={(e) => {
                    e.preventDefault();
                    handleSelect(career.career_field);
                  }}
                >
                  {selected === career.career_field
                    ? "✓ Selected"
                    : "Select This Path"}
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="row mt-4">
        <div className="col-md-12">
          <button
            className="btn btn-secondary me-2"
            onClick={() => navigate("/subjects")}
          >
            <i className="bi bi-arrow-left"></i> Back
          </button>
          {selected && (
            <button
              className="btn btn-success"
              onClick={() => navigate("/roadmap")}
            >
              <i className="bi bi-arrow-right"></i> View Roadmap
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
