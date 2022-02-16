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
      <h3>{couponCode}</h3>
      <p>Validity : {startDate}-{endDate}</p>
      <p>Discount : {idiosyncrasy}{couponType? "/-" : "%"}</p>
      <p>Minimum amount : {minAmount}/-</p>
    </div>
  )
}

export default Coupon