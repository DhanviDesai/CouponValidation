import json
from flask_restful import Resource
from flask import jsonify
from repositories import CouponRepo

couponRepo = CouponRepo()

class CouponListResource(Resource):
    def get(self):
        result = couponRepo.listCoupons()
        return jsonify({"data":result})

class AddCouponResource(Resource):
    def post(self):
        result = couponRepo.addCoupon()
        return jsonify(result)

class ValidateCouponResource(Resource):
    def post(self):
        result = couponRepo.validateCoupon()
        return jsonify(result)