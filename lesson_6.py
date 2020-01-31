# 

from selenium import webdriver
import time
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_element_by_id('num1')
	a = int(input1.text)
	input2 = browser.find_element_by_id('num2')
	b = int(input2.text)
	x = a + b
	print(x)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(x))
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
finally:
	time.sleep(8)
	browser.quit()

#