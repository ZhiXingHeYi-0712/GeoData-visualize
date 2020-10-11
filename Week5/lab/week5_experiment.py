import pandas as pd
import matplotlib.pyplot as plt


def simplifyProvinceName(name: str) -> str:
    '''
        返回省份的简化名称
        :param name 原名，例如：新疆维吾尔自治区
        :return 简化名，例如：新疆
    '''
    if '自治区' in name:
        # 自治区类，按字典一个个处理，免除一个个if-else的麻烦
        return {
            '广西壮族自治区': '广西',
            '内蒙古自治区': '内蒙古',
            '宁夏回族自治区': '宁夏',
            '西藏自治区': '西藏',
            '新疆维吾尔自治区': '新疆'
        }[name]
    elif '特别行政区' in name:
        # 这句是删掉“特别行政区”
        return name.replace('特别行政区', '')
    else:
        # 删掉省市
        return name.replace('省', '').replace('市', '')


# %matplotlib inline
plt.rcParams['font.family'] = 'SimSun'
file = pd.ExcelFile('Covid2019.xlsx')

dfCases: pd.DataFrame = pd.read_excel(file, file.sheet_names[0])
dfMoving: pd.DataFrame = pd.read_excel(file, file.sheet_names[1])

index_province = '省份'
index_new_cases = '新增确诊'
index_moving = '迁移指数'
index_province_simplify = 'index_province_simplify'

dfMoving.set_index(index_province, inplace=True)
date0314DF = dfCases.query('date == 20200314')
date0314DF.set_index(index_province, inplace=True)

# 查询字符串，利用了列表解析的写法
# 实际上
# '省份.str.find("湖北") < 0 and 省份.str.find("香港") < 0 and 省份.str.find("澳门") < 0 and 省份.str.find("台湾") < 0'
queryString = ' and '.join(['省份.str.find("{}") < 0'.format(i) for i in ['湖北', '香港', '澳门', '台湾']])
date0314DF_remove = date0314DF.query(queryString, engine='python')
dfMoving_remove = dfMoving.query(queryString, engine='python')

# 画条形图
date0314DF_remove.plot(kind='bar', y=index_new_cases)
plt.show()

# 画折线图
# 这一行是在做省份名字的简化，看不懂跳过吧，知道dfMoving_remove有一列index_province_simplify是简化的省份名就好
dfMoving_remove[index_province_simplify] = list(map(simplifyProvinceName, dfMoving_remove.index))

#画图，指定了x，y， rot=90是说x轴的标签逆时针旋转90度
dfMoving_remove.plot(kind='line', x=index_province_simplify, y=index_moving, rot=90)
plt.show()

# 合并
df_merge = dfMoving_remove.join(date0314DF_remove)

# 也是简化
df_merge[index_province_simplify] = list(map(simplifyProvinceName, df_merge.index))

# 画第一张图，存下来。注意这里因为要指定x轴内容，而之前已经把省份设置成了索引没法获取到，因此要先执行reset_index()重置，然后画图。
# plot.scatter和plot(kind='scatter')是同等的。
# 要记得存成变量
ax = df_merge.reset_index().plot.scatter(x=index_province_simplify, y=index_new_cases, c='r', label=index_new_cases, rot=60)
# 画第二张图，注明参数ax=ax, 前一个ax是指明传入哪个参数，后一个ax是变量名。具体参考关键字参数。
# 这样叠图就完成了。同样旋转60度。
df_merge.reset_index().plot.scatter(x=index_province_simplify, y=index_moving, c='b', ax=ax, label=index_moving, rot=60)
#画出来，大功告成！
plt.show()
