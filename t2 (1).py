from selenium import webdriver
import time


try:
    link="http://suninjuly.github.io/registration1.html"
    browser=webdriver.Chrome()
    browser.get(link)

    input1=browser.find_element_by_css_selector('.first_block input[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2=browser.find_element_by_css_selector('.first_block input[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3=browser.find_element_by_css_selector('.first_block input[placeholder="Input your email"]')
    input3.send_keys("121@mail.ru")
  
    button=browser.find_element_by_tag_name("button")
    
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt=browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text=welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!"==welcome_text
    
finally:
    # успеваем скопировать код за 30 сек
    time.sleep(5)
    # закрываем браузер
    browser.quit()

