from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class A1:
    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    time.sleep(3)
    upload = driver.find_element_by_xpath("//input[@value='Upload CV']")#send_keys("H:\selenium\shree\shree_selenium\python_package\dummy_doc.docx")
    act = ActionChains(driver)
    act.send_keys_to_element(upload,"H:\selenium\shree\shree_selenium\python_package\dummy_doc.docx").perform()
    time.sleep(5)

ob=A1()
ob