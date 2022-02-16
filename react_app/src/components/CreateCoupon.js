import React, { useState } from 'react'

function CreateCoupon() {

    const [startDate, setStartDate] = useState("")
    const [endDate, setEndDate] = useState("")
    const [idiosyncrasy, setIdiosyncrasy] = useState("")
    const [minAmount, setMinAmount] = useState("")
    const [maxPermissable, setMaxPermissable] = useState(null)
    const [couponType, setCouponType] = useState("")
    const [couponCode, setCouponCode] = useState("")
    const [flat, setFlat] = useState(false)
    const [percentage, setPercentage] = useState(false)

    const handleStartDate = event => {
        setStartDate(event.target.value)
    }

    const handleEndDate = event => {
        setEndDate(event.target.value)
    }

    const handleIdiosyncrasy = event => {
        setIdiosyncrasy(event.target.value)
    }

    const handleMinAmount = event => {
        setMinAmount(event.target.value)
    }

    const handleMaxPermissable = event => {
        setMaxPermissable(event.target.value)
    }

    const flatSelected = () => {
        setFlat(true)
        setPercentage(false)
    }

    const percentageSelected = () => {
        setPercentage(true)
        setFlat(false)
    }

    const createCoupon = () =>{
        var couponType = flat?70:80
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                'startDate':startDate,
                'endDate':endDate,
                'idiosyncrasy':parseInt(idiosyncrasy),
                'minAmount':parseInt(minAmount),
                'maxPermissable':parseInt(maxPermissable),
                'type':couponType
            })
        };
        fetch('/coupon/add', requestOptions)
            .then(response => response.json())
            .then(result => {
                setCouponCode(result.couponCode)
            }).catch(error => console.log(error))
    }

    const clearForm = () => {
        setFlat(false)
        setPercentage(false)
        setEndDate("")
        setStartDate("")
        setIdiosyncrasy("")
        setMinAmount("")
        setMaxPermissable("")
        setCouponCode("")
    }


  return (
    <div>
        <div className='radioInputOuter'>
            <div className='radioInput' onClick={flatSelected}>
                <input type="radio" name='couponType' value='flat' checked={flat}/>
                <label className='inputPadding' for="flat">Flat</label>
            </div>
            <div className='radioInput' onClick={percentageSelected}>
                <input type="radio" name='couponType' value='percent' checked={percentage}/>
                <label className='inputPadding' for="percent">Percentage</label>
            </div>
        </div>
        <div className='cartAmount'>
            <p>Start date : </p>
            <input type='date' onChange={handleStartDate} value={startDate} />
            <p>End date : </p>
            <input type='date' onChange={handleEndDate} value={endDate} />
        </div>
        <div  className='cartAmount'>
            <p>Minimum amount</p>
            <input type="text" onChange={handleMinAmount} value={minAmount}/>
            <p className={percentage?"displayBlock":"displayNone"}>Max discount amount</p>
            <input className={percentage?"displayBlock":"displayNone"} type="text" onChange={handleMaxPermissable}
            value={maxPermissable}/>
        </div>
        <div  className='cartAmount'>
            <p>{flat?"Flat discount amount":"Discount percentage"}</p>
            <input type="text" onChange={handleIdiosyncrasy} value={idiosyncrasy}/>
        </div>
        <div className={couponCode.length>0?'cartAmount displayBlock':'cartAmount displayNone'}>
            <h4>Newly create coupon code : {couponCode}</h4>
        </div>
            <button className='customButton validateButton' onClick={createCoupon}>Create coupon</button>
            <button className='customButton' onClick={clearForm}>Clear</button>
    </div>
  )
}

export default CreateCoupon