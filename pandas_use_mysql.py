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


# ================================================================


# 通过ssh连接
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
import pandas as pd


# ================================ MySQL 数据库配置 ================================
ssh_host = '11.22.33.44'  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般是22，必须是数字
ssh_user = 'root'  # 堡垒机上的用户名
ssh_password = 'ssh123456'  # 堡垒机上的用户密码
mysql_host = '127.0.0.1'  # mysql服务器的主机名或ip地址
mysql_port = 3306  # mysql服务器上的端口，mysql一般是3306，必须是数字
mysql_user = 'mysqluser'  # mysql的用户名
mysql_password = '123456'  # mysql的密码
mysql_db = 'db_tmp'  # mysql的数据库名
# ==================================================================================

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)
) as server:
    local_port = str(server.local_bind_port)
    engine = create_engine(
        'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(mysql_user,
                                                             mysql_password,
                                                             '127.0.0.1',
                                                             local_port,
                                                             mysql_db),
        pool_size=100,
        pool_recycle=3600
    )

    sql = 'select `user_id`, `name` from t_user'
    user_df = pd.read_sql(sql, engine, )

