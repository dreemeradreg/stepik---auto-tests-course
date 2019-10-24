
from selenium import webdriver
import math
import os 
import time 
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	# загрузка драйвера и открытие страницы
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	#  самая орная часть
	browser.execute_script("alert('Robots at work');")
	alert = browser.switch_to.alert
	time.sleep(2)
	alert.accept()
	# поиск элемента и значения для уравнения
	input1 = browser.find_element_by_id('input_value')
	print(input1) # выведет то число которое было в уравнении х
	x = input1.text
	y = calc(x)
	
	# водим значение
	input2 = browser.find_element_by_id('answer')
	input2.send_keys(y)
	# жмакаем копочку
	option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
	option1.click()
 	# ***************************************************************************************
	# 
	# прокрутка
	browser.execute_script("window.scrollBy(0, 100);")
	# прокрутка до указанного элемента
	# button = browser.find_element_by_tag_name("button")
	# browser.execute_script("return arguments[0].scrollIntoView(true);", button).click()
	# 
	# 
	# ***************************************************************************************
	# жмакаем вторую кнопочку
	option1 = browser.find_element_by_css_selector("[id='robotsRule']").click()


	# button = browser.find_element_by_css_selector("button.btn")
	# button.click()

	# подтверждаем
	button = browser.find_element_by_tag_name("button").click()
	alert = browser.switch_to.alert
	alert_text = alert.text
	print(" ")
	print(alert_text)
finally:
	# time.sleep(10)
	browser.quit()

