""" 根据地名获取该地方对应的经纬度 所用到的地理服务是百度地理编码服务 需要使用到一个百度开发Key，目前是我的个人Key 同学可以自行申请自己的开发Key 申请网址：http://lbsyun.baidu.com/apiconsole/key#/home """
import geopandas as gpd # 测试地理编码功能

baiduKey = '7CV7c9h3RjzuvuA6LArDVj3sCa1eFsL9' # 用百度的服务来解析
provider = 'Baidu'
locName = '广东省深圳市'
loc = gpd.tools.geocode(locName, provider=provider, api_key=baiduKey)
#查询得到地理位置的经纬度坐标（球面坐标，单位为度）,并转化为浮点型数据类型
lon = float(loc['geometry'].x)
lat = float(loc['geometry'].y)
outString = '地点：{} 经纬度坐标是:经度:{:.5f}，纬度:{:.5f}'.format(locName, lon, lat)
print(outString) #将球面坐标（经纬度）转化为平面坐标（X,Y,单位为米）
#将球面坐标系统转换为平面坐标系统，这里使用的是代码为3395的坐标系--墨卡托投影
locXY = loc.to_crs(epsg = 3395)
X_1 = float(locXY['geometry'].x)
Y_1 = float(locXY['geometry'].y)
outString = '地点：{} 地理坐标是:X = {:.5f}，Y = {:.5f}'.format(locName, X_1, Y_1)
print(outString)

baiduKey = '7CV7c9h3RjzuvuA6LArDVj3sCa1eFsL9' # 用百度的服务来解析
provider = 'Baidu'
locName = '广东省珠海市北京师范大学珠海校区'
loc = gpd.tools.geocode(locName, provider=provider, api_key=baiduKey)
#查询得到地理位置的经纬度坐标（球面坐标，单位为度）,并转化为浮点型数据类型
lon = float(loc['geometry'].x)
lat = float(loc['geometry'].y)
outString = '地点：{} 经纬度坐标是:经度:{:.5f}，纬度:{:.5f}'.format(locName, lon, lat)
print(outString) #将球面坐标（经纬度）转化为平面坐标（X,Y,单位为米）
#将球面坐标系统转换为平面坐标系统，这里使用的是代码为3395的坐标系--墨卡托投影
locXY = loc.to_crs(epsg = 3395)
X_2 = float(locXY['geometry'].x)
Y_2 = float(locXY['geometry'].y)
outString = '地点：{} 地理坐标是:X = {:.5f}，Y = {:.5f}'.format(locName, X_2, Y_2)
print(outString)
a = (X_1 - X_2) ** 2 + (Y_1 - Y_2) ** 2
d = a ** 0.5
print(d)
