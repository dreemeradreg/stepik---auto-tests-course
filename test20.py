
#		# *****************************************************************************************
#		# пробный вариант сиди разбирайся 
#		# *****************************************************************************************
# def test_input_text(expected_result, actual_result):
# 	assert abs(expected_result) == actual_result, "expected {}, got {}".format(expected_result, actual_result)


# test_input_text(8, 11)

# def test_substring(full_string, substring):

# 	assert full_string in substring, "expected {} to be substring of {}".format(full_string, substring)


# # s = 'My Name is Julia'

# # if 'Name' in s:
# #     print('Substring found')

# # index = s.find('Name')
# # if index != -1:
# #     print(f'Substring found at index {index}')
#		# *****************************************************************************************


#		# *****************************************************************************************
#		# работает как должнор и падает с ошибкой
#		# *****************************************************************************************
# import unittest

# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
# if __name__ == "__main__":
#     unittest.main()
#		# *****************************************************************************************




# 		# *****************************************************************************************
# 		# не всё работает но работает как должно
# 		# *****************************************************************************************
# import pytest

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException


# def test_exception1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally: 
#         browser.quit()

# def test_exception2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("no_such_button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally: 
#         browser.quit()


# def main():
# 	test_exception2()
# 	test_exception1()

# if __name__ == "__main__":
# 	main()
# 		# *****************************************************************************************





# 		# *****************************************************************************************
# 		# всё работает и проверяет
# 		# *****************************************************************************************
# import unittest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# class TestMainPage1():

#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.Chrome()

#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()

#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# class TestMainPage2():

#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()

#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()

#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# if __name__ == "__main__":
#     unittest.main()
# 		# *****************************************************************************************



# 		# *****************************************************************************************
# 		# *****************************************************************************************
# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     return browser


# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#  		# *****************************************************************************************




#  		# *****************************************************************************************
#  		# *****************************************************************************************
# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1(object):
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#  		# *****************************************************************************************


#  		# *****************************************************************************************
#  		# *****************************************************************************************
# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():

#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         print("finish test1")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#         print("finish test2")
#  		# *****************************************************************************************



#  		# *****************************************************************************************
#		# дз 
#  		# *****************************************************************************************


# import pytest
# from selenium import webdriver

# link = "http://selenium1py.pythonanywhere.com/"

# @pytest.fixture(scope="class")
# def prepare_faces():
#     print("^_^", "\n")
#     browser = webdriver.Chrome()
#     yield
#     print(":3", "\n")
#     browser.quit()


# @pytest.fixture()
# def very_important_fixture():
#     print(":)", "\n")
#     browser = webdriver.Chrome()


# @pytest.fixture(autouse=True)
# def print_smiling_faces():
#     print(":-Р", "\n")
#     browser = webdriver.Chrome()


# class TestPrintSmilingFaces():
#     def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         # какие-то проверки

#     def test_second_smiling_faces(self, prepare_faces):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")        
        # какие-то проверки
#  		# *****************************************************************************************


#  		# *****************************************************************************************
#  		# ****************************DZ
#  		# *****************************************************************************************

# import pytest

# # @pytest.mark.xfail(run=False)
# @pytest.mark.xfail(strict=True)
# def test_succeed():
#     assert True

# @pytest.mark.xfail
# def test_not_succeed():
#     assert False

# @pytest.mark.skip
# def test_skipped():
#     assert False
#  		# *****************************************************************************************








# import pytest


# class TestMainPage():
#     # номер 1
#     @pytest.mark.xfail
#     @pytest.mark.smoke
#     def test_guest_can_login(self, browser):
#         assert True

#     # номер 2
#     @pytest.mark.regression
#     def test_guest_can_add_book_from_catalog_to_basket(self, browser):
#         assert True


# class TestBasket():
#     # номер 3
#     @pytest.mark.skip(reason="not implemented yet")
#     @pytest.mark.smoke
#     def test_guest_can_go_to_payment_page(self, browser):
#         assert True

#     # номер 4
#     @pytest.mark.smoke
#     def test_guest_can_see_total_price(self, browser):
#         assert True


# @pytest.mark.skip
# class TestBookPage():
#     # номер 5
#     @pytest.mark.smoke
#     def test_guest_can_add_book_to_basket(self, browser):
#         assert True

#     # номер 6
#     @pytest.mark.regression
#     def test_guest_can_see_book_price(self, browser):
#         assert True


# # номер 7
# @pytest.mark.beta_users
# @pytest.mark.smoke
# def test_guest_can_open_gadget_catalogue(browser):
#     assert True




