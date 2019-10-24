
from selenium import webdriver
import math
import os 
import time 
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	  #мой код , который заполняет обязательные поля
	button = browser.find_element_by_tag_name("button").click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	# alert = browser.switch_to.alert
	# alert.accept()

	input1 = browser.find_element_by_id('input_value')
	print(input1) # выведет то число которое было в уравнении х
	x = input1.text
	y = calc(x)
	
	# водим значение
	input2 = browser.find_element_by_id('answer')
	input2.send_keys(y)

	button = browser.find_element_by_css_selector("button.btn").click()

	alert = browser.switch_to.alert
	alert_text = alert.text
	print(" ")
	print(alert_text)
finally:
	# time.sleep(1)
	browser.quit()

