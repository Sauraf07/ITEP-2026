from fastapi import FastAPI, Body
from data import product_list
app = FastAPI()
@app.get("/")
async def welcome():
    return {"message": "Welcome to FastAPI!"}

@app.get("/home")
async def home():
    return {"message": "It is home page"}
@app.get("/about")
async def about():
    return {"message":"It is about page"}

@app.get("/products")
async def get_products():
    return product_list


@app.post("/product")
async def create_product(title: str=Body(...), price: float=Body(...),brand: str=Body(...)):
    id = len(product_list) + 1
    product = {"id": id, "title": title, "price": price, "brand": brand}
    product_list.append(product)
    return product

# @app.post("/product")
# async def create_product(request:Request):
#     data = await request.json()
#     data["id"] = len(product_list)+1
#     product_list.append(data)
#     return {"message":"Product created successfully","product":data}


