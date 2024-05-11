# Project 0

#### Link to Project is [Project 0](https://inst.eecs.berkeley.edu/~cs188/sp23/projects/proj0/https://inst.eecs.berkeley.edu/~cs188/sp23/projects/proj0/)

## Q1: Addition 

## Q2: buyLotsOfFruit function 

#### Implement the buyLotsOfFruit(orderList) function in buyLotsOfFruit.py which takes a list of (fruit,numPounds) tuples and returns the cost of your list. If there is some fruit in the list which doesn’t appear in fruitPrices it should print an error message and return None. Please do not change the fruitPrices variable.

#### Run python autograder.py until question 2 passes all tests and you get full marks. Each test will confirm that buyLotsOfFruit(orderList) returns the correct answer given various possible inputs. For example, test_cases/q2/food_price1.test tests whether:

#### Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25

## Q3: shopSmart function

#### Fill in the function shopSmart(orderList,fruitShops) in shopSmart.py, which takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder) and a list of FruitShop and returns the FruitShop where your order costs the least amount in total. Don’t change the file name or variable names, please. Note that we will provide the shop.py implementation as a “support” file, so you don’t need to submit yours.

#### test_cases/q3/select_shop1.test tests whether: shopSmart.shopSmart(orders1, shops) == shop1

#### and test_cases/q3/select_shop2.test tests whether: shopSmart.shopSmart(orders2, shops) == shop2
