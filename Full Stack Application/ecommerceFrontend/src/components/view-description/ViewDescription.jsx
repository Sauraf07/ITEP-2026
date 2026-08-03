import { useNavigate, useParams } from "react-router-dom";
import Nav from "../nav/Nav";
import { useEffect, useState } from "react";
import axios from "axios";
import BASE_URL  from "../../Api";
import { useSelector } from "react-redux";
import { toast } from "react-toastify";
import axiosInstance from "../../axios-config/api";

function ViewDescription(){
    const {id} = useParams()
    const [product,setProduct] = useState(null)
    const {isLoggedIn,currentUser} = useSelector((store)=>store.user)
    useEffect(()=>{
        loadProduct()
    },[])
    const loadProduct = async ()=>{
        let response = await axiosInstance.get(`/product/${id}`)
        setProduct(response.data)
    }
    const navigate = useNavigate()

    const addToCart = async()=>{
      try{  
        if(!isLoggedIn || !currentUser?.id){
            toast.info("Please sign in first to add items to cart")
            navigate("/signin")
            return
        }
        let response = await axiosInstance.post("/cart/",{"user_id":currentUser.id,"product_id":parseInt(id)})
        toast.success(response.data.message || "Item added to cart successfully")
      }
      catch(err){
        console.error("Add to cart error:", err)
        const msg = err?.response?.data?.message || err?.response?.data?.detail || err?.message || "Failed to add item to cart"
        toast.error(msg)
        if(err?.response?.status === 401 || err?.response?.status === 403) {
            toast.info("Session expired. Please sign in again.")
            navigate("/signin")
        }
      }  
    }
    return <>
     <Nav/>
     <div className="mt-3 container">
        <button className="btn btn-secondary mb-3" onClick={()=>navigate(-1)}>Back</button>
        <div className="row">
            <div className="col-md-6">
                <img src={BASE_URL + product?.product_image} style={{width:"100%", height:"400px", objectFit:"cover"}} alt={product?.title}/>
            </div>
            <div className="col-md-6 border p-4">
                <h1>{product?.title}</h1>
                <p className="mt-3">{product?.description}</p>
                <p>Rating : {product?.rating} / 5</p>
                <h4 className="text-success my-3">Price : {product?.price} Rs</h4>
                <p>Warranty Information : {product?.warranty_information}</p>
                <button onClick={addToCart} className="btn btn-warning text-white font-weight-bold w-100 py-2 mt-3">Add To Cart</button>
            </div>
        </div>
    </div> 
    </>

}

export default ViewDescription;