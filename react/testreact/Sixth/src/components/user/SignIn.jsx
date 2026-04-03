import axios from "axios";
import { useRef } from "react";
import { Link, useNavigate } from "react-router-dom";
import Api from "../../Api";
import { toast } from "react-toastify";

function SignIn(){
    const emailInput = useRef();
    const passwordInput = useRef();
    const navigate = useNavigate();
    const handleSubmit = async(event)=>{
       try{ 
        event.preventDefault();
        let email = emailInput.current.value;
        let password = passwordInput.current.value;
        let response = await axios.post(Api.USER_SIGNIN,{email,password});
        console.log(response.data);
        toast.success("Sign in success..");
        sessionStorage.setItem("token",response.data.token);
        sessionStorage.setItem("currentUserId",""+response.data.user.id);
        sessionStorage.setItem("currentUserEmail",response.data.user.email);
        navigate("/");
       }
       catch(err){
         console.log(err);
         toast.error("Sign in failed..");
       }
    }
    return <>
     <div className="d-flex justify-content-center align-items-center" style={{height:"650px"}}>
        <div className="border" style={{width:"35%",minHeight:"200px"}}>
            <h6 className="bg-danger p-2 text-white text-center">Sign in</h6>
            <form onSubmit={handleSubmit}>
            <div className="container mt-2 d-flex flex-column align-items-center">
              <input ref={emailInput} type="text" placeholder="Enter email id" className="form-control"/>
              <input ref={passwordInput} type="text" placeholder="Enter password" className="form-control mt-2"/>
              <button type="submit" className="btn btn-secondary mt-2">Submit</button>
              <Link to="/sign-up">Create new account ?</Link>
            </div>
            </form>
        </div>
     </div>
    </>
}

export default SignIn;