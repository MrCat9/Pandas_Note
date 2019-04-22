# -*- coding: utf-8 -*-

import pymysql
import pandas as pd


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='···',
    passwd='···',
    db='pymysql_test01',
)

sql = 'select * from country'
df = pd.read_sql(sql, conn, index_col='Code')
# print(df)

conn.close()

country_name = df.loc[:, 'Name']
# print(country_name)
population = df.loc[:, 'Population']
# print(population)

big_country = df.loc[(df.loc[:, 'Population'] >= 100000000) & (df.loc[:, 'SurfaceArea'] >= 1000000)]
print(big_country[['Name', 'Population', 'SurfaceArea']])

