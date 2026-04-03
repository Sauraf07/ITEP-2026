import { Link } from 'react-router-dom';
import heroImg from '../assets/hero_tech_career.png';
import roadmapImg from '../assets/roadmap_feature.png';

export default function Home() {
  return (
    <div className="landing-page-wrapper">
      {/* Hero Section */}
      <div className="container mt-5 pt-5 pb-5">
        <div className="row align-items-center">
          <div className="col-lg-6 mb-5 mb-lg-0">
            <div className="hero-text pe-lg-4">
              <span className="badge bg-primary bg-opacity-10 text-primary mb-3 py-2 px-3 border border-primary border-opacity-25 rounded-pill">
                <i className="bi bi-stars me-2"></i> Your Future Awaits
              </span>
              <h1 className="display-3 fw-bold mb-4">
                Navigate your <span className="text-primary">Tech Career</span> with confidence.
              </h1>
              <p className="lead fs-5 mb-5 text-muted">
                Ditch the confusion. Get personalized roadmaps, actionable daily tasks, and data-driven recommendations tailored specifically to your academic background.
              </p>
              
              <div className="d-flex flex-wrap gap-3">
                <Link to="/register" className="btn btn-primary btn-lg pulse-btn px-5 py-3 d-flex align-items-center">
                  Start Your Journey <i className="bi bi-arrow-right ms-2 fs-5"></i>
                </Link>
                <Link to="/login" className="btn btn-outline-primary btn-lg px-5 py-3 d-flex align-items-center">
                  <i className="bi bi-person me-2"></i> Log In
                </Link>
              </div>
              
              <div className="mt-5 d-flex align-items-center gap-4 text-muted small">
                <div className="d-flex align-items-center"><i className="bi bi-check2-circle text-success me-2 fs-5"></i> AI-Powered Paths</div>
                <div className="d-flex align-items-center"><i className="bi bi-check2-circle text-success me-2 fs-5"></i> Real-world Tasks</div>
              </div>
            </div>
          </div>
          
          <div className="col-lg-6">
            <div className="hero-image-container position-relative">
              <div className="glow-backdrop position-absolute top-50 start-50 translate-middle w-100 h-100 rounded-circle" style={{ background: 'radial-gradient(circle, rgba(99,102,241,0.2) 0%, rgba(99,102,241,0) 70%)', zIndex: -1 }}></div>
              <img 
                src={heroImg} 
                alt="Tech Professional with Digital Roadmap" 
                className="img-fluid rounded-4 shadow-lg hero-img animated-float border border-light border-opacity-10"
                style={{ filter: 'drop-shadow(0 20px 40px rgba(0,0,0,0.5))' }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Features Cards Section */}
      <div className="container py-5 my-5">
        <div className="text-center mb-5 pb-3">
          <h2 className="fw-bold display-6">Everything you need to succeed</h2>
          <p className="text-muted fs-5">A complete ecosystem designed to accelerate your growth.</p>
        </div>
        
        <div className="row g-4">
          <div className="col-md-4">
            <div className="card p-4 h-100 feature-card text-center">
              <div className="icon-wrapper mb-4 mx-auto bg-primary bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center" style={{ width: '80px', height: '80px' }}>
                <i className="bi bi-person-check fs-1 text-primary animated-icon"></i>
              </div>
              <h4 className="fw-bold mb-3">Personalized Path</h4>
              <p className="text-muted">Get highly targeted career recommendations based on your unique academic background and skills.</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card p-4 h-100 feature-card text-center position-relative overflow-hidden">
              <div className="position-absolute top-0 start-50 translate-middle-x w-75 h-25" style={{ background: 'radial-gradient(ellipse at top, rgba(168,85,247,0.2), transparent)', zIndex: 0 }}></div>
              <div className="icon-wrapper mb-4 mx-auto bg-secondary bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center position-relative z-1" style={{ width: '80px', height: '80px' }}>
                <i className="bi bi-map fs-1 text-info animated-icon" style={{ animationDelay: '0.5s' }}></i>
              </div>
              <h4 className="fw-bold mb-3 position-relative z-1">Structured Roadmap</h4>
              <p className="text-muted position-relative z-1">Follow step-by-step learning paths tailored to your goals. No more guessing what to learn next.</p>
            </div>
          </div>
          <div className="col-md-4">
            <div className="card p-4 h-100 feature-card text-center">
              <div className="icon-wrapper mb-4 mx-auto bg-success bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center" style={{ width: '80px', height: '80px' }}>
                <i className="bi bi-check-circle fs-1 text-success animated-icon" style={{ animationDelay: '1s' }}></i>
              </div>
              <h4 className="fw-bold mb-3">Daily Tasks</h4>
              <p className="text-muted">Track your progress with actionable, bite-sized daily learning tasks that keep you motivated.</p>
            </div>
          </div>
        </div>
      </div>

      {/* Deep Dive Feature Section */}
      <div className="container py-5 my-5">
        <div className="row align-items-center bg-dark bg-opacity-50 rounded-5 p-4 p-md-5 border border-light border-opacity-10 shadow-lg">
          <div className="col-lg-6 mb-4 mb-lg-0 order-2 order-lg-1">
            <img 
              src={roadmapImg} 
              alt="Interactive Glowing Roadmap" 
              className="img-fluid rounded-4 shadow"
            />
          </div>
          <div className="col-lg-6 order-1 order-lg-2 ps-lg-5 mb-5 mb-lg-0">
            <span className="text-info fw-bold text-uppercase tracking-wide small mb-2 d-block">Interactive Learning</span>
            <h2 className="display-5 fw-bold mb-4">Visualize your entire journey.</h2>
            <p className="lead text-muted mb-4">
              Our dynamic roadmaps adapt to your progress. See precisely where you are, what milestones you've achieved, and what critical skills you need to tackle next to land your dream job.
            </p>
            <ul className="list-unstyled mb-5">
              <li className="d-flex align-items-start mb-3">
                <i className="bi bi-arrow-right-circle-fill text-primary fs-4 me-3 mt-1"></i>
                <div>
                  <h5 className="fw-bold mb-1">Skill-Tree Progression</h5>
                  <p className="text-muted small">Unlock new modules as you demonstrate mastery of foundational concepts.</p>
                </div>
              </li>
              <li className="d-flex align-items-start">
                <i className="bi bi-arrow-right-circle-fill text-info fs-4 me-3 mt-1"></i>
                <div>
                  <h5 className="fw-bold mb-1">Industry-Aligned Content</h5>
                  <p className="text-muted small">Curriculum reflects what top employers are actually looking for today.</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      
      {/* CTA Section */}
      <div className="container py-5 mb-5 text-center">
        <h2 className="display-6 fw-bold mb-4">Ready to level up?</h2>
        <p className="lead text-muted mb-5 max-w-2xl mx-auto">Join thousands of others who are navigating their tech careers with clarity and purpose.</p>
        <Link to="/register" className="btn btn-primary btn-lg pulse-btn px-5 py-3 rounded-pill shadow-lg">
          Create Your Free Account
        </Link>
      </div>
    </div>
  );
}