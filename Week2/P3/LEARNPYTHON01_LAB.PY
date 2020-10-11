# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:08:06 2020

@author: quyh2_000
"""
# 导入系统模块，用来处理文件路径
import os
import geopandas as gpd
import matplotlib.pyplot as plt

# 定义文件主目录
# 请补充你的数据文件所在的主目录
homePath = '.'
# 定义一个子目录
subPath = 'ChinaLevelCov'
# 目录拼接，形成一个数据目录字符串
dataPath = os.path.join(homePath, subPath)
# 看当前目录下有哪些文件
files = os.listdir(dataPath)
# nFile表示文件的个数
nFile = len(files)

# 请补充下面的print代码，能够打印出文件所在的子目录名和该目录下总共有多少个文件
print(subPath, nFile)

# 定义一个整型变量，用来记录访问文件的序号（从1开始）
# i = 1
# 对所有文件进行逐个循环，即每次从files里取出一个文件f
shpFile = None
for i, f in enumerate(os.listdir(dataPath)):
    # 写一行代码，能够输出如下信息：第aa个文件的文件名是bb。
    # 其中aa，和bb分别是文件序号和文件名称
    print("第{}个文件的文件名是{}".format(i + 1, f))
    # i += 1 #让i记录当前访问文件的序号（从1开始）
    # 将文件名和文件扩展名分开
    name, ext = os.path.splitext(f)
    # 判断是不是shape类型的文件
    if 'shp' in ext:
        # 如果是，就记录下来，供后面使用
        assert shpFile is None   # 保证shp文件只有一个
        shpFile = f
##写一行代码，将文件列表中文件类型是shape类型的文件名打印出来
print(shpFile)
# 将文件名和文件目录连接起来，形成文件的全名
fullFile = os.path.join(dataPath, shpFile)
# 用geopandas读取shape文件
provinces = gpd.read_file(fullFile)
# 将地图画出来
provinces.plot()
plt.show()

# 定义两个变量，分别对应shape文件的两个列名称
caseColumn = '累计确诊'
nameColumn = 'NAME'
# 定义一个变量，用来计算全国累计确诊病例
allCaseCount = 0
# 定义一个变量，用来保存累计确诊病例数最大数
maxCaseCount = 0
# 定义一个变量，用来保存累计确诊病例最大的省份名称
maxCaseProvince = ''
# 逐个省查看累计确诊病例数
for item in provinces.iterrows():
    inx = item[0]  # 得到每一行的索引号
    data = item[1]  # 得到每一行的数据
    name = data[nameColumn]  # 得到省名
    count = data[caseColumn]  # 得到累计确诊数
    # 写成一行代码，输出每个省的名称和该省的累计确诊病例数
    print("{}累计{}例".format(name, count))
    # 写一行代码，实现对各个省份确诊病例数的累加
    allCaseCount += count
    if count > maxCaseCount:
        maxCaseCount = count
        maxCaseProvince = name

# 写一行代码，输出全国的累计病例数
print("全国:{}例".format(allCaseCount))
# 写一行代码，打印出累计病例最多的省份和累计病例数
print("最多省份：{}，{}例".format(maxCaseProvince, maxCaseCount))
# 写一行代码，计算累计确诊病例最大的省份的病例数占全国累计病例数的比例
print("占全国的{}".format(maxCaseCount/allCaseCount))
# 写一行代码，将上述比例按照百分比输出，小数点保留2位小数
print("即{}%".format(round(maxCaseCount/allCaseCount * 100, 2)))
# 补充以上所有代码以后，运行程序，看看是否能够达到你的预期
