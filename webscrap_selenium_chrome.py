from selenium import webdriver
browser = webdriver.Chrome()
#browser.get("http://www.globalsources.com/SITE/BUY-PRODUCT-SAMPLES.HTM")
browser.get("http://www.google.com")
print("scraping using Selenium on Chrome: ")
nav = browser.find_element_by_id("q")
print(nav.text)