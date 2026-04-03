import "bootstrap/dist/css/bootstrap.min.css";
import { Route, Routes } from "react-router-dom";
import Home from "./components/home";
import Categories from "./components/Catagory";
import Product from "./components/Product";
import ViewMore from "./components/viewmore";
import BuyNow from "./components/BuyNow";
import SignIn from "./components/user/SignIn";
import SignUp from "./components/user/SignUp";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer } from "react-toastify";
import Auth from "./components/Auth";
import SignOut from "./components/user/SignOut";
function App() {
  return (
    <>
      <ToastContainer />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="category" element={<Categories />} />
        <Route path="product" element={<Product />} />
        <Route
          path="view-more/:id"
          element={
            <Auth>
              <ViewMore />
            </Auth>
          }
        />
        <Route
          path="buy-now"
          element={
            <Auth>
              <BuyNow />
            </Auth>
          }
        />
        <Route path="sign-in" element={<SignIn />} />
        <Route path="sign-up" element={<SignUp />} />
        {/* <Route path='sign-out' element={<SignOut/>}/> */}
      </Routes>
    </>
  );
}

export default App;
