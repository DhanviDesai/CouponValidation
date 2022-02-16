# Coubase - coupon management system

This project is deployed on [Heroku](https://coubase.herokuapp.com).

`Note : coupon codes are generated automatically upon creation of a new coupon. These have to be used to validate the coupons`

## To run locally

Once the project is cloned, install all the necessary requirements using requirements.txt like so

### `pip install -r requirements.txt` 

To connect to MongoDB, set an environment variable with key and value pair as shown

#### `MONGO_URL={mongodb://localhost:27017}|{Mongo Atlas cluster connection string}`

After installation of required packages and once the environment variable is set up. 


App can be run by 
### `python wsgi.py`

This starts running the server on `localhost:5000`. \
This can be viewed on your browser

## Backend

Backend for the application is developed using __Flask Python framework__ .\
All the related code can be found in __flask_server__ package in the application

### APIs

There are 4 available APIs : 

`/coupon/add` - This API is used to create new coupons and store them on the database. The API takes all the necessary details such as (start date, end date, coupon type, discount etc) as a JSON body through __POST__ method. Before inserting, server adds two more keys to the coupon namely __active__ which keeps track of validity of the coupon as well as its previous usage and ___id__ which is a mandatory field for MongoDB, this is used as the coupon code. The method returns newly created __coupon code__ upon successful creation.

`/coupon/list` - This is a __GET__ method which returns all the coupons in the database.

`/coupon/validate` - This is a __POST__ method which takes in the cart amount and the coupon code and returns the amount of discount to be applied if it is applicable. It also returns a __status__ which gives the status of the current coupon transaction.

`/coupon/delete` - This is a __GET__ method which deletes all the inactive coupons in the database. Coupons that are expired or are already used once are considered to be inactive.

## Database

Storing of different coupons is essential for the working of the application.

__MongoDB__ is used as the database for the application.

Application hosted on [Heroku](https://coubase.herokuapp.com) is connected to a __cluster__ on __MongoDB Atlas__



## Frontend

This is implemented using __React js__. All the related code can be found in __react_app__ package in the application.
