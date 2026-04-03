// import { Header } from "./components/header";
import Header from "./components/header";
import Home from "./components/home";
import Products from "./components/productscomponents";
// import { Products } from "./components/productscomponents";
// import { SignIn } from "./components/signin";
// import { SignUp } from "./components/signup";

export default function App() {
  return <>
   <div>
      <Header/>
      <Home/>
      <Products/>
    </div>  
  </>
  
}