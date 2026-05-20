import requests
import json
response = requests.get("https://dummyjson.com/products")
# print(response.status_code)
# print(response.headers)
response= response.json()
# print(type(response.json()))
def get_api_response(data):
    try:
        with open("file-collection/product.json","w") as f:
            json.dump(data,f,indent=4)
            print("Operation Success")
    except Exception as e:
        print(e)

# get_api_response(response)

def read_file():
    try:
      with open("file-collection/product.json") as f:
        data =  json.load(f)
        product_list = data["products"]
        for product in product_list:
           print(product["title"]," : ",product["price"])
    except Exception as e:
      print(e)

read_file()