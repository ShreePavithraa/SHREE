from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class A1:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.actitime.com")
    driver.find_element_by_id("username").send_keys("admin")
    # driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_css_selector("input[name = 'pwd']").send_keys("manager")
    driver.find_element_by_id("loginButton").click()
    time.sleep(10)
    driver.find_element_by_xpath("//div[text()='USERS']").click()
   # driver.find_element_by_link_text("administration/userlist.do").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='components_button  withPlusIcon']").click()
    driver.find_element_by_id("createUserPanel_firstNameField").send_keys("shree")
    #driver.find_element_by_xpath("//input[@id='createUserPanel_firstNameField']").send_keys("shree")
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='closeButton hideButton_panelContainer']").click()

abc=A1()
abc