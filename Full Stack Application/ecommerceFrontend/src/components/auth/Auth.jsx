import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";

function Auth({children}){ 
  const {isLoggedIn} = useSelector((store)=>store.user)
  if(isLoggedIn)
    return children; 
  else
    return <Navigate to="/signin"/>
}

export default Auth;