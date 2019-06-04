# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# pandas 的索引建议使用 .loc .iloc .at .iat

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print('='*64)
print(df.at[dates[0], 'A'])  # 第一行第A列
print('='*64)
print(df.loc[dates[1]])  # 第二行
print('='*64)
print(df.loc[:, ['A', 'B']])  # 每一行的A,B列
print('='*64)
print(df.loc[(df.loc[:, 'A'] >= 0) & (df.loc[:, 'B'] >= 0)])  # 每一行中 A,B列值均大于0的 行

