#!/usr/bin/env python
# coding: utf-8

# In[1]
import pandas as pd
import numpy as np
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
# 数据可视化
# 准备
cols = df.columns #为了避免输入列名的汉字，把所有列先取出来
colT = cols[0] #第一列，应该是温度
colP = cols[1]
# In[3]
#下面开始绘折线图
df.plot(kind = 'line', y = colT) #画温度的折线图，默认x是df的索引
# In[4]
#这时，你发现图中的中文变成了乱码，主要原因是画图函数默认字体是西文，需要改为中文字体
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun' #宋体字
#如果你感觉画图的字体太小的话，可以顺便改变图形的字体大小
plt.rcParams['font.size'] = 20

#提示：一般是把上述字体设置代码放在程序的开始处进行设置
# In[5]
#经过上述设置以后，再绘图就不会中文乱码了
df.plot(kind = 'line', y = colT)

# In[6]
#代码填空
# 绘制每个城市的用电量的折线图
df.plot(kind='line', y = colP)
plt.show()
# In[7]
#绘制温度柱状图
df.plot(kind = 'bar', y = colT)

#代码填空
#绘制用电量柱状图
df.plot(kind = 'bar', y = colP)
plt.show()
# In[8]
#同时绘制用电量和温度柱状图
df.plot(kind = 'bar', y = [colT,colP])
#同时绘制用电量和温度柱状图,将电量叠加在温度上面
df.plot(kind = 'bar', y = [colT, colP],stacked = True)

# In[9]
#画散点图，看看用电量与温度之间是不是有线性关系
df.plot(kind = 'scatter', x = colT, y = colP)
#我们看到，随着温度升高，城市用电量也在逐渐增大
# In[10]
# 修改一下点的颜色,符号类型，符号大小。#例如：点是红色，符号是*，大小是80（像素）
size = 80
df.plot(kind = 'scatter', x = colT, y = colP, marker = '*', c = 'r', s = size)

#代码填空
#仿照上面的代码，修改散点图的颜色为黑色，符号类型为^,大小为160
df.plot(kind = 'scatter', x = colT, y = colP, marker='^', c = 'black', s = 160)

# In[11]
#代码填空，思考题：
#如果让点的符号大小不是固定值，让点的尺寸等于城市的用电量增，该怎么修改代码
size = df[colP]
df.plot(kind = 'scatter', x = '城市', y = colP, marker = '^', c = 'k', s = size)
plt.show()

