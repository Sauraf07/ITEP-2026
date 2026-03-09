import express from "express";
import Restaurant from "../models/restaurent.model.js";
import MenuItem from "../models/menuItem.model.js";

const router = express.Router();

router.post("/restaurants", async (req, res) => {
  const restaurant = await Restaurant.create(req.body);
  res.json(restaurant);
});

router.get("/restaurants", async (req, res) => {
  const restaurants = await Restaurant.findAll();
  res.json(restaurants);
});

router.get("/restaurants/:id/menu", async (req, res) => {
  const data = await Restaurant.findByPk(req.params.id, {
    include: MenuItem
  });

  res.json(data);
});

router.post("/restaurants/:restaurantId/menu-items", async (req, res) => {
  const item = await MenuItem.create({
    ...req.body,
    RestaurantId: req.params.restaurantId
  });

  res.json(item);
});

router.get("/restaurants/:restaurantId/menu-items", async (req, res) => {
  const items = await MenuItem.findAll({
    where: { RestaurantId: req.params.restaurantId }
  });

  res.json(items);
});

export default router;