import CareerPath from "../models/careerpath.model.js";
import RoadmapStep from "../models/roadmap.model.js";

// IT Industry Important Subjects
const IT_SUBJECTS = [
  { name: "Data Structures", importance: 10 },
  { name: "Algorithms", importance: 10 },
  { name: "Database Management Systems (DBMS)", importance: 9 },
  { name: "Operating Systems", importance: 9 },
  { name: "Computer Networks", importance: 9 },
  { name: "Object Oriented Programming (OOP)", importance: 9 },
  { name: "Web Development", importance: 8 },
  { name: "JavaScript/TypeScript", importance: 8 },
  { name: "Python Programming", importance: 8 },
  { name: "Java Programming", importance: 8 },
  { name: "SQL Queries", importance: 9 },
  { name: "Cloud Computing", importance: 8 },
  { name: "Docker & Kubernetes", importance: 7 },
  { name: "Git & Version Control", importance: 8 },
  { name: "REST APIs", importance: 8 },
  { name: "Machine Learning Basics", importance: 7 },
  { name: "System Design", importance: 8 },
  { name: "Cybersecurity Fundamentals", importance: 7 },
  { name: "Linux/Unix Systems", importance: 8 },
  { name: "DevOps Tools", importance: 7 }
];

// IT Industry Careers with Roadmaps
const IT_CAREERS = {
  "Full Stack Developer": {
    description: "Develops complete web applications (frontend + backend)",
    roadmap: [
      { step: 1, title: "Master HTML, CSS, JavaScript", description: "Learn web fundamentals and UI creation" },
      { step: 2, title: "Frontend Framework (React/Vue)", description: "Learn modern frontend frameworks" },
      { step: 3, title: "Backend Basics (Node.js/Python)", description: "Learn backend development" },
      { step: 4, title: "Database Design", description: "SQL and NoSQL databases" },
      { step: 5, title: "APIs & Integration", description: "Create and consume REST APIs" },
      { step: 6, title: "Deployment & DevOps", description: "Learn Docker, cloud deployment" },
      { step: 7, title: "System Design", description: "Design scalable applications" },
      { step: 8, title: "Build Portfolio Projects", description: "Create real-world projects" }
    ]
  },
  "Frontend Developer": {
    description: "Specializes in user interface and user experience",
    roadmap: [
      { step: 1, title: "HTML & CSS Mastery", description: "Semantic HTML, CSS Grid, Flexbox" },
      { step: 2, title: "JavaScript Advanced", description: "ES6+, Async programming, DOM manipulation" },
      { step: 3, title: "React Fundamentals", description: "Components, hooks, state management" },
      { step: 4, title: "State Management", description: "Redux, Context API, Zustand" },
      { step: 5, title: "UI/UX Principles", description: "Responsive design, accessibility (A11y)" },
      { step: 6, title: "Testing & Debugging", description: "Jest, Cypress, Chrome DevTools" },
      { step: 7, title: "Build Tools", description: "Webpack, Vite, npm scripts" },
      { step: 8, title: "Performance Optimization", description: "Code splitting, lazy loading, SEO" }
    ]
  },
  "Backend Developer": {
    description: "Focuses on server-side development and databases",
    roadmap: [
      { step: 1, title: "Programming Fundamentals", description: "Choose Java/Python/Go and master basics" },
      { step: 2, title: "Database Design", description: "Relational and NoSQL databases" },
      { step: 3, title: "Backend Frameworks", description: "Spring Boot/Django/FastAPI" },
      { step: 4, title: "APIs & Web Services", description: "RESTful APIs, GraphQL" },
      { step: 5, title: "Authentication & Security", description: "JWT, OAuth, encryption" },
      { step: 6, title: "Caching & Performance", description: "Redis, database optimization" },
      { step: 7, title: "Microservices Architecture", description: "Service-oriented design" },
      { step: 8, title: "Deployment & Monitoring", description: "Cloud platforms, logging, monitoring" }
    ]
  },
  "Data Scientist": {
    description: "Analyzes data and builds machine learning models",
    roadmap: [
      { step: 1, title: "Python Programming", description: "Master Python for data science" },
      { step: 2, title: "Mathematics & Statistics", description: "Probability, distributions, hypothesis testing" },
      { step: 3, title: "Data Analysis with Pandas", description: "Data manipulation and cleaning" },
      { step: 4, title: "Data Visualization", description: "Matplotlib, Seaborn, Plotly" },
      { step: 5, title: "Machine Learning Algorithms", description: "Supervised and unsupervised learning" },
      { step: 6, title: "Deep Learning", description: "Neural networks, TensorFlow/PyTorch" },
      { step: 7, title: "SQL for Data Analysis", description: "SQL queries and optimization" },
      { step: 8, title: "Model Deployment", description: "Flask, FastAPI, cloud deployment" }
    ]
  },
  "DevOps Engineer": {
    description: "Manages infrastructure, deployment, and operations",
    roadmap: [
      { step: 1, title: "Linux/Unix Administration", description: "Command line, system administration" },
      { step: 2, title: "Scripting (Bash, Python)", description: "Automation and scripting" },
      { step: 3, title: "Version Control (Git)", description: "Git workflows and branching" },
      { step: 4, title: "CI/CD Pipelines", description: "Jenkins, GitLab CI, GitHub Actions" },
      { step: 5, title: "Containerization (Docker)", description: "Docker images, containers" },
      { step: 6, title: "Orchestration (Kubernetes)", description: "K8s clusters and deployments" },
      { step: 7, title: "Cloud Platforms", description: "AWS, GCP, or Azure" },
      { step: 8, title: "Monitoring & Logging", description: "Prometheus, ELK stack, DataDog" }
    ]
  },
  "Mobile App Developer": {
    description: "Develops applications for mobile platforms",
    roadmap: [
      { step: 1, title: "Choose Platform (iOS/Android)", description: "Swift/Kotlin or React Native" },
      { step: 2, title: "Fundamentals", description: "UI components, layouts, navigation" },
      { step: 3, title: "State Management", description: "Managing app state" },
      { step: 4, title: "APIs & Networking", description: "HTTP requests, REST APIs" },
      { step: 5, title: "Local Storage", description: "Databases, file storage" },
      { step: 6, title: "Testing & Debugging", description: "Unit testing, debugging tools" },
      { step: 7, title: "Performance Optimization", description: "Memory, battery, responsiveness" },
      { step: 8, title: "Deployment", description: "App Store/Play Store publishing" }
    ]
  },
  "Cloud Architect": {
    description: "Designs cloud infrastructure and solutions",
    roadmap: [
      { step: 1, title: "Cloud Fundamentals", description: "IaaS, PaaS, SaaS concepts" },
      { step: 2, title: "Core Services", description: "Compute, storage, networking" },
      { step: 3, title: "Databases in Cloud", description: "RDS, DynamoDB, Firestore" },
      { step: 4, title: "Security Best Practices", description: "IAM, encryption, compliance" },
      { step: 5, title: "Scalability & High Availability", description: "Load balancing, auto-scaling" },
      { step: 6, title: "Cost Optimization", description: "Resource management, billing" },
      { step: 7, title: "Infrastructure as Code", description: "Terraform, CloudFormation" },
      { step: 8, title: "Disaster Recovery", description: "Backup, failover, business continuity" }
    ]
  },
  "AI/ML Engineer": {
    description: "Develops artificial intelligence and machine learning systems",
    roadmap: [
      { step: 1, title: "Math Fundamentals", description: "Linear algebra, calculus, statistics" },
      { step: 2, title: "Python for ML", description: "NumPy, Pandas, Scikit-learn" },
      { step: 3, title: "Traditional ML", description: "Regression, Classification, Clustering" },
      { step: 4, title: "Deep Learning", description: "Neural networks, CNN, RNN, Transformers" },
      { step: 5, title: "NLP Basics", description: "Text processing, embeddings" },
      { step: 6, title: "Computer Vision", description: "Image processing, object detection" },
      { step: 7, title: "Model Optimization", description: "Quantization, pruning, distillation" },
      { step: 8, title: "Production Deployment", description: "MLOps, model serving, monitoring" }
    ]
  },
  "Cybersecurity Specialist": {
    description: "Protects systems and data from security threats",
    roadmap: [
      { step: 1, title: "Networking Fundamentals", description: "TCP/IP, DNS, HTTP/HTTPS" },
      { step: 2, title: "Operating Systems Security", description: "Windows, Linux security" },
      { step: 3, title: "Cryptography", description: "Encryption, hashing, digital signatures" },
      { step: 4, title: "Web Security", description: "OWASP Top 10, SQL injection prevention" },
      { step: 5, title: "Penetration Testing", description: "Ethical hacking, vulnerability scanning" },
      { step: 6, title: "Firewalls & IDS", description: "Network defense tools" },
      { step: 7, title: "Incident Response", description: "Detection and recovery" },
      { step: 8, title: "Compliance & Governance", description: "Security policies, standards" }
    ]
  }
};

export const seedAllData = async (req, res, next) => {
  try {
   
    const existingCareers = await CareerPath.findAll();
    
    if (existingCareers.length > 0) {
      return res.json({
        message: "Data already seeded",
        careers: existingCareers.length
      });
    }

    let totalRoadmapSteps = 0;
    for (const [careerName, careerData] of Object.entries(IT_CAREERS)) {
      await CareerPath.create({
        user_id: 0, 
        career_field: careerName,
        description: careerData.description
      });

      for (const step of careerData.roadmap) {
        await RoadmapStep.create({
          career_field: careerName,
          step_number: step.step,
          step_title: step.title,
          description: step.description
        });
        totalRoadmapSteps++;
      }
    }

    res.json({
      message: "Data seeded successfully",
      careers: Object.keys(IT_CAREERS).length,
      roadmapSteps: totalRoadmapSteps,
      careersList: Object.keys(IT_CAREERS)
    });

  } catch (error) {
    next(error);
  }
};

export const getImportantSubjects = async (req, res, next) => {
  try {
    res.json({
      message: "Important IT subjects",
      subjects: IT_SUBJECTS
    });
  } catch (error) {
    next(error);
  }
};

export const getAllCareers = async (req, res, next) => {
  try {
    const careers = await CareerPath.findAll({
      where: { user_id: 0 },
      attributes: ['id', 'career_field', 'description']
    });

    res.json({
      message: "All IT careers",
      careers
    });
  } catch (error) {
    next(error);
  }
};

export const getCareerRoadmap = async (req, res, next) => {
  try {
    const { careerField } = req.params;

    const roadmap = await RoadmapStep.findAll({
      where: { career_field: careerField },
      order: [["step_number", "ASC"]]
    });

    if (roadmap.length === 0) {
      return res.status(404).json({
        message: `No roadmap found for career: ${careerField}`
      });
    }

    res.json({
      message: "Career roadmap",
      career_field: careerField,
      totalSteps: roadmap.length,
      roadmap
    });
  } catch (error) {
    next(error);
  }
};
