import { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import stuData from "./data.js";

class App extends Component {
  constructor() {
    super();
    this.state = {
      studentList: stuData,
      branchList: ["CS", "IT", "CV", "MECH"],
      branchAll:"All"
    }
  }
  studentAdd=()=>{
    let roll=document.getElementById("rollInput").value;
    let name=document.getElementById("nameInput").value;
    let branch=document.getElementById("branchInput").value;
    let gender=document.getElementById("genderInput").value;
    let newStudent={roll,name,branch,gender};
    this.setState({studentList:[...this.state.studentList,newStudent]});
  }
  studentRemove=(index)=>{
    let newList = this.state.studentList.filter((student,i)=>{return i!==index});
    this.setState({studentList:newList});
    
  }

  rollCheck=()=>{
    console.log("input lost focus")
  }
  render() {
    return <>
      <div className="bg-danger">
        <h4 className=" text-center text-white">Student App</h4>
      </div>
      <div className="container">
        <div className="row">
          <div className="col-md-6 mt-3">
            <input id="rollInput" type="text" placeholder="Enter student roll number" className="form-control" />
          </div>
          <div className="col-md-6 mt-3">
            <input id="nameInput" type="text" placeholder="Enter student name" className="form-control" />
          </div>
        </div>
      </div>
      <div className="container">
        <div className="row">
          <div className="col-md-6 mt-4 mb-2">
            <select id="branchInput" className="form-control">
              <option>Select branch</option>
              {this.state.branchList.map((branch, index) => { return <option key={branch}>{branch}</option> })}
            </select>
          </div>
          <div className="col-md-6 mt-4 mb-2">
            <select id="genderInput" className="form-control">
              <option>Select gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
        </div>
        <div className="row">
          <div className="col-md-6 mb-5">
            <button className="btn btn-success" onClick={this.studentAdd}>Add</button>
          </div>
          <div className="col-md-6 mb-5">
            <button onClick={()=>{this.setState({branchAll:"CS"})}} className="ms-2 btn btn-danger">CS({this.state.studentList.filter((student)=>{return student.branch=="CS"}).length})</button>
            <button onClick={()=>{this.setState({branchAll:"IT"})}} className="ms-2 btn btn-info">IT({this.state.studentList.filter((student)=>{return student.branch=="IT"}).length})</button>
            <button onClick={()=>{this.setState({branchAll:"CV"})}} className="ms-2 btn btn-primary">CV({this.state.studentList.filter((student)=>{return student.branch=="CV"}).length})</button>
            <button onClick={()=>{this.setState({branchAll:"MECH"})}} className="ms-2 btn btn-secondary">MECH({this.state.studentList.filter((student)=>{return student.branch=="MECH"}).length})</button>
            <button onClick={()=>{this.setState({branchAll:"All"})}} className="btn btn-success ms-2">Total({this.state.studentList.length})</button>
          </div>
        </div>
      </div>


      <table className="table table-striped">
        <thead >
          <tr>
            <th>SrNo</th>
            <th>Roll No</th>
            <th>Name</th>
            <th>Gender</th>
            <th>Branch</th>
            <th>Remove</th>
          </tr>
        </thead>
        <tbody>
          {this.state.studentList.map((student, index) => {
            return <tr key={index}>
              <td>{index + 1}</td>
              <td>{student.roll}</td>
              <td>{student.name}</td>
              <td>{student.gender}</td>
              <td>{student.branch}</td>
              <td>
                <button className="btn btn-outline-danger" onClick={()=>{{this.studentRemove(index)}}}>Remove</button>
              </td>
            </tr>
          })}
        </tbody>
      </table>
    </>
  }
}
export default App;