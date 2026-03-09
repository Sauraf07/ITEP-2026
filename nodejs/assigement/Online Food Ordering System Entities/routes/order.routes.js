import express from "express";
import Order from "../models/order.model.js";
import OrderItem from "../models/orderItem.model.js";
import MenuItem from "../models/menuItem.model.js";
import User from "../models/user.model.js";

const router = express.Router();

router.post("/users/:userId/orders", async (req, res) => {

  const order = await Order.create({
    UserId: req.params.userId,
    total_price: 0
  });

  let total = 0;

  for (const item of req.body.items) {

    const menu = await MenuItem.findByPk(item.menuItemId);

    total += menu.price * item.quantity;

    await OrderItem.create({
      OrderId: order.id,
      MenuItemId: item.menuItemId,
      quantity: item.quantity
    });
  }

  order.total_price = total;
  await order.save();

  res.json(order);
});

router.get("/users/:userId/orders", async (req, res) => {

  const orders = await Order.findAll({
    where: { UserId: req.params.userId }
  });

  res.json(orders);
});

router.get("/orders/:orderId", async (req, res) => {

  const order = await Order.findByPk(req.params.orderId, {
    include: [
      User,
      {
        model: OrderItem,
        include: MenuItem
      }
    ]
  });

  res.json(order);
});

export default router;