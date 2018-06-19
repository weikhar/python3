# https://docs.seleniumhq.org/docs/03_webdriver.jsp#setting-up-webdriver-project
print("Python - Selenium Web-driver on Chrome")
import os
print("\nPython3 script:", os.path.basename(__file__))
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()
print("\nSearch - Buy Samples page")
url = "http://www.globalsources.com/SITE/BUY-PRODUCT-SAMPLES.HTM"
driver.get(url)
print("at page:", driver.title)
print("page url:", driver.current_url)

#--Reference --------
# select = driver.find_element_by_tag_name("select")
# allOptions = select.find_elements_by_tag_name("option")
# for option in allOptions:
#     print("Value is:", option.get_attribute("value"))
#     option.click()
#----------

	# <div class="GS_search GS_searchRFQ">
	# <div class="GS_searchType">
	# <div class="searchType_tit" id="qTypeSelTrigger">Products</div>
	# <ul class="searchType_list" id="qTypeSelTarget">
	# <li optionVal="PRODUCT"><a href="javascript:void(0);">Products</a></li>
	# <li optionVal="SUPPLIER"><a href="javascript:void(0);">Suppliers</a></li>
	# <li optionval="EXHIBITOR"><a href="javascript:void(0);">Exhibitors</a></li>
	# <li optionVal="NEWS"><a href="javascript:void(0);">News</a></li>
	# </ul>
	# </div>

# use select_by_index( ) method to select an option using the index attribute. -- 'qTypeSelTarget' not found
#searchmode = Select(driver.find_element_by_id('qTypeSelTarget'))
#searchmode.select_by_index(2)

# use select_by_value( ) method to select an option using the index attribute. -- 'qTypeSelTarget' not found
# searchmode = Select(driver.find_element_by_id('qTypeSelTarget'))
# searchmode.select_by_value('SUPPLIER')

# Using Text of Dropdown - have to match the text which is displayed in the drop down.
#searchmode = driver.find_element_by_id('qTypeSelTarget')
#searchmode.select_by_visible_text('Suppliers')
#-- selenium.common.exceptions.UnexpectedTagNameException: Message: Select only works on <select> elements, not on <ul>


print("wait 1 sec")
time.sleep(1)
KWS = driver.find_element_by_id("gsolquery")
KWS.send_keys("cheese!", Keys.ENTER)
print("wait 1 sec")
time.sleep(1)
#KWS_submit = driver.find_element_by_class_name("GS_searchBtn").click() #because KWS does not have a submit/click but uses an 'enter' key

try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print("\nat page:", driver.title)  #see "Global Sources - Product Search: cheese!"
    print("page url:", driver.current_url)
finally:
    #input("Press Enter to continue...")
    time.sleep(1)
    print("wait 1 sec")

# At the KWS results listing page, select the Supplier List tab
rtabs = driver.find_element_by_css_selector("[class^=listing_tab ]")
items = rtabs.find_elements_by_tag_name("li")
for item in items:
    #print("tab:",item.tag_name,"-",item.text)
    if item.text == "Supplier List":
        item.click()
        break
input("\nWhen at Supplier List tab, press Enter to continue...")

# try to do a sKWS here (selenium prefers to select visible droplist options, ie show droplist first)
searchmode = driver.find_element_by_id("qTypeSelTrigger") 
searchmode.click() # >> select the droplist
searchmode = driver.find_element_by_id("qTypeSelTarget")
items = searchmode.find_elements_by_tag_name("li")
for item in items:
    print("tab:",item.tag_name,"-",item.text)
    if item.text == "Suppliers":
        item.click()
        input("\nselected [Suppliers] search mode, press Enter to continue...")
        break

print("wait 1 sec")
time.sleep(1)
KWS = driver.find_element_by_id("gsolquery")
KWS.clear()
KWS.send_keys("grout", Keys.ENTER)
input("\nEntered keyword, press Enter to continue...")
#KWS_submit = driver.find_element_by_class_name("GS_searchBtn").click() #because KWS does not have a submit/click but uses an 'enter' key

driver.quit()
print("end")