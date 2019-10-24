
from selenium import webdriver
import math
import os 
import time 
from selenium.webdriver.common.keys import Keys
import re

link = "http://orteil.dashnet.org/cookieclicker/"
browser = webdriver.Chrome()
browser.get(link)
# time.sleep(5)
		
b = ""
c = ""
d = ""
e = ""


i = 1
while True:
	cookie = browser.find_element_by_id('cookies')
	a = cookie.text
	print(a)
	# product2 = browser.find_element_by_id("productPrice2")
	# d = product2.text
	# print(d)
	reg = re.compile('[^a-zA-Z ]')



	if a >= b:
		product0 = browser.find_element_by_id("product0").click()
		prod0 = browser.find_element_by_id("productPrice0")
		b = prod0.text
	if a >= c:
		product1 = browser.find_element_by_id("product1").click()
		prod1 = browser.find_element_by_id("productPrice1")
		c = prod1.text
	if i > 900:		
		if a >= d:
			product2 = browser.find_element_by_id("product2").click()
			prod2 = browser.find_element_by_id("productPrice2")
			d = prod2.text
		if i > 15000:	
			if a >= e:
				product3 = browser.find_element_by_id("product3").click()
				prod3 = browser.find_element_by_id("productPrice3")
				e = prod3.text
			
	button = browser.find_element_by_id('cookieAnchor').click()
	print("нажато = ", i)
	i += 1
	


time.sleep(5)
browser.quit()
