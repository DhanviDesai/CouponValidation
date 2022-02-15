import os

PORT = 5000

DATABASE = "CouponDB"
COLLECTION = "coupon"

DATABASE_URL = os.getenv("MONGO_URL")