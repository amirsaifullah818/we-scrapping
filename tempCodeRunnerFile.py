from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.bbc.com/news")

bbcDivs = browser.find_elements(By.CLASS_NAME, "hnNPal")

# scroll the website
js_code_for_scrolling = "window.scrollBy(0, document.body.scrollHeight)"
browser.execute_script(js_code_for_scrolling)

for bbcdiv in bbcDivs:
    Headline = bbcdiv.find_element(By.CLASS_NAME, "eQumHa").text
    Subtext =  bbcdiv.find_element(By.CLASS_NAME,  "ffnHHm").text
    
    print(f"A current BBC headline right now is {Headline} with its following subtext, {Subtext}")
    
browser.quit()