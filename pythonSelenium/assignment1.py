from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_object = Service()
driver = webdriver.Chrome(service=service_object, options=chrome_options)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise")

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
statement = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
driver.close()
print(statement)
username = statement[19:48]
print(username)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Hello@123")
driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()



