import sequelize from "../config/dbconfig.js";
import Product from "../models/product.model.js";
import Reviews from "../models/reviws.model.js";

export const fetchById = async(request,response,next)=>{
    try{
      let id = request.params.id;
      const product = await Product.findByPk(id,{include:[{model: Reviews}]});
      return response.status(200).json({product});
    }
    catch(err){
        return response.status(500).json({error: "Internal Server Error"});
    }
}
export const fetchAll = async(request,response,next)=>{
    try{
       let products = await Product.findAll({include:[{model: Reviews}]});
       return response.status(200).json({products});
    }
    catch(err){
        return response.status(500).json({error:"Internal Server Error"});
    }
}
export const saveInBulk = async (request,response,next)=>{
   let transaction = await sequelize.transaction();
   try{ 
    let productList = request.body;
    for(let product of productList){
      let reviewsList = product.reviews;
      let rList = []
      for(let r of reviewsList){
        r.productId = product.id
        rList.push(r)
      }
      await Product.create(product,{transaction});
      await Reviews.bulkCreate(rList,{transaction});
    }
    await transaction.commit();
    return response.status(200).json({message: "Products saved..."});
   }
   catch(err){
    await transaction.rollback();
    console.log(err);
    return response.status(500).json({error: "Internal Server Error"});
   }

}