import { useState } from "react";

function Multi() {
    const [result, setResult] = useState(0);
    const [firstNum, setFirstNum] = useState(0);
    const [secondNum, setSecondNum] = useState(0);
    const multi = () => {
        setResult(firstNum * secondNum)
    }
    return<>
    <hr />
    <h1>Multiplication of Two Numbers | Using State </h1>
    <input  value={firstNum} onChange={(e)=>{setFirstNum(e.target.value)}} placeholder="Enter 1st number" />
    <input  value={secondNum} onChange={(e)=>{setSecondNum(e.target.value)}} placeholder="Enter 2nd number" />
    <button onClick={multi}>Multiply</button>
    <h2>Result: {result}</h2>
    <hr />
    
    </>
}
export default Multi;