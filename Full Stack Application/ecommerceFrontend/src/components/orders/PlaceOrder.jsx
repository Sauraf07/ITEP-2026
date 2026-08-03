import axios from "axios";
import { useRef } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import Nav from "../nav/Nav";
import BASE_URL  from "../../Api";
import { toast } from "react-toastify";
import axiosInstance from "../../axios-config/api";

function PlaceOrder(){
    const location = useLocation()
    const navigate = useNavigate()
    
    let params = location.state?.params || {cartItems: [], totalBillAmount: 0, currentUser: {}}
    let {cartItems,totalBillAmount,currentUser} = params
    let nameRef = useRef("")
    let emailRef = useRef("")
    let contactRef = useRef("")
    let deliveryAddressRef = useRef("")

    const handleSubmit = async (event)=>{
      try{
        event.preventDefault()
        let name = nameRef.current.value
        let email = emailRef.current.value
        let contact = contactRef.current.value
        let address = deliveryAddressRef.current.value
        
        let orderDetails = {
            "user_id":currentUser.id,
            "totalBillAmount": totalBillAmount,
            "name": name,
            "email":email,
            "contact" : contact,
            "address": address,
            "order_items":cartItems
        }
        let response = await axiosInstance.post("/orders/",orderDetails)
        toast.success("Order placed successfully.....")
        setTimeout(()=>{
          navigate("/")
        },1500)
      }
      catch(err){
        toast.error("Oops! something went wrong...")
        console.log(err)
      } 
    }
    return <>
       <Nav/>
       <h1 className="container mt-3">Enter order details</h1>
       <div className="container">
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Enter name</label>
                <input ref={nameRef} defaultValue={currentUser?.name || ""} type="text" className="text-capitalize form-control"/>
            </div>
            <div className="form-group">
                <label>Enter email id</label>
                <input ref={emailRef} defaultValue={currentUser?.email || ""} type="text" className="form-control"/>
            </div>
            <div className="form-group">
                <label>Enter contact number</label>
                <input ref={contactRef} defaultValue={currentUser?.contact || ""} type="text" className="form-control"/>
            </div>
            <div>
                <label>Enter delivery address</label>
                <textarea ref={deliveryAddressRef} className="form-control"></textarea>
            </div>
            <div className="form-group mt-2">
                <button className="btn btn-secondary">Place order</button>
            </div>
        </form>
       </div>
    </>
}

export default PlaceOrder;