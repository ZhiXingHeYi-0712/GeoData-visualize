import geopandas as gpd

from math import sqrt


def get_geo_xy(loc_name: str) -> tuple:
    """ 获取loc_name的坐标 """
    baidu_key = '7CV7c9h3RjzuvuA6LArDVj3sCa1eFsL9'  # 用百度的服务来解析
    provider = 'Baidu'
    loc = gpd.tools.geocode(loc_name, provider=provider, api_key=baidu_key)  # 查询得到地理位置的经纬度坐标（球面坐标，单位为度）,并转化为浮点型数据类型
    loc_xy = loc.to_crs(epsg=3395)
    x = float(loc_xy['geometry'].x)
    y = float(loc_xy['geometry'].y)
    return x, y


def get_distance(point1: tuple, point2: tuple) -> float:
    """ 获取两点间距离，单位米 """
    print(point1)
    print(point2)
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


home = get_geo_xy('广东省深圳市地王大厦')
school = get_geo_xy('广东省珠海市北京师范大学珠海校区')
print(get_distance(home, school) // 1000, "千米")
