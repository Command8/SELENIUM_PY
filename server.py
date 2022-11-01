from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#serv_obj = Service("C:\Users\kkandikatla\Documents\Drivers\chromedriver_Win32\chromedriver.exe")
serv_obj = Service("C:\Users\anrosario\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://cures.azurewebsites.net/")
driver.maximize_window()
driver.close()