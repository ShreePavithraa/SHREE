from selenium import webdriver
import time

class A:
    driver = webdriver.Chrome()
    driver.get("http://www.naukri.com")
    driver.maximize_window()
    time.sleep(2)
    driver.minimize_window()
    time.sleep(2)
    #driver.fullscreen_window()
    #time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2) #after 2 sec it will move to the next line
    driver.quit()


test = A()
test