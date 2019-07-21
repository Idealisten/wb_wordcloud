from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import requests
import re
import time
import json


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
ele = b.find_element_by_xpath(
    '//div[@id="app"]/div[1]/div[1]/div[1]/a/aside/label/div')
ele.click()
time.sleep(3)

# 在弹出的页面中再次点击搜索框
ele = b.find_element_by_xpath(
    '/html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/form/input')
ele.click()
time.sleep(5)

# 输入搜索关键词
ele.send_keys('我宇宙第一怂包')

# ENTER键确认搜索
ele.send_keys(Keys.ENTER)
time.sleep(5)

# 点击用户名/头像进入用户主页
ele = b.find_element_by_xpath(
    '/html/body/div/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/h3/span')
ele.click()
time.sleep(2)

# 保存cookie信息(字典列表)
cookies_dict = b.get_cookies()

# 去除cookie中的一个无用信息
cookies_dict.pop(-1)

# 从cookie字典列表中仅提取出'name'和'value'属性，组成列表
cookie_list = []
for dict in cookies_dict:
    cookie = dict['name'] + '=' + dict['value']
    cookie_list.append(cookie)

# 将cookie列表转化为字符串，成为可以传入浏览器的cookie
cookie_str = ';'.join(cookie_list)

# 请求参数
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
header = {'User-Agent': user_agent, 'Cookie': cookie_str}

# 访问这个API可以获得每页的微博信息,页数通过最后的page参数传递
xhr_url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304136486443586_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}'

# 这个列表储存所有的微博ID（非必须）
wb_id_list = []

# 假设共有n页微博
n = 10

# 微博文本存储路径
file_path = r'C:\Users\CY\Desktop\text.txt'

with open(file_path, 'a') as f:

    # 循环爬取50页
    for i in range(1, n):
        try:
            # 通过format控制请求的页数
            r = requests.get(xhr_url.format(i), headers=header)
            # 保存返回的json字符串
            json_str = r.text
            # 将json字符串转化为字典格式
            json_dict = json.loads(json_str)
            for index in range(25):
                if json_dict['data']['cards'][index]['card_type'] == 9:
                    # 从字典中提取微博id
                    wb_id = json_dict['data']['cards'][index]['mblog']['idstr']
                    # 将微博id插入微博id列表
                    wb_id_list.append(wb_id)
                    # 从'text'标签提取出微博文本（包含表情/换行符等标签）
                    raw_text = json_dict['data']['cards'][index]['mblog']['text']
                    # 通过正则表达式去除所有标签，只保留中文文本
                    pattern = re.compile(r'<.*?>')
                    m = pattern.split(raw_text)
                    # 将得到的文本列表转化为字符串
                    text = ''.join(m)
                    text = text + '\n'
                    # 保存得到的文本字符串
                    f.write(text)

        except BaseException:
            pass
        time.sleep(10)
        print("\r当前进度:{:.2f}%".format((i + 1) * 100 / n), end=' ')

with open(r'C:\Users\CY\Desktop\wb_id.txt', 'a') as wb:
    for wb_id in wb_id_list:
        wb_id = wb_id + '\n'
        wb.write(wb_id)
