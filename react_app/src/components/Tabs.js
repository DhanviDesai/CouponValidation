import { useState } from "react";
import "../App.css";
import ListCoupon from "./ListCoupon";
import ValidateCoupon from "./ValidateCoupon";

function Tabs() {
  const [toggleState, setToggleState] = useState(1);
  const [coupons,setCoupons] = useState([]);

  const toggleTab = (index) => {
    setToggleState(index);
    if(index == 3){
        fetchCoupons()
    }
  };

  const fetchCoupons = () => {
    fetch("/coupon/list",{
        'methods':'GET',
        headers:{
            'Content-Type':'application/json'
        }
    }).then(response => response.json())
    .then(result => {
        setCoupons(result.coupons)
    }).catch(error => console.log(error))
  }

  return (
    <div className="Background">
      <div className="bloc-tabs">
        <button
          className={toggleState === 1 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(1)}
        >
          VALIDATE
        </button>
        <button
          className={toggleState === 2 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(2)}
        >
          CREATE
        </button>
        <button
          className={toggleState === 3 ? "tabs active-tabs" : "tabs"}
          onClick={() => toggleTab(3)}
        >
          LIST
        </button>
      </div>

      <div className="content-tabs">
        <div
          className={toggleState === 1 ? "content  active-content" : "content"}
        >
         <ValidateCoupon /> 
        </div>

        <div
          className={toggleState === 2 ? "content  active-content" : "content"}
        >
          
        </div>

        <div
          className={toggleState === 3 ? "content  active-content" : "content"}
        >
            <ListCoupon coupons={coupons}/>
          
        </div>
      </div>
    </div>
  );
}

export default Tabs;