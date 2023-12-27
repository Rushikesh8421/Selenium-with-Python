from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Rushikesh"
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()

