# https://docs.seleniumhq.org/docs/03_webdriver.jsp#setting-up-webdriver-project

print("\nPython - Selenium Web-driver on Chrome")
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()
#-driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
#-driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
# go to the google home page
#driver.get("http://www.google.com")
driver.get("http://www.globalsources.com")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
# inputElement = driver.find_element_by_name("q")
inputElement = driver.find_element_by_name("query")

# reference webdriver get elements
# Locating Elements with Selenium WebDriver, findElement() method returns and WebElement and findElements() returns a list of WebElements.
# 1. By ID:				element = driver.find_element_by_id("coolestWidgetEvah")
# 2. By NAME:			cheese = driver.find_element_by_name("cheese")
# 3. By CLASS:			cheeses = driver.find_elements_by_class_name("cheese")
# 4. By TAGNAME:		frame = driver.find_element_by_tag_name("iframe")
# 5. By CSS Selector:	cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
# 6. By Link text:		cheese = driver.find_element_by_link_text("cheese")
# 6a. By Partial Link text:	cheese = driver.find_element_by_partial_link_text("cheese")
# 7. By XPath:			inputs = driver.find_elements_by_xpath("//input")
#

# type in the search text
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()
submitElement = driver.find_element_by_class_name("GS_searchBtn").click() #because inputElement does not have a submit/click but uses an 'enter' key

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 100).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print(driver.title)  #see "Global Sources - Product Search: cheese!"
   
finally:
    # nwait = 5
    # while nwait:
    #     print(nwait)
    #     time.sleep(1)	# idle for some amount of time
    #     nwait = nwait - 1
    input("Press Enter to continue...")
    driver.quit()




print("\n\nNew search - Buy Samples page")
driver.get("http://www.globalsources.com/SITE/BUY-PRODUCT-SAMPLES.HTM")
print(driver.title)
select = driver.find_element_by_id("qTypeSelTarget")
allOptions = select.find_element_by_tag_name("a")
for option in allOptions:
    print "Value is: ", option.get_attribute("optionval")
    
input("Press Enter to continue...")
driver.quit()

