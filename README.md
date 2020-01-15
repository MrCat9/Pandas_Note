# Pandas_Note

pandas 官网  http://pandas.pydata.org/

## 目录

#### 1_pandas索引

#### 2_pandas读MySQL

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





