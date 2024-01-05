from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedList = []
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

elementList = driver.find_elements(By.XPATH, "//tr/td[1]")

for el in elementList:
    browserSortedList.append(el.text)

originalBrowserList = browserSortedList.copy()

browserSortedList.sort()
assert originalBrowserList == browserSortedList
