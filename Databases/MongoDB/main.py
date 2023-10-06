from pymongo import MongoClient

# MongoDBに接続する
client = MongoClient("mongodb://localhost:27017/")

# データベースを選択する（存在しない場合、自動的に作成されます）
db = client["mydatabase"]

# コレクション（テーブルのようなもの）を選択または作成
collection = db["mycollection"]

# ドキュメント（レコードのようなもの）を挿入
insert_result = collection.insert_one({"name": "John", "age": 30})
print(f"Inserted document with ID: {insert_result.inserted_id}")

# ドキュメントを検索（全てのドキュメントを取得）
for document in collection.find():
    print(document)

# ドキュメントを検索（条件付き）
for document in collection.find({"name": "John"}):
    print(document)

# ドキュメントを更新
update_result = collection.update_one({"name": "John"}, {"$set": {"age": 31}})
print(f"Matched {update_result.matched_count} and modified {update_result.modified_count} documents")

# ドキュメントを削除
delete_result = collection.delete_one({"name": "John"})
print(f"Deleted {delete_result.deleted_count} documents")
