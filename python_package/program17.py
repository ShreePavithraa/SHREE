from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from datetime import timedelta
import time
presentmonth=datetime.datetime.now().strftime("%B")

cudate=datetime.datetime.now().strftime("%d")
dedate=datetime.datetime.now()+timedelta(days=20)
demonth=dedate.strftime("%B")
ardate=dedate+datetime.timedelta(days=50)
armonth=ardate.strftime("%B")
print(cudate,dedate,ardate)