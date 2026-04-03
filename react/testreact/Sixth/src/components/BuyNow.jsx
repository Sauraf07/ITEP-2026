import { useLocation, useNavigate } from "react-router-dom";
import Header from "./Header";

function BuyNow() {
  const location = useLocation();
  console.log(location);
  let { id, title, price, thumbnail } = location.state.params;
  const navigate = useNavigate();
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
        <div className="container border mt-2">
          <h3>
            <img src={thumbnail} width="100px" height="100px" />
            Title : {title}
          </h3>
          <p>
            <b>
              Price : <label className="text-success">{price}Rs.</label>
            </b>
          </p>
          <form>
            <div className="form-group mt-2">
              <label>Name</label>
              <input
                type="text"
                placeholder="Enter name"
                className="form-control"
              />
            </div>
            <div className="form-group mt-2">
              <label>Contact number</label>
              <input
                type="text"
                placeholder="Enter contact number"
                className="form-control"
              />
            </div>
            <div className="form-group mt-2">
              <label>Delivery address</label>
              <textarea className="form-control"></textarea>
            </div>
            <div className="mt-2 mb-2">
              <button className="btn btn-warning">Place order</button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}

export default BuyNow;
