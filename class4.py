from selenium import webdriver
from selenium.webdriver.common.by import By



# setup the browser
browser = webdriver.Chrome()


# open the website
browser.get("https://quotes.toscrape.com/")



# now find all the quote Divs

quoteDivs = browser.find_elements(By.CLASS_NAME, "quote")


# now loop trhough the quote divs and get each quote div

for quoteDiv in quoteDivs:
    author_quote = quoteDiv.find_element(By.CLASS_NAME,"text").text
    author_name = quoteDiv.find_element(By.CLASS_NAME, "author").text
    
    print(f"{author_name} said: {author_quote} \n")
    
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://books.toscrape.com/catalogue/category/books_1/index.html")

bookDivs = browser.find_elements(By.CLASS_NAME, "product_pod")

for bookDiv in bookDivs:
    name = bookDiv.find_element(By.CLASS_NAME, "a").text
    price = bookDiv.find_element(By.CLASS_NAME, "price_color").text
    print(f"The book{name} costs {price}")

browser.quit()   