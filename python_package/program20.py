from selenium import webdriver
import time

class scroll:
    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,200)")
    driver.find_element_by_xpath("//a[text()='Jobseeker Services']").location_once_scrolled_into_view

p=scroll()
p