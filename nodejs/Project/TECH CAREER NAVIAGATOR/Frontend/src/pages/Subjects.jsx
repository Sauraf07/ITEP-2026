import { useState, useEffect } from "react";
import { subjectAPI } from "../services/api";
import { useAuth } from "../contex/authcontex";
import { useNavigate } from "react-router-dom";

export default function Subjects() {
  const [subjects, setSubjects] = useState([]);
  const [selectedSubjects, setSelectedSubjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchSubjects();
  }, []);

  const fetchSubjects = async () => {
    try {
      setLoading(true);
      const res = await subjectAPI.getImportantList();
      setSubjects(res.data.subjects || []);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error fetching subjects",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSelectSubject = (subjectId) => {
    setSelectedSubjects((prev) =>
      prev.includes(subjectId)
        ? prev.filter((id) => id !== subjectId)
        : [...prev, subjectId],
    );
  };

  const handleAddSubjects = async () => {
    if (selectedSubjects.length === 0) {
      setMessage({
        type: "warning",
        text: "Please select at least one subject",
      });
      return;
    }

    try {
      setLoading(true);
      // Add each selected subject
      for (const subjectId of selectedSubjects) {
        const subject = subjects.find((s) => s.id === subjectId);
        if (subject) {
          await subjectAPI.add({
            user_id: user?.id || 1,
            subject_name: subject.name,
          });
        }
      }

      setMessage({
        type: "success",
        text: `Added ${selectedSubjects.length} subjects successfully!`,
      });

      // Save selected subjects to localStorage
      localStorage.setItem(
        "selectedSubjects",
        JSON.stringify(selectedSubjects),
      );

      setTimeout(() => navigate("/career"), 1500);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error adding subjects",
      });
    } finally {
      setLoading(false);
    }
  };

  if (loading && subjects.length === 0) {
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
      <div className="row">
        <div className="col-md-12">
          <div className="card">
            <div className="card-header bg-info text-white">
              <i className="bi bi-book"></i> Select Important IT Subjects
              <span className="float-end">
                Selected: {selectedSubjects.length}
              </span>
            </div>
            <div className="card-body">
              {message && (
                <div className={`alert alert-${message.type}`}>
                  {message.text}
                </div>
              )}

              <div className="row">
                {subjects.map((subject) => (
                  <div key={subject.id} className="col-md-6 mb-3">
                    <div className="form-check">
                      <input
                        className="form-check-input"
                        type="checkbox"
                        id={`subject${subject.id}`}
                        checked={selectedSubjects.includes(subject.id)}
                        onChange={() => handleSelectSubject(subject.id)}
                      />
                      <label
                        className="form-check-label"
                        htmlFor={`subject${subject.id}`}
                      >
                        <strong>{subject.name}</strong>
                        <br />
                        <small className="text-muted">
                          Importance: {"⭐".repeat(subject.importance)}
                        </small>
                      </label>
                    </div>
                  </div>
                ))}
              </div>

              <div className="mt-4">
                <button
                  className="btn btn-primary me-2"
                  onClick={handleAddSubjects}
                  disabled={loading || selectedSubjects.length === 0}
                >
                  {loading
                    ? "Adding Subjects..."
                    : "Continue to Career Selection"}
                </button>
                <button
                  className="btn btn-secondary"
                  onClick={() => navigate("/profile")}
                >
                  Back
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
