import enum
class Status(enum.Enum):
    EXPIRED = {"status":"Coupon expired"}
    USED = {"status":"Coupon already used"}
    APPLIED = {"status":"Coupon applied!"}
    INELIGIBLE = {"status":"Minimum not reached"}