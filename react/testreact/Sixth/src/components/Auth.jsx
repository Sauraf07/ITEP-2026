import { Navigate, useNavigate } from "react-router-dom";

export const isLoggedIn = ()=>{
   return !!sessionStorage.getItem("currentUserEmail"); 
}

function Auth({children}){
   if(isLoggedIn())
    return children; // <BuyNow/>
   return <Navigate to="/sign-in"/>
}

export default Auth;