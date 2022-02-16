import React, { useState } from 'react'

function ValidateCoupon() {

    const [cartAmount, setCartAmount] = useState("")

    const [couponCode, setCouponCode] = useState("")

    const [discountAmount, setDiscountAmount] = useState("")

    const [status, setStatus] = useState("")

    const [validateButton,setValidateButton] = useState(true)

    const handleCouponCode = event => {
        setCouponCode(event.target.value)
    }

    const handleCartAmount = event => {
        setCartAmount(event.target.value)
    }

    const validateCoupon = () => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({'cartAmount':parseInt(cartAmount),'couponCode':couponCode})
        };
        fetch('/coupon/validate', requestOptions)
            .then(response => response.json())
            .then(result => {
                setValidateButton(false)
                setDiscountAmount(result.amount)
                setStatus(result.status)
            }).catch(error => console.log(error))
    }

    const clearFields = () => {
        setValidateButton(true)
        setCartAmount("")
        setCouponCode("")
    }

  return (
      <div>
          <div className='cartAmount'>
            <p>Cart amount : </p>
            <input onChange={handleCartAmount} type="text" value={cartAmount} />
        </div>
        <div className='cartAmount'>
            <p>Coupon Code : </p>
            <input onChange={handleCouponCode} type="text" maxLength="11" value={couponCode}/>
        </div>
        <div className={validateButton?'cartAmount displayNone':'cartAmount displayVisible'}>
            <p>Discount amount : </p>
            <input type="text" value={discountAmount}  />
        </div>
        <p className={validateButton?'pushRight displayNone':'pushRight displayVisible'}>{status}</p>
        <button className={validateButton?"customButton validateButton displayVisible":"customButton validateButton displayNone"} onClick={validateCoupon}>Validate coupon</button>
        <button className="customButton displayVisible" onClick={clearFields}>Clear</button>
      </div>    
  )
}

export default ValidateCoupon