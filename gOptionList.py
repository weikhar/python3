# https://docs.seleniumhq.org/docs/03_webdriver.jsp#setting-up-webdriver-project

print("\nPython - Selenium Web-driver on Chrome")
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
	# </ul></div>
	# 	<div class="GS_searchQuery GS_searchTSQuery">
	# 		<input type="text" id="gsolquery" name="query" class="GS_searchFiled" value="" onKeyPress="if(event.keyCode==13){setUpHeaderSearch();return false;}" autocomplete="off">
	# 		<div class="searchRelated" id="relateSearch" domain="http://www.globalsources.com" sourceCode="GSOLHP_PopularRecentSearch" language="en" pageType="">
	# 		</div>
	# 	</div>
	# 	<input onclick="setUpHeaderSearch();return false;" id="keywordBtnSearch" type="submit" class="GS_searchBtn" value="">
	# 	<input type="hidden" name="language" id="language" value="en"/>
	# 	</div>

#print("1 sec")
time.sleep(1)
KWS = driver.find_element_by_id("gsolquery")
#print("1 sec")
time.sleep(1)
KWS.send_keys("cheese!", Keys.ENTER)
#KWS_submit = driver.find_element_by_class_name("GS_searchBtn").click() #because KWS does not have a submit/click but uses an 'enter' key

try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print("\nat page:", driver.title)  #see "Global Sources - Product Search: cheese!"
    print("page url:", driver.current_url)
finally:
    #input("Press Enter to continue...")
    time.sleep(1)

#print("1 sec")
time.sleep(1)
rtabs = driver.find_element_by_css_selector("[class^=listing_tab ]")
items = rtabs.find_elements_by_tag_name("li")
for item in items:
    #print("tab:",item.tag_name,"-",item.text)
    if item.text == "Supplier List":
        item.click()
        break

input("\nWhen at Supplier List tab, press Enter to continue...")
driver.quit()
print("end")