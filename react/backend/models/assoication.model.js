import Product from "./product.model.js";
import Reviews from "./reviws.model.js";
import User from "./user.model.js";
Product.hasMany(Reviews);
Reviews.belongsTo(Product);