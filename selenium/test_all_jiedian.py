import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get('https://cdn2.byhy.net/files/selenium/sample1a.html')

poem_list = driver.find_elements(By.CSS_SELECTOR,'#t1 > p')

for p in poem_list :
    print(p.text)


