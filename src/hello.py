'''
Dockerを用いてpythonを実行する確認のコード
'''

import pandas as pd
df=pd.read_csv("./csv/data.csv")

#print('hello docker python')
print(df)