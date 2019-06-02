from selenium import webdriver

class A1:
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/Dell/Desktop/selenium/html/test3.html")
    driver.find_element_by_tag_name("input").click() #this selects only the first input tag
    #driver.find_elements_by_tag_name("input").click() #this calls both input tag. and store it in a list

ob = A1()
ob