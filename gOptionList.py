# https://docs.seleniumhq.org/docs/03_webdriver.jsp#setting-up-webdriver-project

print("\nPython - Selenium Web-driver on Chrome")
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()
print("\nSearch - Buy Samples page")
driver.get("http://www.globalsources.com/SITE/BUY-PRODUCT-SAMPLES.HTM")
print(driver.title)

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

# selector = driver.find_element_by_class_name("searchType_list")
# items = selector.find_elements_by_tag_name("li")
# for item in items:
#     text = item.text
#     print("item:",text)
# driver.execute_script("document.getElementById('qType').setAttribute('value', 'EXHIBITOR')")

KWS = driver.find_element_by_name("query")
KWS.send_keys("cheese!")
KWS_submit = driver.find_element_by_class_name("GS_searchBtn").click() #because KWS does not have a submit/click but uses an 'enter' key

try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print(driver.title)  #see "Global Sources - Product Search: cheese!"

finally:
    input("Press Enter to continue...")

results_tabs = driver.find_element_by_class_name("listing_tab ")
for tab in results_tabs:
    print(tab(text))
driver.quit() 