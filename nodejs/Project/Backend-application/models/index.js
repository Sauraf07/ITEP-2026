const sequelize = require("../config/database");

const User = require("./user.model");
const Bus = require("./bus.model");
const Booking = require("./booking.model");

User.hasMany(Booking);
Booking.belongsTo(User);

Bus.hasMany(Booking);
Booking.belongsTo(Bus);

module.exports = {
  sequelize,
  User,
  Bus,
  Booking
};