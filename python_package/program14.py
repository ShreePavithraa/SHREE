from selenium import webdriver
import time
class Naukri():
    def noti(self):
        chrome_options=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://www.naukri.com")
        time.sleep(5)
        driver.save_screenshot=("H:\selenium\selenium\screenshot.png")

ob=Naukri()
ob.noti()