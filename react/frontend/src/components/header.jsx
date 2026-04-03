function Header() {
  return <>
  <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <a className="navbar-brand" href="#">MyStore</a>
      <div className="ms-auto d-flex gap-3">
        <button className="btn btn-outline-light">Home</button>
        <button className="btn btn-outline-light">Cart</button>
        <button className="btn btn-outline-light">Sign In</button>
      </div>
    </nav>
  </> 
    
  
}
export default Header;