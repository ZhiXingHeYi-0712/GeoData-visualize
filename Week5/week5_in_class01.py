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
#提取城市名称为"Haila"的城市温度
rows = ['Haila']
cols = ['温度']
selDF = df.loc[rows,cols]

# In[3]:
# 模仿上面的代码，不出能够完整下面的代码
# 提取第二到第六个城市的温度
rows = range(1,6)
cols = [0]
selDF = df.iloc[rows,cols]

#
# # In[4]:
# #提取所有城市的用电量
cols = ['电量']
selDF = df.loc[:, cols]
