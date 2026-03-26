import { BrowserRouter, Link } from "react-router-dom";
import RouteConfig from "./routeconfig";

function App() {
  return <>
   <BrowserRouter>
      <div className="navbar navbar-expand-sm bg-dark navbar-dark">
        <div className="navbar-nav mx-auto">
          <Link to="/" className="nav-link px-3">Home</Link>
          <Link to="/about" className="nav-link px-3">About</Link>
          <Link to="/contact" className="nav-link px-3">Contact us</Link>
        </div>
      </div>

      <RouteConfig />
    </BrowserRouter>
  </>
   
}

export default App;