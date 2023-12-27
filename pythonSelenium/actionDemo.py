from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
service_object = Service()
driver = webdriver.Chrome(service=service_object,options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com//AutomationPractice/")

action = ActionChains(driver)
# action.double_click(driver.find_element(By.))
# action.click_and_hold()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()