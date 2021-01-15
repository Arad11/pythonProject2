# from selenium import webdriver
# import pytest
# from config import DRIVER_PATH
# from project.Main_Page import Main_Page
#
# # class TestMain_Page():
#
# @pytest.fixture
# def browser():
#     # Initialize ChromeDriver
#     driver = webdriver.Chrome(executable_path = DRIVER_PATH)
#     # Wait implicitly for elements to be ready before attempting interactions
#     driver.implicitly_wait(10)
#
#     # Return the driver object at the end of setup
#     #return few times
#     yield driver
#
#     # For cleanup, quit the driver
#     driver.quit()
#
# def test_go_to_category_page(browser):
#     print(browser)
#     main_page = Main_Page(browser)
#     main_page.load()
#     main_page.go_to_category_page("speakers")
#
#
# """
# testproject
# selenium python example
# pytest
# objects model page
# """