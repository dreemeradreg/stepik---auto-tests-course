
import math
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	#  **************************************************************************
	buton = WebDriverWait(browser, 20).until(
	        EC.text_to_be_present_in_element((By.ID, "price"), "100")
		)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	browser.execute_script("window.scrollBy(0, 100);")
	
	# ************************************************************
	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	print(x)
	y = calc(x)
	input2 = browser.find_element_by_id('answer')
	input2.send_keys(y)

	#******************************************************************************
	# button1 = browser.find_element_by_id('solve')
	# botton1.click()

	button = browser.find_element_by_xpath("//button[@id='solve']")
	button.click()

	alert = browser.switch_to.alert
	alert_text = alert.text

	# reg = re.compile(r'[^a-zA-Z ]')
	# a = reg.sub('', alert_text)
	# print(" ")
	print(alert_text)

finally:	
	# time.sleep(5)
	browser.quit()

