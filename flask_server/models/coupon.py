class Coupon:
    def __init__(self,couponCode,startDate,endDate,couponType,minAmount,maxPermissable,idiosyncrasy,active):
        self.couponCode = couponCode
        self.startDate = startDate
        self.endDate = endDate
        self.couponType = couponType
        self.minAmount = minAmount
        self.maxPermissable = maxPermissable
        self.idiosyncrasy = idiosyncrasy
        self.active = active