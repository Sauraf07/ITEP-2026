import { Route, Routes } from "react-router-dom";
import Home from "./components/home/Home";
import ViewDescription from "./components/view-description/ViewDescription";
import Signup from "./components/user/Signup";
import { ToastContainer } from "react-toastify";
import Signin from "./components/user/Signin";
import ViewCart from "./components/view-cart/ViewCart";
import Auth from "./components/auth/Auth";
import PlaceOrder from "./components/orders/PlaceOrder";
import CartHistory from "./components/orders/CartHistory";

function App(){
  return <>
     <ToastContainer/>
     <Routes>
       <Route path="/" element={<Home/>}/>
       <Route path="/view-description/:id" element={<ViewDescription/>}/>
       <Route path="/signup" element={<Signup/>}/>
       <Route path="/signin" element={<Signin/>}/>
       <Route path="/view-cart" element={<Auth><ViewCart/></Auth>}/>
       <Route path="/checkout" element={<Auth><PlaceOrder/></Auth>}/>
       <Route path="/order-history" element={<Auth><CartHistory/></Auth>}/>
     </Routes>
  </>
}

export default App;