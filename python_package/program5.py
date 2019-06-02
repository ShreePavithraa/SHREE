from selenium import webdriver
import time

class A1:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.actitime.com")
    driver.find_element_by_name("remember").click()
    time.sleep(20)
    driver.find_element_by_link_text("actiTIME Inc.").click()

test = A1()
test