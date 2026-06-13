from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.bbc.com/news")


js_code_for_scrolling = "window.scrollBy(0, document.body.scrollHeight)"
browser.execute_script(js_code_for_scrolling)

BBCDivs = browser.find_elements(By.CLASS_NAME, "hvtsmL")


for BBCdiv in BBCDivs:
    Headline = BBCdiv.find_element(By.CLASS_NAME, "eQumHa").text 
    Location =  BBCdiv.find_element(By.CLASS_NAME,  "dIrLFx").text
    
    print(f"A current BBC headline right now is {Headline} from {Location}")
    
browser.quit()