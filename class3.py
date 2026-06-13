from selenium import webdriver
from selenium.webdriver.common.by import By




# setup the browser

driver = webdriver.Chrome()

# now open a website
driver.get("https://www.scrapethissite.com/pages/simple/")



#find the country names
element = driver.find_element(By.CLASS_NAME, "lead")

print(element.text)