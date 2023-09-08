# There are some problems in original collection
# This code tries to fix these problem
# Problems: 1. contain blank(" ") in some article's date
#           2. type of push_num is string not int
#              and some of them are '爆' or ''
#              ('爆' means this article is popular,
#               '' means that no one give this article like)
#           3. url lack some part to use

from pymongo import MongoClient
import pprint
import datetime
import time

# password will be hide
uri = "mongodb+srv://lyt0310603:****@cluster0.manfrh4.mongodb.net/?retryWrites=true&w=majority"

# connect to database
client = MongoClient(uri)
db = client.Learning
collection = db.ptt_CFantasy_correction

# fix 1 problem
find_query = {"time": {'$regex': ' '}}
results = collection.find(find_query)

start = time.time()
n = 1
for r in results:
    correct_query = {"_id": r['_id']}
    correct_change = {"$set": {"time": r['time'].strip()}}
    correct_result = collection.update_one(correct_query, correct_change)
    print(n)
    n += 1
end = time.time()
print("consume "+str(end-start)+" sec")


client.close()
