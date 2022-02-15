from pymongo import MongoClient
import json
from flask import jsonify


import config
from models import Coupon

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
    
    def getDocument(self,couponCode):
        coupon = self.collection.find_one({config.ID:couponCode})
        return Coupon(coupon[config.ID],coupon[config.START_DATE],coupon[config.END_DATE],coupon[config.TYPE],coupon[config.MIN_AMOUNT],coupon[config.MAX_PERMISSABLE],coupon[config.IDIOSYNCRASY],coupon[config.ACTIVE])

    def updateDocument(self,couponCode,newValue):
        condition = {config.ID:couponCode}
        self.collection.update_one(condition,{"$set":newValue})





