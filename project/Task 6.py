from selenium import webdriver
import time
from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.Actions import Actions

#chromedriver = r'C:\Users\USER4\Desktop\New folder\chromedriver.exe'
chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

names = []
color = []
quantity = []
price = []

# Adding products to the cart and keeping it's details in lists.
Main_Page(driver).click_tablets()
Category_Page(driver).focus_on_a_product(2).click()
Actions.remember_details(driver, names, price, color, quantity)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_laptops()
Category_Page(driver).focus_on_a_product(0).click()
Actions.remember_details(driver, names, price, color, quantity)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_cart()

# Editing the products' quantity.
time.sleep(5)
Cart_Page(driver).edit_product_from_cart(0)
Actions.change_quantity(driver, 3)
Product_Page(driver).add_to_cart()

time.sleep(5)
Cart_Page(driver).edit_product_from_cart(1)
Actions.change_quantity(driver, 5)
Product_Page(driver).add_to_cart()

# Keeping the new information in different lists.
changes = Cart_Page(driver).cart_products_details()

print(names, color, quantity, price)
print(changes)

if names == changes[0] and color == changes[1] and changes[2] == [3, 5] and changes[3] == [price[0]*3, price[1]*5]:
    print('test passed')
else:
    print('test failed')
