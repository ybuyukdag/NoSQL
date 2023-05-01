import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ybuyukdag:(*PASSWORD*)@cluster0.tyezpvw.mongodb.net/node-app?retryWrites=true&w=majority")


mydb = myclient["node-app"]

mycollection = mydb["products"]

# product = {"name":"Samsung S13","price":"25000"}
# result = mycollection.insert_one(product)

# print(result)
# print(result.inserted_id)

productList = [
    {"name":"Samsung S14","price":"28000","description":"iyi telefon"},
    {"name":"Samsung S15","price":"29000","categories":["telefon,elektronik"]},
]

result = mycollection.insert_many(productList)
print(result)
