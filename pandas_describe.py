# -*- coding: utf-8 -*-
# describe()方法


import pandas as pd


df = pd.DataFrame({'A': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'], 'B': [1, 1, 2, 3, 1, 2, 2, 3, 3]})
df.describe()  # 可以使用 to_csv() 后在 Excel 中操作
'''
              B
count  9.000000
mean   2.000000
std    0.866025
min    1.000000
25%    1.000000
50%    2.000000
75%    3.000000
max    3.000000
'''

grouped = df.groupby(['A', ])
grouped.describe()  # 可以使用 to_csv() 后在 Excel 中操作
'''
      B                                          
  count  mean       std  min  25%  50%   75%  max
A                                                
a   4.0  1.75  0.957427  1.0  1.0  1.5  2.25  3.0
b   5.0  2.20  0.836660  1.0  2.0  2.0  3.00  3.0
'''
