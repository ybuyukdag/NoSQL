import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ybuyukdag:Ysfmdb103@cluster0.tyezpvw.mongodb.net/node-app?retryWrites=true&w=majority")


mydb = myclient["node-app"]


print(mydb.list_collection_names)