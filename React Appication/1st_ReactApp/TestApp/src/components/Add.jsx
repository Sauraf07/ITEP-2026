import { useState } from "react";

function ADD(){
    const [result, setResult] = useState(0);
    const add = () => {
        let num1 = document.getElementById("num1").value;
        let num2 = document.getElementById("num2").value;
        
        num1 = num1 *1
        num2 = num2 *1
        setResult(num1 + num2)
    }
    return <>   
    <hr />
    <h1>Addition of Two Numbers | Using ID </h1>
    <input  id="num1" placeholder="Enter 1st number" />
    <input  id="num2" placeholder="Enter 2nd number" />
    <button onClick={add}>Add</button>
    <h2>Result: {result}</h2>
    <hr />
    </>

}
export default ADD;