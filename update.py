import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://ybuyukdag:(*PASSWORD*)@cluster0.tyezpvw.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

#update_one
# mycollection.update_one(     #güncelleme/ ilk parametre değiştirmek istediğimiz yer,ikinci parametre yeni bilgi
#     {"name":"Samsung S14"},
#     {"$set":{
#         "name":"Iphone XS"
#     }}
#     )
# for i in mycollection.find():
#     print(i)

#update_many
mycollection.update_many(     #güncelleme/ ilk parametre değiştirmek istediğimiz yer,ikinci parametre yeni bilgi
    {"name":"Samsung S13"},
    {"$set":{
        "name":"Samsung S12"
    }}
    )
for i in mycollection.find():
    print(i)

# query = {"name":"Iphone XS"}
# new_values = {"$set":{
#         "name":"Iphone XL"}}

# result = mycollection.update_many(query,new_values)
# for i in result:
#     print(i)
