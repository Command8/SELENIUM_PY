from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#serv_obj = Service("C:\Users\<username>\Documents\Drivers\chromedriver_Win32\chromedriver.exe")
serv_obj = Service("C:\Users\<username>\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://<applicaton url>/")
driver.maximize_window()
driver.close()
