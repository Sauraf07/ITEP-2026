import User from "../models/user.model.js";

export const registerUser = async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.json(user);
  } catch (error) {
    res.json({ message: error.message });
  }
};