from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
b = webdriver.Chrome()
#b = webdriver.PhantomJS()
#b.get('http://m.weibo.cn/')
b.get("https://weibo.com/")

#elem = b.find_element_by_id("loginname")

#elem = b.find_element_by_xpath("/html/body/div[1]/div/a[2]")
#elem.send_keys(Keys.ENTER)
sleep(5)
#b.find_element_by_id("loginname")
#b.find_element_by_class_name("W_login_form")

#elem = b.find_element_by_xpath("//*[@id='loginname']")
elem = b.find_element_by_id("loginname")
elem.send_keys('15708418034@163.com')

elem = b.find_element_by_xpath("//*[@type='password']")
elem.send_keys('w*963.*963.')

#suda-uatrack='key=V6update_leftnavigate&value=unfold'
#suda-uatrack='key=V6update_leftnavigate&value=secret'
elem.send_keys(Keys.ENTER)
sleep(5)
elem = b.find_element_by_xpath("//*[@suda-uatrack='key=V6update_leftnavigate&value=unfold']")
elem.send_keys(Keys.ENTER)
elem = b.find_element_by_xpath("//*[@suda-uatrack='key=V6update_leftnavigate&value=secret']")
elem.send_keys(Keys.ENTER)
print(b.page_source)