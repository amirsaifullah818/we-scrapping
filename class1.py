
import webbrowser


website_name = input("Enter the name of the website: ")

website_link = f"https://{website_name}.com"

print(website_link)


# now open the link

webbrowser.open(website_link)




# HW: Use webbrowser to open any website
# Instruction:
# - Take the website name from the  user as input
# - Then print "opening the website.."
# Then, open the website

import webbrowser

website_name = input("Enter the name of the website: ")


website_link = f"https://{website_name}.com"


print("opening the website")


webbrowser.open(website_link)