from datetime import datetime as dt
from dateutil.parser import parse
import uuid


from db.mongo_client import DbClient
from models import Status
import config

class CouponRepo:

    def __init__(self):
        self.dbClient = DbClient()
    
    def listCoupons(self):
        """
            Return a list of available coupons
        """
        return self.dbClient.getDocuments()

    def addCoupon(self,coupon):
        """
            Create a new coupon and insert into the collection.

            CouponId : Type of coupon (Flat/Percentage) - seconds and date - randomly generated 4 characters
        """
        couponCode = "{0}-{1}-{2}".format(chr(coupon.get("type")),dt.strftime(dt.now(),"%S%d"),str(uuid.uuid4()).split('-')[1])
        coupon[config.ID] = couponCode
        coupon[config.ACTIVE] = True
        return self.dbClient.addCoupon(coupon)

    def customResponse(self,amount,status):
        status["amount"] = amount
        return status

    def validateCoupon(self,properties):
        """
            Validate the given coupon and retrun the value that needs to be dedcuted from the total
        """
        coupon = self.dbClient.getDocument(properties["couponCode"])
        if not coupon.active:
            return self.customResponse(0,Status.USED.value)
        if dt.now() > parse(coupon.endDate):
            return self.customResponse(0,Status.EXPIRED.value)
        if properties["cartAmount"] < coupon.minAmount:
            return self.customResponse(0,Status.INELIGIBLE.value)
        self.dbClient.updateDocument(properties["couponCode"],{config.ACTIVE:False})
        if coupon.couponType == 70:
            return self.customResponse(coupon.idiosyncrasy,Status.APPLIED.value)
        if coupon.couponType == 80:
            discount = (coupon.idiosyncrasy / 100) * properties["cartAmount"]
            if discount > coupon.maxPermissable:
                return self.customResponse(coupon.maxPermissable,Status.APPLIED.value)
            else:
                return self.customResponse(discount,Status.APPLIED.value)
        


    def deleteExpiredCoupons(self):
        """
            Go through the list of coupons and delete the ones that are expired
        """
        pass