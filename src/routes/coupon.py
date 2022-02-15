from flask import Blueprint
from flask_restful import Api
from resources import AddCouponResource,CouponListResource,ValidateCouponResource

COUPON_BLUEPRINT = Blueprint("coupon",__name__)

Api(COUPON_BLUEPRINT).add_resource(AddCouponResource,"/coupon/add")
Api(COUPON_BLUEPRINT).add_resource(CouponListResource,"/coupon/list")
Api(COUPON_BLUEPRINT).add_resource(ValidateCouponResource,"/coupon/validate")