import { useSelector, useDispatch } from "react-redux";
import { increment, incevenCounter, incoddCounter } from "./redux-config/counter";


import React from 'react';

const App = () => {
  const {count, evenCounter, oddCounter} = useSelector((state) => state.counter);
  const dispatch = useDispatch();
  return (
    <div>
      <h1>Counter: {count}</h1>
      <h2>Even Counter: {evenCounter}</h2>
      <h2>Odd Counter: {oddCounter}</h2>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(incevenCounter())}>Increment Even</button>
      <button onClick={() => dispatch(incoddCounter())}>Increment Odd</button>
    </div>
  )
}

export default App;