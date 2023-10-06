from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("mongodb://localhost:27017/")

# データベースを選択
db = client["mydatabase"]

# コレクションを選択
collection = db["mycollection"]

# 大量のドキュメント（ここでは1000件）を用意
bulk_data = [{"name": f"John_{i}", "age": 30 + i} for i in range(1000)]

print(bulk_data)

# 一括で挿入
insert_result = collection.insert_many(bulk_data)
print(f"Inserted {len(insert_result.inserted_ids)} documents.")
