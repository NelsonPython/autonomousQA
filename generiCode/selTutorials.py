'''
Tutorial for using  Selenium locators

Locator 	Description
class name 	Locates elements whose class name contains the search value (compound class names are not permitted)
css selector 	Locates elements matching a CSS selector
id 		Locates elements whose ID attribute matches the search value
name 		Locates elements whose NAME attribute matches the search value
link text 	Locates anchor elements whose visible text matches the search value
partial link text 	Locates anchor elements whose visible text matches the search value
tag name 	Locates elements whose tag name matches the search value
xpath 		Locates elements matching an XPath expression

Best practice:
1. id
2. css selector
3. other locator types

get_attribute('innerHTML')
get_attribute('value')      # input elements
get_attribute('text')       # text

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("file:///home/iotahub/testNGG/test.html")

print("FIND_ELEMENT_BY_ID")
print('Finding a list of cheeses: \n', driver.find_element_by_id("cheese"))
cheeses = driver.find_element_by_id("cheese")
# cheeses is not a list
cheddar = cheeses.find_element_by_id("cheddar")
print("\nChedder results\n ", cheddar)
print("Cheddar text ", cheddar.text)
print("Cheddar tag_name ", cheddar.tag_name)
print("Cheddar innerHTML ", cheddar.get_attribute('innerHTML'))

print("\n\nFIND_ELEMENT_BY_CSS_SELECTOR")
mucho_cheeses = driver.find_elements_by_css_selector("#cheese li")
print("\nMucho_cheeses:\n")
for mucho_cheese in mucho_cheeses:
	print(mucho_cheese.text)

cheddar2 = driver.find_element_by_css_selector("#cheese #cheddar")
print("\nCheddar2 ",cheddar2.text)
goat = driver.find_element_by_css_selector("#cheese #goat")
print("\nGoat ",goat.text)

print("__dict__ ", cheddar2.__dict__)


# print all the attributes for a web element - CAUTION - lots of data
attrs = driver.execute_script(
    'var element = arguments[0];'
    'var attributes = {};'
    'for (index = 0; index < element.attributes.length; ++index) {'
    '    attributes[element.attributes[index].name] = element.attributes[index].value };'
    'var properties = [];'
    'properties[0] = attributes;'
    'var element_text = element.textContent;'
    'properties[1] = element_text;'
    'var styles = getComputedStyle(element);'
    'var computed_styles = {};'
    'for (index = 0; index < styles.length; ++index) {'
    '    var value_ = styles.getPropertyValue(styles[index]);'
    '    computed_styles[styles[index]] = value_ };'
    'properties[2] = computed_styles;'
    'return properties;', cheddar2)

#print("\nElement attributes")
#for attr in attrs:
#	print(attr)


driver.quit()

