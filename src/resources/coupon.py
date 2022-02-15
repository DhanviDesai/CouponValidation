from flask import request
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
        req = request.get_json()
        result = couponRepo.addCoupon(req)
        return jsonify({"couponCode":result})

class ValidateCouponResource(Resource):
    def post(self):
        result = couponRepo.validateCoupon()
        return jsonify(result)