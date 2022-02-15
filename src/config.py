import os

PORT = 5000

DATABASE = "CouponDB"
COLLECTION = "coupon"

START_DATE = "startDate"
END_DATE = "endDate"
TYPE = "type"
MIN_AMOUNT = "minAmount"
MAX_PERMISSABLE = "maxPermissable"
IDIOSYNCRASY = "idiosyncrasy"
ACTIVE = "active"
ID = "_id"

DATABASE_URL = os.getenv("MONGO_URL")