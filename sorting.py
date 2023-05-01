import pymongo
from bson.objectid import ObjectId

#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ybuyukdag:Ysfmdb103@cluster0.tyezpvw.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

result = mycollection.find()
result = mycollection.find().sort("name")
result = mycollection.find().sort("price",1) #asc
result = mycollection.find().sort("price",-1) #desc
result = mycollection.find().sort([("name",1),("price",-1)])

for i in result:
    print(i)
