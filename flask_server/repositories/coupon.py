from datetime import datetime as dt
from dateutil.parser import parse
import uuid


from db import DbClient
from models import Status
import config as config

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
        couponCode = "{0}-{1}-{2}".format(chr(coupon.get(config.TYPE)),dt.strftime(dt.now(),"%S%d"),str(uuid.uuid4()).split('-')[1])
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
        coupon = self.dbClient.getDocument(properties[config.COUPON_CODE])
        if coupon is None:
            return self.customResponse(0,Status.INVALID.value)
        if dt.now() > parse(coupon.endDate):
            self.dbClient.updateDocument(properties[config.COUPON_CODE],{config.ACTIVE:False})
            return self.customResponse(0,Status.EXPIRED.value)
        if not coupon.active:
            return self.customResponse(0,Status.USED.value)
        if properties[config.CART_AMOUNT] < coupon.minAmount:
            return self.customResponse(0,Status.INELIGIBLE.value)
        self.dbClient.updateDocument(properties[config.COUPON_CODE],{config.ACTIVE:False})
        if coupon.couponType == 70:
            return self.customResponse(coupon.idiosyncrasy,Status.APPLIED.value)
        if coupon.couponType == 80:
            discount = (coupon.idiosyncrasy / 100) * properties[config.CART_AMOUNT]
            if discount > coupon.maxPermissable:
                return self.customResponse(coupon.maxPermissable,Status.APPLIED.value)
            else:
                return self.customResponse(discount,Status.APPLIED.value)
        


    def deleteInactiveCoupons(self):
        """
            Go through the list of coupons and delete the ones that are expired
        """
        self.dbClient.deleteInactiveDocuments()
        return True