import Category from "../models/catagory.model.js"

export const fetchAll = async(request,response,next)=>{
  try{
    let categories = await Category.findAll({raw : true});
    return response.status(200).json({categories});
  }
  catch(err){
    return response.status(500).json({error: "Internal Server Error"});
  }
}
export const saveInBulk = (request,response,next)=>{
   let categoryList = request.body
   Category.bulkCreate(categoryList)
   .then(result=>{
     return response.status(200).json({message: "Category saved..."});
   }).catch(err=>{
    return response.status(500).json({error: "Internal Server Error..."});
   })
}