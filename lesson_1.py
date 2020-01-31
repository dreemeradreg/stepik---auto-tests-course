# coding : utf-8


from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
































# import os
# import sys
# import psutil
# import shutil
# import random
# import turtle
# print("привет")
# print("")
# # turtle.speed(0)
# # turtle.circle(20)
# mass = [3,4,5,6,7,8,9,10,11]

# h = 0
# z = ''

# m = random.randint(0,9)
# h += mass[m]
# print("карта на руках", mass[m], "\n")
	
# m = random.randint(0,9)
# h += mass[m]
# print("карта на руках", mass[m], "\n")
# print("сумма", h , "\n")

# while z != 'n':
# 	z = input("да или нет\n")
# 	m = random.randint(0,9)
# 	h += mass[m]
# 	print("ещё карта", mass[m])
# 	print(" ")
# 	print("сумма",h)
# 	print(" ")
# 	print("*"*20)
# 	if h > 21:
# 		print("ты всрал катку\n")
# 		z = 'n'


# print("*"* 25)

