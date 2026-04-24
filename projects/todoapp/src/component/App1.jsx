import {useRef,useState} from "react"
import todoData from "../todoData"


function App(){
const[taskList,setTaskList] =  useState(todoData);


const[priorityList,setPriority] =   useState([

   { "priorityId":1, "priorityValue":"High" },
   {"priorityId":2,"priorityValue":"Normal"},
   {"priorityId":3,"priorityValue":"Low"},

])

let titleRef = useRef(null)
let priorityRef = useRef(null)

const addtask =() => {
 let title = titleRef.current.value;
 let pid = priorityRef.current.value;
let date = new Data();
date = date.getdate()+ "/" + date.getmonth()+"/" + date.getFullyear();
let status="active";
let newList = {title,pid,date,status};
setTaskList ([...taskList,newList])
}

const [statusFilter,setstatusFilter] = useState("active");
const changeStatus =(task,newStatus) => {
let index= taskList.findIndex((obj)=> {return obj.title == task.title })
taskList.splice(index,1);
 task.status= newStatus;
 taskList.splice(index,0,task);
 setTaskList([... taskList]);

}

return <>
    <div className="bg-info text-center">
        <span className=" text-white">Todo List</span>
    </div>

    <div className = "container">
        <div className="row">
            <div className="col-md-6 mt-4 mb-4">
                <input ref={titleRef} className="form-control  "  type="text" placeholder="Enter the Task"></input>
                
            </div>
            <div className="col-md-6 mt-4 mb-4">
                <select ref={priorityRef} className="form-control">
                    <option>Select the Priority</option>
                    {priorityList.map((priority,index) => {return<option value={priority.priorityId}>{priority.priorityValue}</option>})}
                </select>
            </div>
        </div>
       <div></div>

    </div>
</>









}
export default App;
