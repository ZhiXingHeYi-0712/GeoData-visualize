#!/usr/bin/env python
# coding: utf-8

# In[1]
import pandas as pd
T = [ 20, 30, 35, 18, 22, 25]
P = [ 300, 460, 580, 280, 350, 370]
C= ['hailun', 'Beiku', 'Haiqi', 'Genhe', 'Haila', 'Binhe']
df = pd.DataFrame()
df['温度'] = T
df['电量'] = P
df['城市'] = C
df.set_index('城市',inplace = True)#将列名转换为索引
#提示：set_index函数传递了一个新的参数，inplace 
# inplace 为一个布尔型变量，可以取True或False。 
# True表示是原位转换（即改变原始的DataFrame），False表示新生成一个DataFrame，（不改变原来DataFrame）

# In[2]:
#查询温度大于30度的所有数据
#第一步：设置目标参数，即要查询的数值
targetT = 30
#第二步：构建一个查询字符串，回忆一下format函数
strQuery = '温度 > {}'.format(targetT) 
#第三步：调用query函数进行查询
selDF = df.query(strQuery)
print(selDF)
# In[3]
# 查询温度大于等于20度且小于30度的数据
targetT0 = 20
targetT1 = 30
strQuery = '温度 >= {} and 温度 < {}'.format(targetT0, targetT1) 
selDF = df.query(strQuery)
print(selDF)

# In[3]
# 模仿上面的示例，查询用大于电量300且温度低于25度的城市数据
targetP = 300
targetT = 25
strQuery = '电量 > {} and 温度 < {}'.format(targetP, targetT)
selDF = df.query(strQuery)
print(selDF)

