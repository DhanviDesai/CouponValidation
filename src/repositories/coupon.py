import db

class CouponRepo:
    
    def listCoupons(self):
        """
            Return a list of available coupons
        """
        pass

    def addCoupon(self):
        """
            Create a new coupon in the DB
        """
        pass

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