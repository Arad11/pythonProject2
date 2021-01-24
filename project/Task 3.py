from selenium import webdriver

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.general_functions import General


chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

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

# change the function source
dict1 = General(driver).get_products_info_popup()

Main_Page(driver).click_cart()

deleted_product_name = [driver.find_element_by_css_selector("h3[class='ng-binding']").text]
Cart_Page(driver).remove_product_from_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_cart()
table = driver.find_element_by_css_selector('table[ng-show="cart.productsInCart.length > 0"]')
rows = table.find_elements_by_tag_name("tr")

# change the function source
dict2 = General(driver).get_products_info_popup()

if dict1["names"] != dict2["names"] and deleted_product_name not in dict2["names"]:
    print('test passed')
else:
    print('test failed')