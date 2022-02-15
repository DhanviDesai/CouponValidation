from pymongo import MongoClient
import config

# client = MongoClient("mongodb+srv://dhanvi:1234@cluster0.ljvxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class DbClient:

    def __init__(self):
        self.client = MongoClient(config.DATABASE_URL)
        self.db = self.client[config.DATABASE]
        self.collection = self.db[config.COLLECTION]
    
    def addCoupon(self,coupon):
        insertResult = self.collection.insert_one(coupon)
        return insertResult.inserted_id
    
    def getDocuments(self):
        coupons = []
        cursor = self.collection.find()
        for document in cursor:
            coupons.append(document)
        return coupons





