from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
service_object = Service()
driver = webdriver.Chrome(service=service_object, options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #inside frame give either frame id or frame name to locate frame
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frame")

#when we are inside switch_to.frame we can't access the elements outside of frame to access it we need to switch_to.default_content
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)


