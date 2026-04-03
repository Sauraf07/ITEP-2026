function SignUp() {
  return (
    <div className="auth-container">
      <form className="auth-form">
        <h3>Sign Up</h3>
        <input type="text" placeholder="Name" className="form-control mb-2" />
        <input type="email" placeholder="Email" className="form-control mb-2" />
        <input type="password" placeholder="Password" className="form-control mb-2" />
        <button className="btn btn-dark w-100">Register</button>
      </form>
    </div>
  );
}
export default SignUp;