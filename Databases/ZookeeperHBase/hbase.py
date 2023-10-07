import happybase

# HBaseサーバーに接続
connection = happybase.Connection('localhost', autoconnect=False)
connection.open()

# テーブルを作成
table_name = 'my_table'
families = {
    'cf1': dict(),  # 列族 cf1
    'cf2': dict()   # 列族 cf2
}

connection.create_table(table_name, families)

# テーブルオブジェクトを取得
table = connection.table(table_name)

# データを挿入
table.put('row1', {'cf1:col1': 'value1', 'cf2:col2': 'value2'})

# データを取得
row = table.row('row1')
print("Row data:", row)

# 接続を閉じる
connection.close()
