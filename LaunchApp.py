#from selenium import webdriver

#browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')




from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#serv_obj = Service("C:\Users\<username>\Documents\Drivers\chromedriver_Win32\chromedriver.exe")
#serv_obj = Service("C:/Users/<username>/chromedriver.exe")
serv_obj = Service('C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://<application url/")
driver.maximize_window()
l = driver.find_element(By.XPATH,'//button[text()=\"Login\"]')
#perform click
l.click()
print("Page title is: ")
print(driver.title)
driver.implicitly_wait(20)
