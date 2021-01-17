from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Actions import Actions

driver = Actions.open_web()
Main_Page(driver).click_tablets()
Category_Page(driver).focus_on_a_product(1).click()
Product_Page(driver).add_to_cart()
Product_Page(driver).back_to_category_page()
if driver.current_url == "https://www.advantageonlineshopping.com/#/category/Tablet/3":
    print("True")
Category_Page(driver).focus_main_page()
if driver.current_url == "https://www.advantageonlineshopping.com/#/":
    print("True")