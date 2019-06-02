from selenium import webdriver
import pytest
import time
class Test_actitime():
    @pytest.fixture(scope="module")
    def setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("http://demo.actitime.com")
        yield driver
        driver.close()  # this line will be executed after the execution of test_login below.

    @pytest.mark.parametrize("user,passw",[('raju','gentleman'),('admin','manager')]) #since no scope is given it will be taken as function. #this acts as a tuple. raju and gentle man is wrong credential.and admin is correct.so this part will be executed twice. for negative and positive scenario. for 1st it will print as passed(since we have not given any condition to say it as failed). 2nd it should print passed.
    def test_login(self,setup,user,passw):
        time.sleep(2)
        driver.find_element_by_id("username").send_keys(user)
        time.sleep(2)
        driver.find_element_by_name("pwd").send_keys(passw)
        time.sleep(2)
        driver.find_element_by_id("loginButton").click()
        time.sleep(2)
