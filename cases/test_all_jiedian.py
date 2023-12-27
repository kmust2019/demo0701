from hytest import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class UI_0820:
    name = 'UI_0820'
    def teststeps(self):
        STEP(1, '登录网站')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        wd = webdriver.Chrome(options=options)
        print('11')
        wd.implicitly_wait(10)
        STEP(2, '获取左侧文本信息')
        wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')
        poem_list = wd.find_elements(By.CSS_SELECTOR, '#t1 > p')
        for p in poem_list:
            print(p.text)

        poem_content = [p.text for p in poem_list]
        STEP(3, '检查菜单栏')

        CHECK_POINT('check_text', poem_content[:2] == ['静夜思', '春夜喜雨'])
        wd.quit()









