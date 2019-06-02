from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[text()='✕']").click()
driver.implicitly_wait(5)
name=driver.find_element_by_xpath("//span[text()='Men']")

act = ActionChains(driver)
act.move_to_element(name).perform()
time.sleep(3)
driver.find_element_by_xpath("//a[@title='T-Shirts']").click()
time.sleep(3) 

#driver.execute_script("window.scrollTo(0,200)")
#next=driver.find_element_by_link_text("/mens-clothing/tshirts/pr?sid=2oq%2Cs9b%2Cj9y&otracker=nmenu_sub_Men_0_T-Shirts&page=2")
found_next=driver.find_element_by_xpath("//span[text()='Next']").location_once_scrolled_into_view
driver.implicitly_wait(2)
driver.find_element_by_xpath("//span[text()='Next']").click()
#found_next.click()
#driver.find_element_by_link_text("/mens-clothing/tshirts/pr?sid=2oq%2Cs9b%2Cj9y&otracker=nmenu_sub_Men_0_T-Shirts&page=2").click()


