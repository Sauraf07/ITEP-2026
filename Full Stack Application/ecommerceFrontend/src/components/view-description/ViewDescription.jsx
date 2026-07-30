import { useNavigate, useParams } from "react-router-dom";
import Nav from "../nav/Nav";
import { useEffect, useState } from "react";
import axios from "axios";
import Api, { BASE_URL } from "../../Api";
import { useSelector } from "react-redux";
import { toast } from "react-toastify";

function ViewDescription(){
    const {id} = useParams()
    const [product,setProduct] = useState(null)
    const {isLoggedIn,currentUser} = useSelector((store)=>store.user)
    useEffect(()=>{
        const loadProduct = async ()=>{
            try {
                const response = await axios.get(BASE_URL+`/product/${id}`)
                setProduct(response.data)
            } catch {
                toast.error("Unable to load product.")
            }
        }
        loadProduct()
    },[id])
    const navigate = useNavigate()

    const addToCart = async()=>{
      try{  
        if(!isLoggedIn) {
            toast.info("please signin first")
            navigate("/signin")
        } else {
            const response = await axios.post(Api.ADD_TO_CART,{product_id: Number(id)}, {
                headers: { Authorization: `Bearer ${currentUser.token}` },
            })
            toast.info(response.data.message)
        }
      }
      catch(err){
        toast.error(err.response?.data?.message || "Unable to add item to cart.")
      }  
    }
    return <>
     <Nav/>
     <div className="mt-3 container">
        <button className="btn btn-secondary mb-3" onClick={()=>navigate(-1)}>Back</button>
        <div className="row">
            <div className="col-md-6">
                <img src={`http://localhost:8000${product?.product_image}`} style={{width:"100%", height:"400px"}}/>
            </div>
            <div className="col-md-6 border">
                <h1>{product?.title}</h1>
                <p>{product?.description}</p>
                <p>Rating : {product?.rating}/(5)</p>
                <h4 className="text-success">Price : {product?.price} Rs</h4>
                <p>Warranty Information : {product?.warranty_information}</p>
                <button onClick={addToCart} className="btn btn-warning" style={{width:"100%"}}>Add To Cart</button>
            </div>
        </div>
    </div> 
    </>
}

export default ViewDescription;
