# coding : utf-8

from selenium import webdriver
import time
#  иногда ругаеться что нет send_keys Насильстенное подключение помогало избегать подобной проблемы
from selenium.webdriver.common.keys import Keys

try: 
	# сылка на страницу с которой работаем
    link = "http://suninjuly.github.io/registration2.html"
    # подключение драйвера и открытие необходимой страницы
    browser = webdriver.Chrome()
    browser.get(link)
      #мой код , который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
    input1.send_keys("maks")
    input2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input2.send_keys("free")
    input3 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    input3.send_keys("FUUUCK@pisos.ru")

     # эксперемент для упрощения кода (провален)
    # elements = browser.find_elements_by_xpath("//input[@placeholder='Input your'")
    # for element in elements:
    #    element.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    testTxt = "Congratulations! You have successfully registered!"
    assert testTxt == welcome_text
    
     # иной вид проверки в случае успешной работы
    if testTxt == welcome_text:
    	print("200")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка после кода