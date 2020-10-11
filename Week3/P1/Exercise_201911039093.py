import pandas as pd

def pointToPointDist(x0, y0, x1, y1):
    d = (x0 - x1) ** 2 + (y0 - y1)**2
    dist = d**0.5
    return dist

def readCityXY():
    xlsFile = 'ChinaProvincePoint.xlsx'
    xlsInfo = pd.ExcelFile(xlsFile)
    sheet = xlsInfo.sheet_names[0]
    data = pd.read_excel(xlsInfo, sheet_name=sheet)
    X = list(data['X'])
    Y = list(data['Y'])
    cityNames = list(data['NAME'])
    return cityNames, X, Y

cityNames, X, Y = readCityXY()
xBeiJing = X[0]
yBeiJing = Y[0]

cityCount = len(cityNames)
print('共有城市%d个' % cityCount)

for i in range(1, cityCount):
    dist = pointToPointDist(X[0], Y[0], X[i], Y[i])
    name = cityNames[i]
    print("北京到{}的距离是{}km".format(name, int(dist / 1000)))
print('\n'+'*' * 50+'\n')

j = 1
while j < cityCount:
    dist = pointToPointDist(X[0], Y[0], X[j], Y[j])
    name = cityNames[j]
    print("北京到{}的距离是{}km".format(name, int(dist / 1000)))
    j += 1

