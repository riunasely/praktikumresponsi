from pymongo import MongoClient

MONGO_HOST = MongoClient('mongodb://localhost:27017')
db = MONGO_HOST.twitterdb

collection = db.twitter

agg_result = collection.aggregate(
    [{
    "$group":
        {"_id":"$username",
         "sum_tweet":{"$sum":1}
         }}
     ])
for i in agg_result:
    print(i)
