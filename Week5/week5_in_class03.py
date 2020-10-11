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

# In[2]:
# 字符串查询
# 查询城市名称以'H'开头的数据
targetC = 'H'
strQuery = 'index.str.startswith("{}")'.format(targetC)
selDF = df.query(strQuery, engine='python')
print(selDF)

# In[3]:
# 字符串查询

# 查询城市名称不以'H'开头的数据
targetC = 'H'
strQuery = 'not index.str.startswith("{}")'.format(targetC)
selDF = df.query(strQuery, engine='python')
print(selDF)

# In[4]:
# 字符串查询
# 仿照上面的代码，查询城市名称不包含字母'e'且温度大于30度的数据
targetC = 'e'
targetT = 30
strQuery = 'index.str.find("{}") < 0 and 温度 > 30'.format(targetC)
selDF = df.query(strQuery, engine='python')
print(selDF)


