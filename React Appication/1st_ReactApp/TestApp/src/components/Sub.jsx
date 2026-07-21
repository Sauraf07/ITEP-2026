import { useRef, useState } from "react"

function Sub(){
    let num1 = useRef(0)
    let num2 = useRef(0)
    const [result, setResult] = useState(0);
    const sub = () => {
        let n1 = num1.current.value*1
        let n2 = num2.current.value*1
        setResult(n1 - n2)
    }

    return <>
        <hr />
        <h1>Subtraction of Two Numbers | Using useRef </h1>
        <input ref={num1} placeholder="Enter 1st number" />
        <input ref={num2} placeholder="Enter 2nd number" />
        <button onClick={sub}>Sub</button>
        <h2>Result: {result}</h2>
        <hr />
    </>

}
export default Sub;