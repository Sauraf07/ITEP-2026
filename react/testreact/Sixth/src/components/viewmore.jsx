import { useNavigate, useParams } from "react-router-dom";
import Header from "./Header";
import { useEffect, useReducer } from "react";
import axios from "axios";
import Api from "../../Api";

function ViewMore() {
  const navigate = useNavigate();
  const params = useParams();
  const { id } = params;
  const [state, dispatch] = useReducer(
    (state, action) => {
      if (action.type == "set-product") {
        state.product = action.payload;
      }
      return { ...state };
    },
    {
      product: null,
    },
  );
  useEffect(() => {
    loadProduct();
  }, []);
  const loadProduct = async () => {
    try {
      let response = await axios.get(Api.FETCH_PRODUCTS + `/${id}`);
      console.log(response.data);
      dispatch({ type: "set-product", payload: response.data.product });
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <>
      <Header />
      <div className="container mt-2">
        <button
          onClick={() => {
            navigate(-1);
          }}
          className="btn btn-outline-warning"
        >
          Back
        </button>
        <div className="row">
          <div
            className="col-md-6"
            style={{ height: "450px", boxShadow: "10px 10px 10px blue" }}
          >
            <img src={state.product?.thumbnail} width="100%" height="450px" />
          </div>
          <div
            className="col-md-6 p-2"
            style={{ height: "450px", boxShadow: "10px 10px 10px blue" }}
          >
            <div className="p-3 d-flex flex-column">
              <h5>
                {state.product?.title}[{state.product?.brand}]
              </h5>
              <p>{state.product?.description}</p>
              <p>
                <b>Warranty information : </b>
                {state.product?.warrantyInformation}
              </p>
              <p>
                <b>Shipping Information : </b>
                {state.product?.shippingInformation}
              </p>
              <p>
                <b>Availability Status : </b>
                {state.product?.availabilityStatus}
              </p>
              <p>
                <b>Rating : </b>
                {state.product?.rating}/(5)
              </p>
              <p>
                <b>Price : </b>
                <label
                  className="text-success"
                  style={{ fontWeight: "bolder", fontSize: "20px" }}
                >
                  {state.product?.price} Rs.
                </label>
              </p>
              <p>
                <b>After discount : </b>
                <del className="text-danger">{state.product?.price}</del>
                {(
                  state.product?.price -
                  (state.product?.discountPercentage * state.product?.price) /
                    100
                ).toFixed(2)}
              </p>
              <button
                onClick={() => {
                  navigate("/buy-now", { state: { params: state.product } });
                }}
                className="btn btn-warning"
                style={{ width: "100%" }}
              >
                Buy now
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
export default ViewMore;
