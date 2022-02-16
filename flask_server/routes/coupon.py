from flask import Blueprint
from flask_restful import Api
from flask_server.resources import AddCouponResource,CouponListResource,ValidateCouponResource,DeleteInactiveCouponsResource

COUPON_BLUEPRINT = Blueprint("coupon",__name__)

Api(COUPON_BLUEPRINT).add_resource(AddCouponResource,"/coupon/add")
Api(COUPON_BLUEPRINT).add_resource(CouponListResource,"/coupon/list")
Api(COUPON_BLUEPRINT).add_resource(ValidateCouponResource,"/coupon/validate")
Api(COUPON_BLUEPRINT).add_resource(DeleteInactiveCouponsResource,"/coupon/delete")