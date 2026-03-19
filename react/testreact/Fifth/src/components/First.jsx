import Second from "./Second";

function First({dataMessage,studentNameList}){ // props: {dataMessage: "Good morning"}
    //console.log(props)
    //let {dataMessage,studentNameList} = props;
    return <>
       <h1>First Component...</h1>
       {studentNameList.map((studentName,index)=>{
        return <p key={index}>{studentName}</p>
       })}
       <Second />
    </>
}

export default First;