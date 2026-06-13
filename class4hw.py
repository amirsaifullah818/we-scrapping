from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://books.toscrape.com/catalogue/category/books_1/index.html")

bookDivs = browser.find_elements(By.CLASS_NAME, "product_pod")

for bookDiv in bookDivs:
    # name = bookDiv.find_element(By.CSS_SELECTOR, "h3 a").text
    # or
    name = bookDiv.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    price = bookDiv.find_element(By.CLASS_NAME, "price_color").text
    stock_availability = bookDiv.find_element(By.CLASS_NAME,"availability").text
    print(f"The book {name} costs {price} and it is {stock_availability}")

browser.quit()   