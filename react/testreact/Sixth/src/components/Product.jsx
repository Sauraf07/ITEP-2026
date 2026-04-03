import { useEffect, useReducer } from "react";
import Header from "./Header";
import axios from "axios";
import Api from "../../Api";
import { useNavigate } from "react-router-dom";

function Product() {
  const navigate = useNavigate();
  const [state, dispatch] = useReducer(
    (state, action) => {
      if (action.type == "set-product") state.productList = action.payload;
      return { ...state };
    },
    {
      productList: [],
    },
  );
  useEffect(() => {
    loadProducts();
  }, []);
  const loadProducts = async () => {
    try {
      let response = await axios.get(Api.FETCH_PRODUCTS);
      console.log(response.data);
      dispatch({ type: "set-product", payload: response.data.products });
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <>
      <Header />
      <div className="container mt-2">
        <div className="row">
          {state.productList.map((product, index) => {
            return (
              <div key={product.id} className="col-md-3 p-2">
                <div
                  className="d-flex flex-column justify-content-center align-items-center"
                  style={{ height: "350px", boxShadow: "10px 10px 10px blue" }}
                >
                  <img src={product.thumbnail} height="200px" />

                  <p>{product.title}</p>
                  <h6>{product.price}</h6>
                  <button
                    onClick={() => {
                      navigate(`/view-more/${product.id}`);
                    }}
                    className="btn btn-warning"
                    style={{ width: "100%" }}
                  >
                    View more
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}

export default Product;
