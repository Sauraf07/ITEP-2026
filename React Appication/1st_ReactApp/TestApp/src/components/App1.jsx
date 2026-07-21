import { useState } from "react";
import Header from "./components/Header";
import data from "./data";

function App1() {
  const [counter, setCounter] = useState(0);
  const incremenrtCounter = () => {
    setCounter(counter + 1);
  };
  const decrementCounter = () => {
    setCounter(counter - 1);
  };
  const [students, setStudents] = useState(data)

  const deleteStudent = (id) => {
    if (window.confirm("Are you sure to delete this student?")) {
    let newStudents = students.findIndex((student) => {return student.id === id})
    students.splice(newStudents, 1)
    setStudents([...students])

    };
   
  }
  return <>
  <h1>App Component.....</h1>
    <Header />
    <h2>Counter: {counter}</h2>
    <button onClick={incremenrtCounter}>Increment</button>
    <button onClick={decrementCounter}>Decrement</button>

    <hr />
    <hr />
    <table border={1} cellPadding={10} cellSpacing={0}>
     <tr>
        <td>Id</td>
        <td>Name</td>
        <td>Roll</td>
        <td>Percentage</td>
        <td>Course</td>
        <td>Delete</td>
     </tr>
     {students.map((students,index) =>{return<tr key={index}>
        <td>{students.id}</td>
        <td>{students.name}</td>
        <td>{students.roll}</td>
        <td>{students.per}</td>
        <td>{students.course}</td>
        <td><button onClick={()=>{deleteStudent(students.id)}}>Delete</button></td>
     </tr>})}

    
    </table>



  </>
}

export default App1;