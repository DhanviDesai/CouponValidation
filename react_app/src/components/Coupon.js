import React from 'react'
import '../App.css'

function Coupon({couponCode,startDate,endDate,couponTypeId,idiosyncrasy,minAmount}) {
  var couponType = -1
  if(couponTypeId == 70){
    couponType = true
  }else{
    couponType = false
  }
  return (
    <div className={couponType?"Coupon flatCoupons":"Coupon percentageCoupons"}>
      <h4>{couponCode}</h4>
      <p>{startDate}-{endDate}</p>
      <p>{idiosyncrasy}</p>
      <p>{minAmount}</p>
    </div>
  )
}

export default Coupon