from selenium import webdriver
import time

class A2:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath("//input[@id='email']").send_keys("shreepavithraa04@gmail.com")
    driver.find_element_by_xpath("//input[@id='pass']").send_keys("tvszest8768")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id = 'userNavigationLabel']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[text() = 'Log Out']").click()
    time.sleep(5)
  #  driver.quit()

sh = A2()
sh