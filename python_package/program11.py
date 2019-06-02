from selenium import webdriver
import time

class A5:

    driver = webdriver.Chrome()
    driver.get("https://www.craftsvilla.com")
    driver.maximize_window()
    driver.find_element_by_css_selector("input[Id='searchval']").send_keys("salwar")
    driver.find_element_by_xpath("//i[@class='icon cv-search']").click()
    time.sleep(10)
    prize = driver.find_element_by_css_selector("span[class='product-offer-price']").text  #THIS FETCH THE first prize of the product
    print(prize)
    #prize1 = driver.find_element_by_xpath("//span[@class='product-offer-price']/..//span[text()='₹ 1397']").text
    prize1 = driver.find_element_by_xpath("//a[contains(@href,'/shop/craftsvilla-cream-color-cotton-blend-abstract-printed-unstitched-salwar-suit')]/../p/span[@class='product-offer-price']").text
    print(prize1)

salwar = A5()
salwar