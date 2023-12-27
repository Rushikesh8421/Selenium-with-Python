import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(service=service_object,options=chrome_options)

driver.implicitly_wait(2) # 5 seconds is max time out

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #list[]
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation
sumList = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
totalSum = 0
for num in sumList:
    totalSum = totalSum + int(num.text)
displayedSum = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert totalSum == displayedSum
print("Total counted sum is: "+str(totalSum))
print("Total Displayed sum on website is: "+str(displayedSum))

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
if discount < displayedSum:
    print(True)
else:
    assert False






