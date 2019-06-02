from selenium import webdriver
import time

class A1:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.actitime.com")
    driver.find_element_by_id("username").send_keys("admin")
    #driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_css_selector("input[name = 'pwd']").send_keys("manager")
    driver.find_element_by_id("loginButton").click()
    time.sleep(10)
    driver.quit()

ab = A1()
ab