from selenium import webdriver
import time

class A2:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://demo.actitime.com")
    first_title = driver.title
    first_window = driver.current_window_handle
    print(first_window)
    driver.find_element_by_link_text("actiTIME Inc.").click()
    time.sleep(10)
    all_window = driver.window_handles
    print(all_window)
    for curr_window in all_window:
        if curr_window != first_window:
            print(curr_window)
            driver.switch_to.window(curr_window)
    second_title = driver.title
    print(first_title)
    print(second_title)

sh = A2()
sh