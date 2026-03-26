import jwt from "jsonwebtoken";

export const auth = (req, res, next) => {
  const header = req.headers.authorization;
  if (!header) return res.send("No token");
  const token = header.split(" ")[1];
  try {
    const data = jwt.verify(token, "secret");
    req.userId = data.id;
    next();
  } catch {
    res.send("Invalid token");
  }
};