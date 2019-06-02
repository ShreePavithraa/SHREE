from selenium import webdriver
import time

class A3:

    driver = webdriver.Chrome()
    driver.get("http://demo.actitime.com")
    driver.maximize_window()
    driver.find_element_by_xpath()
