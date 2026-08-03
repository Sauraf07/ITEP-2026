import { useEffect, useReducer } from "react";
import Nav from "../nav/Nav";
import { toast } from "react-toastify";
import BASE_URL from "../../Api";
import { useSelector } from "react-redux";
import { Outlet, useNavigate } from "react-router-dom";
import axiosInstance from "../../axios-config/api";

function ViewCart(){
    const {currentUser} = useSelector((store)=>store.user)
    let [state,dispatch] = useReducer((state,action)=>{
        if(action.type === "set-cart-items"){
            let itemList = []
            let totalBill = 0
            for(let item of action.payload){
                const p = { ...item.product, qty: 1, totalPrice: item.product.price }
                itemList.push(p)
                totalBill += p.qty * p.price
            }
            return { cartItems: itemList, totalBillAmount: totalBill }
        }    
        else if(action.type === "update-qty"){
           let productId = action.payload.id
           let qty = parseInt(action.payload.qty) || 1
           let updatedItems = state.cartItems.map((item) => {
               if (item.id === productId) {
                   return { ...item, qty: qty, totalPrice: item.price * qty }
               }
               return item
           })
           let totalBill = updatedItems.reduce((acc, item) => acc + item.totalPrice, 0)
           return { cartItems: updatedItems, totalBillAmount: totalBill }
        }
        else if(action.type === "remove-item"){
           let productId = action.payload
           let updatedItems = state.cartItems.filter((item) => item.id !== productId)
           let totalBill = updatedItems.reduce((acc, item) => acc + item.totalPrice, 0)
           return { cartItems: updatedItems, totalBillAmount: totalBill }
        }
        return state
    },{
        cartItems: [], totalBillAmount: 0
    })

    useEffect(()=>{
        if(currentUser?.id) {
            loadCartItems()
        }
    },[currentUser])

    const navigate = useNavigate()

    const loadCartItems = async()=>{
        try{
           const response = await axiosInstance.get(`/cart/${currentUser.id}`)
           dispatch({type:"set-cart-items",payload: response.data.cart_items})
        }
        catch(err){
            console.log(err)
            toast.error("Failed to load cart items")
        }
    }

    const removeCartItem = async(productId)=>{
        try{
           let response = await axiosInstance.delete(`/cart/${currentUser.id}/${productId}`)
           dispatch({type:"remove-item", payload: productId})
           toast.success(response.data.message || "Item removed successfully")
        }
        catch(err){
           console.log(err)
           toast.error("Failed to remove item")
        }
    }

    const navigateToPlaceOrder = ()=>{
        navigate("/checkout",{state:{params:{cartItems:state.cartItems,totalBillAmount: state.totalBillAmount,currentUser}}})
    }

    return <>
      <Nav/>
      <div className="container mt-4">
         <h2>Your Cart</h2>
         {state.cartItems.length === 0 ? (
             <div className="alert alert-info text-center mt-4">
                 <h4>Your cart is empty!</h4>
                 <button onClick={() => navigate("/")} className="btn btn-warning mt-2">Explore Products</button>
             </div>
         ) : (
             <div className="row mt-3">
                <div className="col-md-8 border p-3">
                    <table className="table table-striped align-middle">
                        <thead>
                            <tr>
                                <th>S.No</th>
                                <th>Title</th>
                                <th>Image</th>
                                <th>Price</th>
                                <th>Total Price</th>
                                <th>Qty</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                           {state.cartItems.map((cartItem,index)=>{return <tr key={cartItem?.id}>
                             <td>{index+1}</td>
                             <td>{cartItem?.title}</td>
                             <td>
                                <img src={BASE_URL+`${cartItem?.product_image}`} width="50px" height="50px" style={{objectFit:"cover"}} alt={cartItem?.title}/>
                             </td>
                             <td>{cartItem?.price} Rs.</td>
                             <td id={`total-price-`+cartItem.id}>{cartItem?.totalPrice} Rs.</td>
                             <td>
                                <input onChange={(event)=>dispatch({type:"update-qty",payload:{id: cartItem.id, qty: event.target.value}})} type="number" value={cartItem.qty} min="1" style={{width:"60px"}} className="form-control form-control-sm"/>
                             </td>
                             <td>
                                <button onClick={()=>removeCartItem(cartItem.id)} className="btn btn-sm btn-outline-danger">Remove</button>
                             </td>
                           </tr>})}           
                        </tbody>
                    </table>
                </div>
                <div className="col-md-4 border p-3">
                    <h4 className="bg-warning text-white p-2 text-center rounded">Bill Summary</h4>
                    <p><b>Total Items : </b>{state.cartItems.length}</p>
                    <p><b>Bill Amount :</b> <span className="text-success" style={{fontSize:"20px", fontWeight:"bolder"}}>{state.totalBillAmount} Rs.</span></p>
                    <button onClick={navigateToPlaceOrder} className="btn btn-warning w-100 mt-2 text-white font-weight-bold">Checkout</button> 
                </div>
             </div>
         )}
      </div>
      <div className="container mt-3">
        <Outlet/>
      </div>
    </>
}

export default ViewCart;
