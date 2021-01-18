from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.AOS import remember_details
from project.general_functions import get_products_info_popup()



# chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
# driver = webdriver.Chrome(chromedriver)

# driver.get("http://advantageonlineshopping.com/#/")
# driver.maximize_window()

# driver.implicitly_wait(10)

driver = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()


Main_Page(driver).click_speakers()
Category_Page(driver).focus_on_a_product(2)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_mice()
Category_Page(driver).focus_on_a_product(4)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_mice()
Category_Page(driver).focus_on_a_product(3)
Product_Page(driver).add_to_cart()

dict1 = get_products_info_popup()

Main_Page(driver).click_cart()

deleted_product_name = [driver.find_element_by_css_selector("h3[class='ng-binding']").text]
Cart_Page(driver).remove_product_from_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_cart()
table = driver.find_element_by_css_selector('table[ng-show="cart.productsInCart.length > 0"]')
rows = table.find_elements_by_tag_name("tr")

dict2 = get_products_info_popup()

if dict1["names"] != dict2["names"] and deleted_product_name not in dict2["names"]:
    print('test passed')
else:
    print('test failed')