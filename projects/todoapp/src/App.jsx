import {useRef , useState } from "react";
import todoData from "./todoData.js"
function App(){
  const [taskList, setTaskList] = useState(todoData);

  const [priorityList, setPriority] = useState([
    { "priorityId":1, "priorityValue": "High" },
    { "priorityId":2, "priorityValue": "Normal" },
    { "priorityId":3, "priorityValue": "Low" }
  ])

  let titleRef=useRef(null);
  let priorityRef=useRef(null);
  const addTask=()=>{
    let title=titleRef.current.value;
    let pid=priorityRef.current.value;
    let date= new Date();
    date=date.getDate()+"/"+date.getMonth()+"/"+date.getFullYear();
    let status="active";
    let newList={title,pid,date,status};
    setTaskList([...taskList,newList])
  }

   const [statusFilter,setStatusFilter] = useState("active");
    const changeStatus = (task,newStatus)=>{
    let index =  taskList.findIndex((obj)=>{return obj.title == task.title});
    taskList.splice(index,1);
    task.status = newStatus;
    taskList.splice(index,0,task);
    setTaskList([...taskList]);
  }

  return <>
    <div className="bg-info text-center">
      <span className=" text-white">TO DO APP</span>
    </div>
    <div className="container">
      <div className="row">
        <div className="col-md-6 mt-4 mb-4">
          <input ref={titleRef} className="form-control" type="text" placeholder="Enter Task Title" />
        </div>
        <div className="col-md-6 mt-4 mb-4">
          <select ref={priorityRef} className="form-control">
            <option>Select priority</option>
            {priorityList.map((priority, index) => { return <option value={priority.priorityId}>{priority.priorityValue}</option> })}
          </select>
        </div>
      </div>
      <button onClick={addTask} className="btn btn-success mb-4">Add</button>
    </div>

      <div className="row">
        <div className="col-md-6 mb-4">
          <button disabled={statusFilter=="active" ? true: false} onClick={()=>setStatusFilter("active")} className="btn btn-primary ml-4 mr-2">Active</button>
          <button disabled={statusFilter=="deactive" ? true : false} onClick={()=>setStatusFilter("deactive")} className="btn btn-danger">Deactive</button>
        </div>
      </div>


    <table className="table table-striped">
      <thead>
        <tr>
          <th>Sr no.</th>
          <th>Task Title</th>
          <th>Date</th>
          <th>Priority</th>
          <th>Status</th>
        </tr>
        {taskList.filter((task)=>{return task.status == statusFilter}).sort((a,b)=>{return a.pid-b.pid}).map((task, index) => {

          return <tr className={task.pid==1? "bg-danger" : task.pid==2 ? "bg-info" : "bg-warning"}key={index}>
            <td>{index + 1}</td>
            <td>{task.title}</td>
            <td>{task.date}</td>
            <td> {priorityList.find((pObj)=>{return pObj.priorityId==task.pid}).priorityValue}</td>
            <td>
              {task.status=="active" ? <button className="btn btn-outline-secondary" onClick={()=>{changeStatus(task,"deactive")}}>Deactive</button> : <button onClick={()=>{changeStatus(task,"active")}} className="btn btn-outline-secondary">Active</button>}
            </td>
          </tr>
        })}
      </thead>
    </table>

  </>

}

export default App;