from pymongo import MongoClient
import config

# client = MongoClient("mongodb+srv://dhanvi:1234@cluster0.ljvxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class DbClient:

    def __init__(self):
        self.client = MongoClient(config.DATABASE_URL)
    
    def addCoupon(self,coupon):
        db = self.client[config.DATABASE]
        collection = db[config.COLLECTION]
        insertResult = collection.insert_one(coupon)
        return insertResult.inserted_id





