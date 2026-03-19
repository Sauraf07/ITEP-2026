import { useState } from "react";
import First from "./components/First";
import IncrementCounter from "./components/counter";


function App(){
  const [counter,setCounter] = useState(100);
  let m1 = "Good Morning.."
  let studentNameList = [
    "Saurav",
    "Shiv",
    "gauarv"
  ]
  return <>
     <h1>App component....</h1>
     <h2>Counter : {counter}</h2>
     <hr/>
     <First dataMessage={m1} studentNameList={studentNameList}/>
     <IncrementCounter setCounter={setCounter} counter={counter}/>
  </>
}
export default App;