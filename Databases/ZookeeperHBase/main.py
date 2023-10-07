import happybase

# HBaseサーバーへの接続を開設（ローカルホストと仮定）
connection = happybase.Connection('localhost')

# テーブルを作成（既に存在する場合はこの部分をコメントアウト）
connection.create_table('my_table', {'cf1': dict()})

# テーブルを選択
table = connection.table('my_table')

# データを書き込む
table.put('row1', {'cf1:col1': 'value1'})
table.put('row2', {'cf1:col2': 'value2'})

# データを読む
row = table.row('row1')
print("Read data: ", row)

# すべてのデータを読む
for key, data in table.scan():
    print(key, data)

# 接続を閉じる
connection.close()
