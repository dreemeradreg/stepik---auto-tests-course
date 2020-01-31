from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def func(block, method, query, text):
    field = block.find_element(method, query)
    field.send_keys(text)


def check(link):
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        lst_required = [
            (By.CLASS_NAME, "first", "Ivan"),
            (By.CLASS_NAME, "second", "Grigoriev"),
            (By.CLASS_NAME, "third", "ari")
        ]

        required_div = browser.find_element_by_class_name("first_block")
        [func(required_div, *i) for i in lst_required]
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(2)
        browser.quit()

check("http://suninjuly.github.io/registration1.html")
check("http://suninjuly.github.io/registration2.html")


