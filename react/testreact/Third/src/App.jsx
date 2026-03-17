import React, { useState, useRef } from "react";
import StudentArray from "./data";

function App() {
  const [studentList, setStudentList] = useState(StudentArray);
  const [branchList] = useState(["CS", "IT", "CV", "MECH"]);
  const [branchFilter, setBranchFilter] = useState("ALL");

  const rollInput = useRef();
  const nameInput = useRef();
  const branchInput = useRef()
  const genderInput = useRef()

  const addStudent = () => {
    const roll = rollInput.current.value.trim();
    const name = nameInput.current.value.trim()
    const branch= branchInput.current.value;
    const gender = genderInput.current.value

    
    if (!roll || !name || branch === "Select Branch" || gender === "Select Gender") {
      alert("Please fill all fields");
      return;
    }
    const rollExists = studentList.some((student) => student.roll === roll);

    if (rollExists) {
      alert("Student with this roll number already exists");
      return;
    }

    const newStudent = { roll, name, branch, gender };

    setStudentList([...studentList, newStudent])

  
    rollInput.current.value = "";
    nameInput.current.value = ""
    branchInput.current.value = "Select Branch";
    genderInput.current.value = "Select Gender";
  };

  return (
    <>
      <div className="bg-danger p-1">
        <h5 className="text-white text-center">Student App</h5>
      </div>

      <div className="container mt-3 mb-3">
        <div className="row">
          <div className="col-md-6">
            <input
              ref={rollInput}
              type="text"
              placeholder="Enter Student Roll Number"
              className="form-control"
            />
          </div>

          <div className="col-md-6">
            <input
              ref={nameInput}
              type="text"
              placeholder="Enter Student Name"
              className="form-control"
            />
          </div>
        </div>

        <div className="row mt-2">
          <div className="col-md-6">
            <select ref={branchInput} className="form-control">
              <option>Select Branch</option>
              {branchList.map((branch) => (
                <option key={branch}>{branch}</option>
              ))}
            </select>
          </div>

          <div className="col-md-6">
            <select ref={genderInput} className="form-control">
              <option>Select Gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
        </div>

        <div className="row mt-2">
          <div className="col-md-6">
            <button onClick={addStudent} className="btn btn-success">
              ADD
            </button>
          </div>

          <div className="col-md-6">
            <button onClick={() => setBranchFilter("CS")} className="ml-2 btn btn-info">
              CS ({studentList.filter((s) => s.branch === "CS").length})
            </button>

            <button onClick={() => setBranchFilter("IT")} className="ml-2 btn btn-danger">
              IT ({studentList.filter((s) => s.branch === "IT").length})
            </button>

            <button onClick={() => setBranchFilter("CV")} className="ml-2 btn btn-primary">
              CV ({studentList.filter((s) => s.branch === "CV").length})
            </button>

            <button onClick={() => setBranchFilter("MECH")} className="ml-2 btn btn-warning">
              MECH ({studentList.filter((s) => s.branch === "MECH").length})
            </button>

            <button onClick={() => setBranchFilter("ALL")} className="ml-2 btn btn-secondary">
              TOTAL ({studentList.length})
            </button>
          </div>
        </div>
      </div>

      <table className="table table-striped">
        <thead>
          <tr>
            <th>S.No</th>
            <th>Roll Number</th>
            <th>Name</th>
            <th>Gender</th>
            <th>Branch</th>
            <th>Remove</th>
          </tr>
        </thead>

        <tbody>
          {studentList
            .filter(
              (student) =>
                branchFilter === "ALL" || student.branch === branchFilter
            )
            .map((student, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{student.roll}</td>
                <td>{student.name}</td>
                <td>{student.gender}</td>
                <td>{student.branch}</td>
                <td>
                  <button className="btn btn-outline-danger">Remove</button>
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </>
  );
}

export default App;