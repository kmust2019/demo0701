# 导入selenium和time库
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个浏览器对象
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://y.qq.com/n/ryqq/toplist/27")
driver.maximize_window()

# 创建一个空列表，用于存储结果
result = []
# 找到所有的歌曲列表项
items = (driver.find_element(By.CLASS_NAME, "songlist__list")).find_elements(By.TAG_NAME,'li')
# 遍历每个列表项
for item in items:
    # 找到排名上升的图标
    icon = (item.find_element(By.CLASS_NAME,'songlist__rank')).find_element(By.TAG_NAME,'i')
    # 如果存在该图标，说明该歌曲排名上升
    if icon.get_attribute('class') == 'icon_rank_up':
        # 找到歌曲名和演唱者
        song_name = item.find_element(By.CLASS_NAME, "songlist__songname_txt").text.strip()
        singer = item.find_element(By.CLASS_NAME, "songlist__artist").text.strip()
        # 将歌曲名和演唱者添加到结果列表中
        result.append((song_name, singer))

print(result)
driver.quit()


# from selenium import webdriver
# wd = webdriver.Chrome()
# wd.implicitly_wait(5)
# wd.get('https://y.qq.com/n/ryqq/toplist/27')
#
# elements = (wd.find_element_by_class_name('songlist__list')).find_elements_by_tag_name('li')#所有歌曲
# for element in elements:
#     rank = (element.find_element_by_class_name('songlist__rank')).find_element_by_tag_name('i')
#     if rank.get_attribute('class') == 'icon_rank_up':
#         song = element.find_element_by_class_name('songlist__songname_txt')#上升 歌曲名
#         name = element.find_element_by_class_name('songlist__artist')#上升 歌手名
#         print(f'{song.text:20}： {name.text}')

