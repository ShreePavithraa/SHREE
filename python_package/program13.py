from selenium import webdriver
import time

class A1:

    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    time.sleep(8)
    #driver.find_element_by_xpath("//label[@for='BE_flight_origin_city']").send_keys("Bangalore")
    driver.find_element_by_xpath("//label[@for='BE_flight_origin_city']").click()
    time.sleep(25)
    driver.find_element_by_xpath("//p[text() ='Bangalore ']").click()
    time.sleep(8)
   # driver.find_element_by_xpath("//label[@for='BE_flight_arrival_city']").send_keys("Goa")
    driver.find_element_by_xpath("//label[@for='BE_flight_arrival_city']").click
    time.sleep(30)
    driver.find_element_by_xpath("//p[text() ='Goa ']").click()
    time.sleep(8)
    driver.find_element_by_class_name("ripple animate").click()
    time.sleep(3)


yatra = A1()
yatra