import db
from db.mongo_client import DbClient

class CouponRepo:

    def __init__(self):
        self.dbClient = DbClient()
    
    def listCoupons(self):
        """
            Return a list of available coupons
        """
        pass

    def addCoupon(self):
        """
            Create a new coupon in the DB
        """
        self.dbClient.addCoupon()

    def validateCoupon(self):
        """
            Validate the given coupn
        """
        pass

    def deleteExpiredCoupons(self):
        """
            Go through the list of coupons and delete the ones that are expired
        """
        pass