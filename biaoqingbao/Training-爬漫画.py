# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import os
import requests
import random


def mouse_scroll(driver):
    count = 1
    # step = random.uniform(250, 500)
    counter = random.uniform(2, 5)
    while count < 4:
        driver.execute_script("window.scrollBy(0, 400)")
        time.sleep(counter)
        count += 1


def get_picture(driver):
    headers = {
        # "Referer": "http://www.1kkk.com/vol4-697431/",
        "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 Safari / 537.36",
    }
    soup = BeautifulSoup(driver.page_source, 'lxml')
    current_page = soup.select('span[class="current"]')[0].get_text()
    img_tag = soup.select('#cp_image')[0]
    # 拿到的是一个链接
    img = img_tag.get("src")
    img_content = requests.get(img, headers=headers).content
    time.sleep(1)
    file_path = "d:/spider_manga/4/" + current_page + ".jpeg"
    mouse_scroll(driver)
    if not(os.path.exists(file_path)):
        fw = open(file_path, "wb")
        fw.write(img_content)
        fw.close()
        print("saved")
    else:
        print('img exists')


def next_page(driver):
    page_number = int(driver.find_element_by_xpath('//span[@class="current"]').text)
    page_number += 1
    max_page_number = 255
    if page_number != max_page_number:
        tag = "//a[@href='/vol4-697431-p" + str(page_number) + "/']"
        print("current tag: " + tag)
        next = driver.find_element_by_xpath(tag)
        next.click()
        return True
    else:
        get_picture(driver)
        return False


driver = webdriver.Chrome()
driver.get("http://www.1kkk.com/vol4-697431/")
time.sleep(1)
flag = True
while flag:
    time.sleep(2)
    get_picture(driver)
    time.sleep(2)
    result = next_page(driver)
    if not result:
        print("Page end")
        break
