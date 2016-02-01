from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.baidu.com")

# the page is ajaxy so the title is originally this:
print driver.title

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("wd")

# type in the search
inputElement.send_keys("selenium!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

# By ID
element = driver.find_element_by_id("coolestWidgetEvah")

# or

from selenium.webdriver.common.by import By
element = driver.find_element(by=By.ID, value="coolestWidgetEvah")
# By Class Name
cheeses = driver.find_elements_by_class_name("cheese")

# or

from selenium.webdriver.common.by import By
cheeses = driver.find_elements(By.CLASS_NAME, "cheese")

# By Tag Name¶
frame = driver.find_element_by_tag_name("iframe")

# or

# By Name¶
cheese = driver.find_element_by_name("cheese")

# or

from selenium.webdriver.common.by import By
cheese = driver.find_element(By.NAME, "cheese")

# By Link Text¶
cheese = driver.find_element_by_link_text("cheese")

# or

from selenium.webdriver.common.by import By
cheese = driver.find_element(By.LINK_TEXT, "cheese")


from selenium.webdriver.common.by import By
frame = driver.find_element(By.TAG_NAME, "iframe")
# By Partial Link Text
cheese = driver.find_element_by_partial_link_text("cheese")

# or

from selenium.webdriver.common.by import By
cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")
# By CSS¶
cheese = driver.find_element_by_css_selector("#food span.dairy.aged")

# or

from selenium.webdriver.common.by import By
cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

# By XPATH


# Driver	Tag and Attribute Name	Attribute Values	Native XPath Support
# HtmlUnit Driver	Lower-cased	As they appear in the HTML	Yes
# Internet Explorer Driver	Lower-cased	As they appear in the HTML	No
# Firefox Driver	Case insensitive	As they appear in the HTML	Yes

inputs = driver.find_elements_by_xpath("//input")

# or

from selenium.webdriver.common.by import By
inputs = driver.find_elements(By.XPATH, "//input")

# Using JavaScript
labels = driver.find_elements_by_tag_name("label")
inputs = driver.execute_script(
    "var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" +
    "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)


# User Input - Filling In Forms
select = driver.find_element_by_tag_name("select")
allOptions = select.find_elements_by_tag_name("option")
for option in allOptions:
    print "Value is: " + option.get_attribute("value")
    option.click()

# available since 2.12
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_tag_name("select"))
select.deselect_all()
select.select_by_visible_text("Edam")

driver.find_element_by_id("submit").click()

element.submit()


# Moving Between Windows and Frames¶
driver.switch_to.window("windowName")

for handle in driver.window_handles:
    driver.switch_to.window(handle)

driver.switch_to.frame("frameName")


# Popup Dialogs
alert = driver.switch_to.alert
# usage: alert.dismiss(), etc.


# Navigation: History and Location
driver.get("http://www.example.com")  # python doesn't have driver.navigate
driver.forward()
driver.back()

# Cookies¶
# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. Here's one for the entire domain
# the cookie name here is 'key' and its value is 'value'
driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})
# additional keys that can be passed in are:
# 'domain' -> String,
# 'secure' -> Boolean,
# 'expiry' -> Milliseconds since the Epoch it should expire.

# And now output all the available cookies for the current URL
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

# You can delete cookies in 2 ways
# By name
driver.delete_cookie("CookieName")
# Or all of them
driver.delete_all_cookies()

# Changing the User Agent
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "some UA string")
driver = webdriver.Firefox(profile)


# Drag And Drop
from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_name("source")
target =  driver.find_element_by_name("target")

ActionChains(driver).drag_and_drop(element, target).perform()
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()