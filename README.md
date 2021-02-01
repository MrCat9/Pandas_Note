# Pandas_Note

pandas 官网  http://pandas.pydata.org/

## 目录

#### [1_pandas索引](https://github.com/MrCat9/Pandas_Note/blob/master/pandas_loc.py)

#### [2_pandas读MySQL](https://github.com/MrCat9/Pandas_Note/blob/master/pandas_use_mysql.py)

#### 3_DataFrame.apply、merge、rename、drop_duplicates

DataFrame.apply、merge、rename，数据预处理、DataFrame.drop_duplicates去重    DataFrame合并、对Series或DataFrame去重  https://blog.csdn.net/weixin_42398658/article/details/82936185

Series和DataFrame都有drop_duplicates，但两者有点不一样（可传入的参数不一样）

#### 4_DataFrame.merge

https://blog.csdn.net/qq_21840201/article/details/80727504

#### 5_DataFrame排序

Pandas之排序函数sort_values()  https://blog.csdn.net/MsSpark/article/details/83154128

#### 6_fillna处理空值

处理DataFrame中的空值  https://www.cnblogs.com/sunbigdata/p/7895295.html

#### 7_dropna去除空值

删除DataFrame中值全为NaN或者包含有NaN的列或行  https://blog.csdn.net/erinapple/article/details/80729726

#### 8_DataFrame的基本操作

DataFrame基本操作  两个DataFrame的合并  contact  append  merge  https://blog.csdn.net/weixin_38285131/article/details/82258131

#### 9_read_csv

pandas.read_csv参数整理  https://www.cnblogs.com/datablog/p/6127000.html

#### 10_DataFrame转dict

https://blog.csdn.net/m0_37804518/article/details/78444110

```python
population_data = pd.read_csv('population.csv', encoding='GBK', header=None, names=['省市', '人口数'])  # DataFrame
population_dict = population_data.set_index('省市').T.to_dict('list')  # dict  # set_index() 设置索引
```

#### 11_DataFrame, Series, ndarray, list, dict, tuple的相互转换

https://blog.csdn.net/lambsnow/article/details/78517340


#### 12_DataFrame的创建

https://www.cnblogs.com/datasnail/p/9675410.html

#### 13_DataFrame增删改查

https://www.cnblogs.com/lizm166/p/10132535.html

#### 14_HDF5文件

```python
df.to_hdf(path_or_buf, key, **kwargs)
pd.read_hdf(path_or_buf, key=None, mode="r", **kwargs)
```

https://www.cnblogs.com/abella/p/11125466.html

https://blog.csdn.net/mzpmzk/article/details/89188968

#### [15_DataFrame的groupby和agg](https://github.com/MrCat9/Pandas_Note/blob/master/df_groupby_agg.py)

https://blog.csdn.net/weixin_38168620/article/details/82149197

https://www.cnblogs.com/vczh/p/6746935.html

#### 16_DataFrame进行groupby后求众数mode

https://blog.csdn.net/yvettre/article/details/79726396

https://blog.csdn.net/u012735708/article/details/84542326

#### [17_describe方法](https://github.com/MrCat9/Pandas_Note/blob/master/pandas_describe.py)

```
生成统计值，可以进行数据概览。
生成的统计值包括： count, mean, std, min, 25%, 50%, 75%, max
```

#### 18_对pandas中的字符串str处理

https://www.cnblogs.com/P--K/p/11148250.html

#### 19_巧用DataFrame布尔索引的方法删除特定行或列

https://blog.csdn.net/sigtem/article/details/81735242

#### 19_sample随机抽样

https://www.cnblogs.com/webRobot/p/11484648.html

#### 20_报错"ValueError: Cannot mask with non-boolean array containing NA / NaN values"

```python
# df['sub_name'].str.contains('bee').unique()  # 发现有空的行
df = df[df['sub_name'].notnull()]  # 去掉 sub_name 为空的行
bee_df = df[df['sub_name'].str.contains('bee')]
```

https://blog.csdn.net/Guo_ya_nan/article/details/81021158

#### 21_DataFrame显示值省略的解决方法

```python
pd.set_option('max_colwidth',200)
```

#### 22_melt

```
宽数据 -> 长数据
```

Pandas的melt的使用 https://blog.csdn.net/maymay_/article/details/80039677

#### 23_将df中的两列转为元组tuple的列表list

`[(1a, 1b), (2a, 2b), ...]`

```python
r = list(zip(df['col1'], df['col2']))
```

####  24_将df转为html中的table的源码

```python
html_table_str = df.to_html()
word = '关键字'
html_table_str = html_table_str.replace(f'{word}', f'<span style="color: red">{word}</span>')  # 关键字加红
html_table_str = html_table_str.replace(r'\n', '<br>')  # 换行
html_table_str = html_table_str.replace(r'\t', '    ')  # 制表符
with open('df.html', 'w') as f:
    f.write(html_table_str)
```

####                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     25_`pandas.read_excel`读`xlsx`和`xlsm`

`pandas==1.1.5`无法使用默认的引擎`xlrd`读`xlsx`和`xlsm`，会报错`xlrd.biffh.XLRDError: Excel xlsx file; not supported`。需选择引擎为`openpyxl`。

```python
import pandas as pd

fp = 'file_path'
ff = fp[fp.rfind('.') + 1:]  # file_format 文件格式
ff = ff.lower()
if ff == 'xls':
	df = pd.read_excel(fp)
elif ff == 'xlsx':
	df = pd.read_excel(fp, engine='openpyxl')
elif ff == 'xlsm':
	df = pd.read_excel(fp, engine='openpyxl')
else:
	raise ('unknown file format')
```












