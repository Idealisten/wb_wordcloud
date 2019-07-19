from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import re
import time


url = "https://m.weibo.cn"

b = webdriver.Firefox()
b.get(url)
b.maximize_window()
time.sleep(2)

# 点击登陆/注册按钮
ele = b.find_element_by_class_name("lite-sign-in")
ele.click()
time.sleep(2)

# 点击使用账号密码登录
ele = b.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/a")
ele.click()
time.sleep(2)

# 输入账号
ele = b.find_element_by_xpath('//*[@id="loginName"]')
ele.send_keys("15033565336")
time.sleep(2)

# 输入密码
ele = b.find_element_by_xpath('//*[@id="loginPassword"]')
ele.send_keys("123678432xlwb")
time.sleep(2)

# 点击登录按钮
ele = b.find_element_by_xpath('//*[@id="loginAction"]')
ele.click()
time.sleep(5)

# 点击搜索框
ele = b.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/a/aside/label/div')
ele.click()
time.sleep(3)

# 在弹出的页面中再次点击搜索框
ele = b.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/form/input')
ele.click()
time.sleep(5)

# 输入搜索关键词
ele.send_keys('我宇宙第一怂包')

# ENTER键确认搜索
ele.send_keys(Keys.ENTER)
time.sleep(5)

# 点击用户名/头像进入用户主页
ele = b.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/h3/span')
ele.click()
time.sleep(2)

