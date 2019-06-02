from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class A1:
    driver = webdriver.Chrome()
    driver.get("https://www.monsterindia.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class='uprcse semi-bold']").click()
    upload=driver.find_element_by_xpath("//input[@id='file-upload']")
    upload.send_keys("H:\selenium\shree\shree_selenium\python_package\dummy_doc.docx")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='pop_sbm']").click()
    print("submitted")
ob=A1()
ob