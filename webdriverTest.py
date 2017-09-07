# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('lang=zh_CN.UTF-8')
# chrome = webdriver.Chrome(chrome_options=options)
# print("------1--------")
# chrome.get("http://www.baidu.com")
# print("-------")
# print(chrome.title)
# keys = chrome.find_element_by_id("kw").send_keys("user open")
# chrome.find_element_by_id("su").click()
# chrome.quit()
# from selenium import webdriver
# # coding = utf-8
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://www.baidu.com')
# print(driver.title)


"""
    notice the version of the chrome and the plugin of chrome
"""
from time import sleep

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("av")
driver.find_element_by_id("su").click()
sleep(500)
driver.quit()
