import React, {useState,useEffect} from 'react'
import Coupon from './Coupon';
import '../App.css'

function ListCoupon({coupons}) {
    var returnCoupons = []
    coupons.map((coupon,i) => {
        returnCoupons.push(<Coupon key={i} couponCode={coupon._id} couponTypeId={coupon.type} idiosyncrasy={coupon.idiosyncrasy}
        startDate={coupon.startDate} endDate={coupon.endDate} minAmount={coupon.minAmount}/>)
    })
    function deleteInactive(){
        alert("Deleting all the inactive/expired coupons")
        fetch("/coupon/delete",{
            'methods':'GET',
            headers:{
                'Content-Type':'application/json'
            }
        }).then(response => response.json())
        .then(result =>{
            console.log(result)
        }).catch(error => console.log(error))
    }
  return (
      <div>
          <img className='deleteButton' onClick={deleteInactive} alt="svgImg" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4Igp3aWR0aD0iMzg0IiBoZWlnaHQ9IjM4NCIKdmlld0JveD0iMCAwIDE3MiAxNzIiCnN0eWxlPSIgZmlsbDojMDAwMDAwOyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJub256ZXJvIiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWxpbmVjYXA9ImJ1dHQiIHN0cm9rZS1saW5lam9pbj0ibWl0ZXIiIHN0cm9rZS1taXRlcmxpbWl0PSIxMCIgc3Ryb2tlLWRhc2hhcnJheT0iIiBzdHJva2UtZGFzaG9mZnNldD0iMCIgZm9udC1mYW1pbHk9Im5vbmUiIGZvbnQtd2VpZ2h0PSJub25lIiBmb250LXNpemU9Im5vbmUiIHRleHQtYW5jaG9yPSJub25lIiBzdHlsZT0ibWl4LWJsZW5kLW1vZGU6IG5vcm1hbCI+PHBhdGggZD0iTTAsMTcydi0xNzJoMTcydjE3MnoiIGZpbGw9Im5vbmUiPjwvcGF0aD48ZyBmaWxsPSIjZTc0YzNjIj48cGF0aCBkPSJNNzEuNjY2NjcsMTQuMzMzMzNsLTcuMTY2NjcsNy4xNjY2N2gtNDN2MTQuMzMzMzNoMTI5di0xNC4zMzMzM2gtNDNsLTcuMTY2NjcsLTcuMTY2Njd6TTMxLjI4NDE4LDUwLjE2NjY3bDEyLjIwNTczLDEwNy41aDg1LjAyMDE4bDEyLjIwNTczLC0xMDcuNXoiPjwvcGF0aD48L2c+PC9nPjwvc3ZnPg=="/>
          <div className='couponHolder'>{returnCoupons}</div>
      </div>
      
  )
}

export default ListCoupon