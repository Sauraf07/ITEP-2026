function IncrementCounter({counter,setCounter}){
    return <>
      <h2>Increment Counter..{counter}</h2>
      <button onClick={()=>setCounter(counter+1)}> Increment Counter</button>
    </>
}
export default IncrementCounter;