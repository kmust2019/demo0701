from hytest import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class UI_0102:
    name = '检查添加客户'

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

        STEP(2, '添加客户')
        #  点添加客户按钮
        wd.find_element(By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > button').click()
        # 填入客户信息,电话,地址
        wd.find_element(By.CSS_SELECTOR, '#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input').send_keys('南京中医院')
        wd.find_element(By.CSS_SELECTOR,
                        '#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > input').send_keys(
            '13897774569')
        wd.find_element(By.CSS_SELECTOR,
                        '#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > textarea').send_keys(
            '测试地址')
        # 点创建
        wd.find_element(By.CSS_SELECTOR,'#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-12.col-md-12.col-sm-12 > button:nth-child(1)').click()
        wd.implicitly_wait(2)
        wd.refresh()
        #  定位客户信息
        list =  wd.find_elements(By.CSS_SELECTOR,'.search-result-item-field span')
        customer_info = [ li.text for li in list]
        INFO(customer_info)

        STEP(3, '客户信息检查')
        CHECK_POINT('客户信息检查', customer_info[1] == '南京中医院')
        CHECK_POINT('客户信息检查',customer_info[3] == '13897774569')
        CHECK_POINT('客户信息检查',customer_info[5] == '测试地址')

        wd.quit()