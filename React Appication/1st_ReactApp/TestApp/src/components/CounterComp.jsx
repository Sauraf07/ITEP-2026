import { useReducer } from "react";

function CounterComp() {
    const [state,dispatch] = useReducer((state,action) => {
        if(action.type === "increment-even"){
            state.evenCounter = state.evenCounter + 2
        }
        else if(action.type === "decrement-even"){
            state.evenCounter = state.evenCounter - 2
        }
        else if(action.type === "increment-odd"){
            state.oddCounter = state.oddCounter + 2
        }
        else if(action.type === "decrement-odd"){
            state.oddCounter = state.oddCounter - 2
        }
        return {...state}
    }, {evenCounter: 0, oddCounter: 1});

    return <>
    <hr />
    <h1>Counter Component </h1>
    <center>
        <h1>Even Counter  Component...</h1>
        <h2>Even Counter: {state.evenCounter}</h2>
        <button onClick={()=>{dispatch({type: "increment-even"})}}>Increment Even Counter</button>
        <button onClick={()=>{dispatch({type: "decrement-even"})}}>Decrement Even Counter</button>
    </center>
    <center>
        <h1>Odd Counter  Component...</h1>
        <h2>Odd Counter: {state.oddCounter}</h2>
        <button onClick={()=>{dispatch({type: "increment-odd"})}}>Increment Odd Counter</button>
        <button onClick={()=>{dispatch({type: "decrement-odd"})}}>Decrement Odd Counter</button>
    </center>
    <hr />
    </>
}    
export default CounterComp;