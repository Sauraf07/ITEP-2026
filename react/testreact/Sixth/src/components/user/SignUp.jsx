import axios from "axios";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Api from "../../Api";

function SignUp(){
    const [name,setName] = useState("");
    const [contact,setContact] = useState("");
    const [email,setEmail] = useState("");
    const [password,setPassword] = useState("");
    const [address,setAddress] = useState("");
    const navigate = useNavigate();
    const handleSubmit = ()=>{
      axios.post(Api.USER_SIGNUP,{name,contact,email,password,address})
      .then(response=>{
        navigate("/sign-in")
      }).catch(err=>{
        console.log(err);
      });
    }
    return <>
     <div className="d-flex justify-content-center align-items-center" style={{height:"650px"}}>
        <div className="border" style={{width:"35%",minHeight:"200px"}}>
            <h6 className="bg-danger p-2 text-white text-center">Sign up</h6>
            <div className="container mt-2 d-flex flex-column align-items-center">
              <input onChange={(event)=>{setName(event.target.value)}} type="text" placeholder="Enter name" className="form-control"/>
              <input onChange={(event)=>{setContact(event.target.value)}} type="text" placeholder="Enter contact number" className="form-control mt-2"/>   
              <input onChange={(event)=>{setEmail(event.target.value)}} type="text" placeholder="Enter email id" className="form-control mt-2"/>
              <input onChange={(event)=>{setPassword(event.target.value)}} type="text" placeholder="Enter password" className="form-control mt-2"/>
              <textarea onChange={(event)=>{setAddress(event.target.value)}} className="form-control mt-2" placeholder="Enter address"></textarea>
              <button onClick={handleSubmit} className="btn btn-secondary mt-2">Submit</button>
              <Link to="/sign-in">Already have account ?</Link>
            </div>
        </div>
     </div>
    </>
}

export default SignUp;