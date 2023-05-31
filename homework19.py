import json

json_data = '''[
    {"device": "iphone", "price": 3000, "count": null}, 
    {"device": "samsung", "price": 2500, "count": 3},
    {"device": "xiaomi", "price": 2100, "count": null},
    {"device": "nokia", "price": 1800, "count": 4}
]'''
# First solution
python_data = json.loads(json_data)

# prices = sum([datas["price"] * datas["count"] for datas in python_data if datas["count"] != None])

# print(prices)

# Second solution
prices = 0
for datas in python_data:
    if datas["count"] != None:
        prices += datas["price"] * datas["count"]
print(prices)