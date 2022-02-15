from pymongo import MongoClient
import config

# client = MongoClient("mongodb+srv://dhanvi:1234@cluster0.ljvxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class DbClient:

    def __init__(self):
        self.client = MongoClient(config.DATABASE_URL)
    
    def addCoupon(self):
        dblist = self.client.list_database_names()
        db = self.client[config.DATABASE]
        collection = db[config.COLLECTION]
        coupon = {"_id":"TodaysDate2","startDate":"","endDate":"","type":"FLAT","minAmount":100,"maxPermissable":300}
        print(collection.insert_one(coupon))





