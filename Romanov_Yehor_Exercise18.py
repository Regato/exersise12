# Importing json library:
import json

# Variables with prices and stocks:
price_form = 0
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}


# Input data: what user need to buy?
input_list = input('To buy any fruits: Enter fruit names in the list:')
json_list = json.loads(input_list)


# Counting price and fruits amounts:
for i in json_list:
    if stock.get(i) > 0:
        price_form += prices.get(i)
        stock_form = stock.get(i) - 1
        stock.update({i: stock_form})


# Output of program:
print('Price is:', price_form,'\n','Amount of fruits:', stock)