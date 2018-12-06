from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
b = webdriver.Chrome()

b.get('http://172.19.135.12:8080/iptvsmp')
elem = b.find_element_by_name("userName")
elem.send_keys("00")
elem = b.find_element_by_name("password")
elem.send_keys("")
#elem.send_keys(Keys.TAB)
elem.send_keys(Keys.ENTER)
