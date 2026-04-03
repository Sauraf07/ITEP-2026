function SignIn() {
  return (
    <div className="auth-container">
      <form className="auth-form">
        <h3>Sign In</h3>
        <input type="email" placeholder="Email" className="form-control mb-2" />
        <input type="password" placeholder="Password" className="form-control mb-2" />
        <button className="btn btn-dark w-100">Login</button>
      </form>
    </div>
  );
}
export default SignIn;