from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #to give explicit time
from selenium.webdriver.common.by import By # to give th epath by is used
import datetime
from datetime import timedelta
import time
#presentmonth=datetime.datetime.now().strftime("%B")

class Trip:
    #opens IRCTC till click on flights
    driver = webdriver.Chrome()
    driver.get("http://www.irctc.com")
    driver.maximize_window()
    tourism=driver.find_element_by_xpath("//div[text() = 'TOURISM ']")
    tourism.click()
    time.sleep(2)
    print(driver.title)
    all_window = driver.window_handles
    driver.switch_to.window(all_window[1])
    print(driver.title)
    time.sleep(30)
    flights=driver.find_element_by_xpath("//div[@class='Flights']")
    flights.click()
  #  driver.find_element_by_xpath("//span[text()='Flights']")
    time.sleep(10)

    #round trip from boston to bangalore
    time.sleep(10)
    all_window_1 = driver.window_handles
    driver.switch_to.window(all_window_1[2])
    print(driver.title)
    time.sleep(10)
    driver.find_element_by_xpath("//label[@for='Round-Trip']").click()
    time.sleep(5)
    #driver.find_element_by_xpath("//div[@class='md-form form-control btn-rounded my-0']/..//input[@name='From']").send_keys("Boston (BOS)")
    driver.find_element_by_xpath("//div[text()='Boston (BOS)']").click()
    time.sleep(3)
    #driver.find_element_by_xpath("//input[@name='To']").send_keys("Bengaluru (BLR)")
    driver.find_element_by_xpath("//div[text()='Bengaluru (BLR)']").click()
    time.sleep(3)

    #dept date and arrival date
    cudate = datetime.datetime.now().strftime("%d")
    dedate = datetime.datetime.now() + timedelta(days=20)
    demonth = dedate.strftime("%B")
    ardate = dedate + datetime.timedelta(days=50)
    armonth = ardate.strftime("%B")
    print(cudate, dedate, ardate)

    #calender
    #departure date
    driver.find_element_by_xpath("//div[@id='Departure-Date'").click()
    driver.find_element_by_xpath("//div[@id='Departure-Date']//tr/td/span[text()='"+str(demonth)+"']").click()
    time.sleep(5)

    #arrival date



xyz=Trip()
xyz

