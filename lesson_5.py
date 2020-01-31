# 

from selenium import webdriver
import time
import math
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# ищем элемент число
	# x_element = browser.find_element_by_id('input_value')
	input1 = browser.find_element_by_id('treasure')
	input1_aaa = input1.get_attribute("valuex")
	print(input1_aaa)
	x = input1_aaa
	y = calc(x)
	
	# водим значение
	input2 = browser.find_element_by_id('answer')
	input2.send_keys(y)
	
	option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
	option1.click()
	option1 = browser.find_element_by_css_selector("[value='robots']")
	option1.click()
	
	# people_radio = browser.find_element_by_id("peopleRule")
	# people_checked = people_radio.get_attribute("checked")
	# print("value of people radio: ", people_checked)
	# # assert people_checked is not None, "People radio is not selected by default"
	# assert people_checked == "true", "People radio is not selected by default"
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

#