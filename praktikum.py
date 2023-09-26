from pymongo import MongoClient

connection = MongoClient('localhost', 27000)

db = connection.praktikum

collection = db.warehouses
data=[
    { "_id" : 6, "stock_item" : "almonds", "warehouse": "A", "instock" : 120 },
    { "_id" : 7, "stock_item" : "pecans", "warehouse": "A", "instock" : 80 },
    { "_id" : 8, "stock_item" : "almonds", "warehouse": "B", "instock" : 60 },
    { "_id" : 9, "stock_item" : "cookies", "warehouse": "B", "instock" : 40 },
    { "_id" : 10, "stock_item" : "cookies", "warehouse": "A", "instock" : 80 }
]
docs=collection.insert_many(data)
