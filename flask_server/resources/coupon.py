from flask import request
from flask_restful import Resource
from flask import jsonify


from flask_server.repositories import CouponRepo
import flask_server.config as config

couponRepo = CouponRepo()

class CouponListResource(Resource):
    def get(self):
        result = couponRepo.listCoupons()
        return jsonify({config.COUPONS:result})

class AddCouponResource(Resource):
    def post(self):
        req = request.get_json()
        result = couponRepo.addCoupon(req)
        return jsonify({config.COUPON_CODE:result})

class ValidateCouponResource(Resource):
    def post(self):
        req = request.get_json()
        result = couponRepo.validateCoupon(req)
        return jsonify(result)

class DeleteInactiveCouponsResource(Resource):
    def get(self):
        result = couponRepo.deleteInactiveCoupons()
        return jsonify(result)