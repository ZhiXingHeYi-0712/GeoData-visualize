import pandas as pd
import matplotlib.pyplot as plt


def simplifyProvinceName(name: str) -> str:
    if '自治区' in name:
        return {
            '广西壮族自治区': '广西',
            '内蒙古自治区': '内蒙古',
            '宁夏回族自治区': '宁夏',
            '西藏自治区': '西藏',
            '新疆维吾尔自治区': '新疆'
        }[name]
    elif '特别行政区' in name:
        return name.replace('特别行政区', '')
    else:
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

queryString = ' and '.join(['省份.str.find("{}") < 0'.format(i) for i in ['湖北', '香港', '澳门', '台湾']])
date0314DF_remove = date0314DF.query(queryString, engine='python')
dfMoving_remove = dfMoving.query(queryString, engine='python')
date0314DF_remove.plot(kind='bar', y=index_new_cases)
plt.show()
dfMoving_remove.plot(kind='line', y=index_moving)
plt.show()
df_merge = dfMoving_remove.join(date0314DF_remove)
# df_merge['index'] = range(1, len(df_merge) + 1)
# df_merge.set_index('index', inplace=True)
# df_merge.plot(kind='scatter', x = df_merge.index, y = [index_new_cases, index_moving])
df_merge[index_province_simplify] = list(map(simplifyProvinceName, df_merge.index))
ax = df_merge.reset_index().plot.scatter(x=index_province_simplify, y=index_new_cases, c='r', label=index_new_cases, rot=60)
df_merge.reset_index().plot.scatter(x=index_province_simplify, y=index_moving, c='b', ax=ax, label=index_moving, rot=60)
plt.show()
