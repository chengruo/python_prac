from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
b = webdriver.Chrome()
b.get("https://www.nowcoder.com/search?query=&type=post")

elem = b.find_element_by_id("search")
elem.send_keys("京东")
elem.send_keys(Keys.ENTER)

elem = b.find_element_by_class_name("discuss-main clearfix")
print(elem.get_attribute("href"))
