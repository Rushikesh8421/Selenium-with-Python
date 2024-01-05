from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("headless") #It helps to run the script without frontend view so the automation process becomes fast

chrome_options.add_argument("--ignore-certificate-errors") #This helps in handeling all ssn or private page or this page is not accessalble things automatically

chrome_options.add_experimental_option('detach', True)
service_object = Service()
driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png") #It takes screenshot and saves file


