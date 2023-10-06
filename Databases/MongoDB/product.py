from pymongo import MongoClient
from statistics import mean

# MongoDBに接続
client = MongoClient("mongodb://localhost:27017/")
db = client["productDB"]
collection = db["products"]

# 商品とレビューを追加
product_1 = {
    "name": "Laptop",
    "category": "Electronics",
    "reviews": [
        {"user": "Alice", "rating": 8},
        {"user": "Bob", "rating": 7},
        {"user": "Charlie", "rating": 9},
    ],
}

product_2 = {
    "name": "Coffee Maker",
    "category": "Home Appliances",
    "reviews": [
        {"user": "Alice", "rating": 10},
        {"user": "Dave", "rating": 6},
    ],
}

# ドキュメントを挿入
collection.insert_many([product_1, product_2])

# 商品に対する平均評価を計算
for product in collection.find({}, {"_id": 0, "name": 1, "reviews.rating": 1}):
    name = product["name"]
    ratings = [review["rating"] for review in product.get("reviews", [])]
    avg_rating = mean(ratings) if ratings else "No reviews yet"
    print(f"The average rating of {name} is {avg_rating}")

# 柔軟なスキーマを活用して新たなフィールドを追加
collection.update_one({"name": "Laptop"}, {"$set": {"stock": 5}})

# ストック情報を表示
for product in collection.find({}, {"_id": 0, "name": 1, "stock": 1}):
    name = product["name"]
    stock = product.get("stock", "Stock information not available")
    print(f"The stock for {name} is {stock}")
