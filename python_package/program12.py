from selenium import webdriver
import time

class A6:

    driver = webdriver.Chrome()
    driver.get("https://www.seleniumhq.org")
    driver.maximize_window()
    driver.find_element_by_xpath("//a[@href ='/download/']").click()
    time.sleep(5)
    a = driver.find_element_by_xpath("//td[text() = 'Ruby']").text
    print(a)
    b = driver.find_element_by_xpath("//td[text() = 'Ruby']/..//td[2]").text
    print(b)


org = A6()
org
