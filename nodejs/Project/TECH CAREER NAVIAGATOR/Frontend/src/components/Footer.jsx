export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="mt-5 py-5 border-top" style={{ borderColor: 'var(--border-glass)' }}>
      <div className="container">
        <div className="row">
          {/* About Section */}
          <div className="col-md-4 mb-4">
            <h5 className="mb-3 fw-bold text-white">
              <i className="bi bi-compass text-primary"></i> About TECH Career Navigator
            </h5>
            <p className="text-muted">
              Guiding students through their IT career journey with personalized
              roadmaps, learning paths, and daily tasks tailored to industry
              needs.
            </p>
          </div>

          {/* Quick Links */}
          <div className="col-md-4 mb-4">
            <h5 className="mb-3 fw-bold text-white">
              <i className="bi bi-link-45deg text-primary"></i> Quick Links
            </h5>
            <ul className="list-unstyled">
              <li className="mb-2">
                <a
                  href="/"
                  className="text-muted text-decoration-none"
                  style={{ fontSize: "1rem" }}
                >
                  <i className="bi bi-house me-2"></i>Home
                </a>
              </li>
              <li className="mb-2">
                <a
                  href="/dashboard"
                  className="text-muted text-decoration-none"
                  style={{ fontSize: "1rem" }}
                >
                  <i className="bi bi-speedometer2 me-2"></i>Dashboard
                </a>
              </li>
              <li className="mb-2">
                <a
                  href="/career"
                  className="text-muted text-decoration-none"
                  style={{ fontSize: "1rem" }}
                >
                  <i className="bi bi-briefcase me-2"></i>Explore Careers
                </a>
              </li>
              <li className="mb-2">
                <a
                  href="/tasks"
                  className="text-muted text-decoration-none"
                  style={{ fontSize: "1rem" }}
                >
                  <i className="bi bi-check-square me-2"></i>My Learning Tasks
                </a>
              </li>
            </ul>
          </div>

          {/* IT Careers */}
          <div className="col-md-4 mb-4">
            <h5 className="mb-3 fw-bold text-white">
              <i className="bi bi-briefcase text-primary"></i> Featured IT Careers
            </h5>
            <div className="d-flex flex-wrap gap-2">
              <span className="badge bg-primary bg-opacity-25 text-primary border border-primary border-opacity-25 p-2">
                <i className="bi bi-stack me-1"></i>Full Stack Dev
              </span>
              <span className="badge bg-success bg-opacity-25 text-success border border-success border-opacity-25 p-2">
                <i className="bi bi-graph-up me-1"></i>Data Scientist
              </span>
              <span className="badge bg-danger bg-opacity-25 text-danger border border-danger border-opacity-25 p-2">
                <i className="bi bi-tools me-1"></i>DevOps Eng
              </span>
              <span className="badge bg-info bg-opacity-25 text-info border border-info border-opacity-25 p-2 align-items-center d-inline-flex">
                <i className="bi bi-shield-lock me-1"></i>Cybersecurity
              </span>
            </div>
          </div>
        </div>

        <hr style={{ borderColor: 'var(--border-glass)' }} />

        {/* Bottom Section */}
        <div className="row align-items-center">
          <div className="col-md-6">
            <p className="mb-0 text-muted">
              &copy; {currentYear} <strong className="text-white">Tech Career Navigator</strong>. All
              rights reserved.
            </p>
          </div>
          <div className="col-md-6 text-md-end">
            <div className="mt-3 mt-md-0">
              <a
                href="#"
                className="text-muted text-decoration-none me-3"
                title="Twitter"
                style={{ fontSize: "1.3rem" }}
              >
                <i className="bi bi-twitter"></i>
              </a>
              <a
                href="#"
                className="text-muted text-decoration-none me-3"
                title="LinkedIn"
                style={{ fontSize: "1.3rem" }}
              >
                <i className="bi bi-linkedin"></i>
              </a>
              <a
                href="#"
                className="text-muted text-decoration-none me-3"
                title="GitHub"
                style={{ fontSize: "1.3rem" }}
              >
                <i className="bi bi-github"></i>
              </a>
              <a
                href="#"
                className="text-muted text-decoration-none"
                title="Email"
                style={{ fontSize: "1.3rem" }}
              >
                <i className="bi bi-envelope"></i>
              </a>
            </div>
          </div>
        </div>

        <div className="text-center mt-4 pt-3 border-top" style={{ borderColor: 'var(--border-glass)' }}>
          <p className="text-muted small mb-0">
            Built with <i className="bi bi-heart-fill text-danger pulse-btn d-inline-block mx-1"></i> for
            aspiring tech professionals
          </p>
        </div>
      </div>

      <style>{`
        footer a:hover {
          opacity: 0.8;
          transition: opacity 0.3s ease;
        }
        footer a:hover i {
          transform: scale(1.1);
          transition: transform 0.2s ease;
        }
      `}</style>
    </footer>
  );
}
