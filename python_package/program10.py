from selenium import webdriver
import time

class A3:

    driver = webdriver.Chrome()
    driver.get("http://www.irctc.com")
    driver.maximize_window()
    driver.find_element_by_xpath("//div[text() = 'TOURISM ']").click()
    time.sleep(2)
    print(driver.title)
    all_window = driver.window_handles
    driver.switch_to.window(all_window[1])
    print(driver.title)
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='Flights']").click()
    time.sleep(2)

irctc = A3()
irctc
