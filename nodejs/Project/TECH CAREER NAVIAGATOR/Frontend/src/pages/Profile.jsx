import { useState } from "react";
import { profileAPI } from "../services/api";
import { useAuth } from "../contex/authcontex";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const [course, setCourse] = useState("");
  const [semester, setSemester] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const { user } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await profileAPI.create({
        user_id: user?.id || 1,
        course,
        semester,
      });
      setMessage({ type: "success", text: "Profile created successfully!" });
      setTimeout(() => navigate("/subjects"), 1500);
    } catch (error) {
      setMessage({
        type: "danger",
        text: error.response?.data?.message || "Error creating profile",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-4">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header bg-primary text-white">
              <i className="bi bi-person"></i> Student Profile
            </div>
            <div className="card-body">
              {message && (
                <div className={`alert alert-${message.type}`}>
                  {message.text}
                </div>
              )}

              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">Course</label>
                  <select
                    className="form-select"
                    value={course}
                    onChange={(e) => setCourse(e.target.value)}
                    required
                  >
                    <option value="">Select Course</option>
                    <option value="B.Tech">B.Tech</option>
                    <option value="BCA">BCA</option>
                    <option value="BSc Computer Science">
                      BSc Computer Science
                    </option>
                    <option value="MCA">MCA</option>
                    <option value="Diploma IT">Diploma in IT</option>
                  </select>
                </div>
                <div className="mb-3">
                  <label className="form-label">Current Semester</label>
                  <select
                    className="form-select"
                    value={semester}
                    onChange={(e) => setSemester(e.target.value)}
                    required
                  >
                    <option value="">Select Semester</option>
                    {[1, 2, 3, 4, 5, 6, 7, 8].map((num) => (
                      <option key={num} value={num}>
                        Semester {num}
                      </option>
                    ))}
                  </select>
                </div>
                <button
                  type="submit"
                  className="btn btn-primary"
                  disabled={loading}
                >
                  {loading ? "Creating Profile..." : "Save Profile & Continue"}
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
