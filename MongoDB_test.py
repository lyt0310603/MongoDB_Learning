from pymongo import MongoClient
import pprint
import datetime

uri = "mongodb+srv://lyt0310603:xjp971403@cluster0.manfrh4.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.Learning
collection = db.ptt_CFantasy

query = {"time": {'$regex': ' '}}
result = collection.find(query).limit(5)
for i in result:
    pprint.pprint(i)

client.close()