'''
- csvファイルの中身が突然消えてしまったのでそれの対策のための調査
- 調査内容としてはcsvがからの時にデータを追加するというものにする
'''
import pandas as pd


if __name__=="__main__":
    try:
        df=pd.read_csv('./../csv/empty.csv')
    except:
        df=pd.DataFrame()
        print("空だよ")
        df['id']=[0,1,2]
        df['value']=['プログラミング','読書','散歩']
    print(df)

'''
# 検証結果
- そもそもread_csvの部分でcsvが空になってしまったらerrorになってしまう
- try,exceptを使ってエラーになったらデータフレームに追加する
'''