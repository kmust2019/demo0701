from hytest import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class UI_0101:
    name = '检查操作菜单 UI_0101'

    def teststeps(self):
        STEP(1, '登录网站')

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        wd = webdriver.Chrome(options=options)
        wd.implicitly_wait(10)

        wd.get('http://127.0.0.1:8047/mgr/sign.html')

        wd.find_element(By.ID,'username').send_keys('byhy')
        wd.find_element(By.ID,'password').send_keys('88888888')

        wd.find_element(By.TAG_NAME,'button').click()

        STEP(2, '获取左侧菜单信息')

        eles = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu li span')

        menuText = [ele.text for ele in eles]

        INFO(menuText)

        STEP(3, '检查菜单栏')

        CHECK_POINT('左侧菜单检查', menuText[:3] == ['客户', '药品', '订单'])

        wd.quit()