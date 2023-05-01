import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ybuyukdag:(*PASSWORD*)@cluster0.tyezpvw.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#delete_one
# for i in mycollection.find():
#     print(i)
# print("*"*50)

# mycollection.delete_one({"name":"Iphone XL"})
# for i in mycollection.find():
#     print(i)


#delete_many
for i in mycollection.find():
    print(i)
print("*"*50)

mycollection.delete_many({"name":{"$regex":"^S"}})
for i in mycollection.find():
    print(i)
