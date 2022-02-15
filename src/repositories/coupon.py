from datetime import datetime as dt
import uuid


from db.mongo_client import DbClient

class CouponRepo:

    def __init__(self):
        self.dbClient = DbClient()
    
    def listCoupons(self):
        """
            Return a list of available coupons
        """
        pass

    def addCoupon(self,coupon):
        """
            Create a new coupon in the DB
        """
        couponCode = "{0}-{1}-{2}".format(chr(coupon.get("type")),dt.strftime(dt.now(),"%S%d"),str(uuid.uuid4()).split('-')[1])
        coupon["_id"] = couponCode
        return self.dbClient.addCoupon(coupon)

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