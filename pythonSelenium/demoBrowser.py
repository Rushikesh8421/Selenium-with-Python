from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#chrome driver - chrome browser
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("https://www.atom.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.helloworld.com")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()