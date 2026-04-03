import { Navigate } from "react-router-dom";
function SignOut(){
    sessionStorage.setItem("currentUserEmail","");
    sessionStorage.clear();
    return <Navigate to="/sign-in"/>
}

export default SignOut;