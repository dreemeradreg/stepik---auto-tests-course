

from selenium import webdriver
import math
import os 
import time 
from selenium.webdriver.common.keys import Keys


try: 
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	  #мой код , который заполняет обязательные поля
	input1 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='firstname']")
	input1.send_keys("maks")
	input2 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='lastname']")
	input2.send_keys("free")
	input3 = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='email']")
	input3.send_keys("FUUUCK@pisos.ru")
											# хз как но оно работает
	# ***********************************************************************************************************************
	element = browser.find_element_by_id("file")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	# print(current_dir)
	file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
	# print(file_path)
	element.send_keys(file_path)
	# ***********************************************************************************************************************
	button = browser.find_element_by_tag_name("button").click()

	alert = browser.switch_to.alert
	alert_text = alert.text
	print(" ")
	print(alert_text)
finally:
	# time.sleep(10)
	browser.quit()



