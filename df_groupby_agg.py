# -*- coding: utf-8 -*-
# pandas DataFrame 的 groupby 和 agg


import pandas as pd


df = pd.DataFrame({'A': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'], 'B': [1, 1, 2, 3, 1, 2, 2, 3, 3]})

df
'''
   A  B
0  a  1
1  a  1
2  a  2
3  a  3
4  b  1
5  b  2
6  b  2
7  b  3
8  b  3
'''

# 用 A 的值进行分组，
# 对每个组内 B 的值求：
#     1. mean，结果命名为 my_name1；
#     2. std，结果命名为 my_name2
df.groupby('A').agg({'B': [('my_name1', 'mean'), ('my_name2', 'std')]})
'''
         B          
  my_name1  my_name2
A                   
a     1.75  0.957427
b     2.20  0.836660
'''

df.groupby('A')['B'].agg([('my_name1', 'mean'), ('my_name2', 'std')])
'''
   my_name1  my_name2
A                    
a      1.75  0.957427
b      2.20  0.836660
'''

# 不指定 B，就是对每个特征做处理
df.groupby('A').agg([('my_name1', 'mean'), ('my_name2', 'std')])
'''
         B          
  my_name1  my_name2
A                   
a     1.75  0.957427
b     2.20  0.836660
'''
