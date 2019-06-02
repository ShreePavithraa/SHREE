from selenium import webdriver
import time

class A:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_script("alert('hi this is shree')")
    time.sleep(2)
    #driver.switch_to.alert.accept()
    #driver.switch_to.alert.dismiss()
    a = driver.switch_to.alert.text
    print(a)


test = A()
test