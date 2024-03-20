'''
- csvファイルの中身が突然消えてしまったのでそれの対策のための調査
- 調査内容としてはcsvがからの時にデータを追加するというものにする
'''
import pandas as pd
import csv


if __name__=="__main__":
    path='./../csv/empty.csv'
    try:
        df=pd.read_csv(path)
    except:
        print("空だよ")
        sub_id=[0,1,2]
        sub_data=[['プログラミング'],['読書'],['散歩']]
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i, row in zip(sub_id, sub_data):
                writer.writerow([i]+row)
        df=pd.read_csv(path)
    print(df)

'''
# 検証結果
- そもそもread_csvの部分でcsvが空になってしまったらerrorになってしまう
- try,exceptを使ってエラーになったらデータフレームに追加する
'''