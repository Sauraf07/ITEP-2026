import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";
import User from "./user.model.js";
import Bus from "./bus.model.js";

const Booking = sequelize.define("Booking", {
  seat_number: DataTypes.INTEGER,
  booking_date: DataTypes.DATE
});

User.hasMany(Booking);
Booking.belongsTo(User);

Bus.hasMany(Booking);
Booking.belongsTo(Bus);

export default Booking;