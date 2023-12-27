
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/jsweather.html')
info = wd.find_element(By.ID, 'forecastID')
citysWeather = info.text.split('℃\n')
# 定义一个字典，key 为城市，value为 该城市对应的低温数值
city_temp = {}
# 遍历列表
for city in citysWeather:
  # 用换行符分割城市和温度
  name, temp = city.split('\n')
  # 分割低温 ，高温
  low, high = temp.split('/')
  # 去掉温度后面的摄氏度符号
  low = low[:-1]
  low = float(low)
  # 把城市和对应的温度添加到字典中
  city_temp[name] = low

# 找出所有城市气温中的最低值
min_temp = min(city_temp.values())
# 遍历字典元素，如果城市气温 等于 最低温度，将该城市加入名单中
min_cities = [name for name, temp in city_temp.items() if temp == min_temp]

print(f'温度最低的城市有{len(min_cities)}个，它们是{", ".join(min_cities)}，它们的最低温度是{min_temp}℃。')
wd.quit()


