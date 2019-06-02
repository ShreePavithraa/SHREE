from selenium import webdriver
import pytest
import time
class Test_actitime():
    @pytest.fixture(scope="module")
    def setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("http://demo.actitime.com")
        driver.maximize_window()
        yield driver
        time.sleep(10)
        driver.close()  # this line will be executed after the execution of test_login below.

    def test_login(self,setup,user='admin',passw='manager'): #setup is used to set the browser
        time.sleep(2)
        driver.find_element_by_id("username").send_keys(user)
        time.sleep(2)
        driver.find_element_by_name("pwd").send_keys(passw)
        time.sleep(2)
        driver.find_element_by_id("loginButton").click()
        time.sleep(2)

    def test_create(self):
        driver.find_element_by_xpath("//div[text()='USERS']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='components_button  withPlusIcon']").click()
        time.sleep(2)
        first_name=driver.find_element_by_id("createUserPanel_firstNameField")
        first_name.send_keys("shree pavithraa")
        time.sleep(2)
        last_name=driver.find_element_by_id("createUserPanel_lastNameField")
        last_name.send_keys("venkatesh")
        email=driver.find_element_by_id("createUserPanel_emailField")
        email.send_keys("shreepavithraa04@gmail.com")
        uname=driver.find_element_by_id("createUserPanel_usernameField")
        uname.send_keys("shree_sp")
        passd=driver.find_element_by_id("createUserPanel_passwordField")
        passd.send_keys("SP@hogwarts")
        time.sleep(12)
        driver.find_element_by_id("createUserPanel_passwordCopyField").send_keys("SP@hogwarts")
        time.sleep(2)
        create=driver.find_element_by_class_name("components_button submitBtn")
        create.click()

