# 登录 51job ，
# http://www.51job.com
#
# 输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉），
# 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
#
# Python高级开发工程师 | 03-23发布 | 1.5-2万/月 | 欧睿恒（大连）信息技术有限公司
# Python开发工程师 | 03-23发布 | 3-4万/月 | 苏州格勤电子科技有限公司
# Python爬虫工程师 | 03-23发布 | 0.8-1.5万/月 | 杭州筑龙信息技术股份有限公司
# Python高级开发工程师 | 03-23发布 | 1.5-3万/月 | 杭州德适生物科技有限公司
# Python开发工程师 | 03-23发布 | 1-1.3万/月 | 浙江大云物联科技有限公司
# Python软件开发工程师 | 03-23发布 | 0.8-1万/月 | 上海特速网络科技有限公司
# Python开发工程师 | 03-23发布 | 1.5-2万/月 | 上海豪亿信息科技有限公司

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# 抓取信息
driver.get('http://www.51job.com')
driver.find_element(By.ID,'kwdselectid').send_keys('python')
driver.find_element(By.ID,'work_position_input').click()
time.sleep(2)


# 选择所有城市，去掉非杭州的且选择杭州，

city_list = driver.find_elements(By.XPATH,'/html/body/div[10]/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]/em')

for city in city_list:
    cityName = city.text
    status = city.get_attribute('class')
    # 检查杭州是否选上
    if cityName == '杭州' and status !='on':
            city.click()
    # 其他城市 如果已经在条件中，再点一次即可取消
    elif cityName != '杭州' and status == 'on':
            city.click()

# 保存城市选择
driver.find_element(By.ID,'work_position_click_bottom_save').click()
# 点击搜索
driver.find_element(By.CSS_SELECTOR,'.ush  button').click()
# 等待界面稳定
time.sleep(5)
# 搜索结果分析
jobs = driver.find_elements(By.CSS_SELECTOR,'.j_joblist .e')
for job in jobs:
    filelds = job.find_elements(By.CSS_SELECTOR,'.jname, .cname, .time, .sal')
    strField = [fileld.text for fileld in filelds]
    print (' | '.join(strField))
driver.quit()

