import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET || "techcareer_secret_key_2024";

export const authenticate = (req, res, next) => {
  try {
  
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return res.status(401).json({
        message: "Access denied. No token provided."
      });
    }

    const token = authHeader.split(" ")[1];

    const decoded = jwt.verify(token, JWT_SECRET);

    req.user = decoded;

    next();

  } catch (error) {
 
    if (error.name === "TokenExpiredError") {
      return res.status(401).json({
        message: "Token expired. Please login again."
      });
    }
    return res.status(401).json({
      message: "Invalid token. Please login again."
    });
  }
};