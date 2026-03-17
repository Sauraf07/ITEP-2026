import { useRef, useState } from 'react'
import tododata from './tododata'
import './App.css'

function App() {
  const [tasklist, settaskList] = useState(tododata);
  const [prioritylist,setprioritylist] = useState([
    {"priorityId":1, "priorityValue":"low"},
    {"priorityId":2, "priorityValue":"Medium"},
    {"priorityId":3, "priorityValue":"High"}

  ])
  const [statusFilter,setstatusFilter] = useState("active");
  
  let titleref = useRef(null);
  let priorityref = useRef(null);

  const addtask = ()=>{
    let title = titleref.current.value;
    let pid = priorityref.current.value;
    let date = new Date();
    date = date.getDate()+"/"(date.getMonth()-1)+"/"(date.getFullYear());
    let status = "active";
    let newtask = [title,pid,date,status];
    settaskList([...tasklist,newtask])
  }
  const changestatus = (task,newstatus)=>{
    let index = tasklist.findIndex((obj)=>{return obj.title==task.title});
    tasklist.splice(index,1);
    task.status = newstatus;
    tasklist.splice(index,0,task);
    settaskList([...tasklist]);
  }

  return (
    <>
      <div className='bg-danger p-2 text-center'>
          <span className='text-white'>TODO APP</span>
        </div>
        <div className='conatiner mt-3 mb-3'>
          <div className='row'>
            <div className='col-md-6'>
              <input  ref={titleref} className='form-control' placeholder='Enter Task Title' />
            </div>
            <div className='col-md-6'>
              <select ref={priorityref} className='form-control'>
                <option >Select Proprity</option>
                {prioritylist.map((pObj,index)=>{return <option key={pObj.priorityId} value={pObj.priorityId}>{pObj.priorityValue}</option>})}
                </select>
            </div>

          </div>
          <div className='row mt-2'>
            <div className='col-md-6'>
              <button onClick={addtask} className='btn btn-success'>ADD</button>
            </div>
          </div>
        </div>
        <div className='container mt-3'>
          <div className='mt-2 mb-2'>
            <button disabled={statusFilter=="active"? true:false} onClick={()=>setstatusFilter("active")} className='btn btn-success'>Active({tasklist.filter((task)=>{return task.status=="active"}).length})</button>
            <button disabled={statusFilter=="deactive" ? true : false} onClick={()=>setstatusFilter("deactive")} className="btn btn-danger ml-2">Deactive({tasklist.filter((task)=>{return task.status=="deactive"}).length})</button>
          </div>
          <table className='table table-striped'>
            <thead>
              <tr>
                <th>S.no</th>
                <th>Title</th>
                <th>Date</th>
                <th>Priority</th>
                <th>Change status</th>
              </tr>

            </thead>
            <tbody>
          {tasklist.filter((task)=>{return task.status == statusFilter}).sort((a,b)=>{return b.pid-a.pid}).map((task,index)=>{return <tr className={task.pid==1? "bg-success" : task.pid==2 ? "bg-warning" : "bg-danger"} key={index}>
            <td>{index+1}</td>
            <td>{task.title}</td>
            <td>{task.date}</td>
            <td>{prioritylist.find((pObj)=>{return pObj.priorityId == task.pid}).priorityValue}</td>
            <td>
              {task.status=="active" ? <button className="btn btn-outline-secondary" onClick={()=>{changestatus(task,"deactive")}}>Deactive</button> : <button onClick={()=>{changestatus(task,"active")}} className="btn btn-outline-secondary">Active</button>}
            </td>
          </tr>})}
        </tbody>
          </table>
        </div>
    </>
  )
}

export default App;
