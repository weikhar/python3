from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://http://www.globalsources.com/SITE/BUY-PRODUCT-SAMPLES.HTM/")
print("scraping using Selenium on Chrome: ")
nav = browser.find_element_by_id("sf_nav_pop")
print(nav.text)