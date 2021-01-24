from selenium import webdriver
import time

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.general_functions import General
from project.Actions import Actions
from project.CheckOut import CheckOut
from project.My_Orders import My_Orders


chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

Main_Page(driver).click_speakers()
Category_Page(driver).focus_on_a_product(2).click()
product1 = [Product_Page(driver).product_name(), Product_Page(driver).product_quantity(), Product_Page(driver).product_color()]
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_mice()
Category_Page(driver).focus_on_a_product(4).click()
product2 = [Product_Page(driver).product_name(), Product_Page(driver).product_quantity(), Product_Page(driver).product_color()]
Product_Page(driver).add_to_cart()
Main_Page(driver).click_cart()

Cart_Page(driver).check_out()

CheckOut(driver).insert_username_in_payment('aaAA11')
CheckOut(driver).insert_password_in_payment('aaAA11')
CheckOut(driver).log_in()

CheckOut(driver).next()
CheckOut(driver).masterCredit()
CheckOut(driver).edit_details()
CheckOut(driver).enter_card_num('1234567891234567')
CheckOut(driver).enter_cvv_number('123')
CheckOut(driver).enter_expiration_mm('01')
CheckOut(driver).enter_expiration_yy('2022')
CheckOut(driver).enter_cardholder_name('nitzan')
CheckOut(driver).pay_now_masterCredit()

header_payment = driver.find_element_by_css_selector("[translate='ORDER_PAYMENT']").text
ordernum = driver.find_element_by_id("orderNumberLabel").text
payment_method = driver.find_elements_by_css_selector('[class="innerSeccion"]>label')[5].text
order_date = driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[1].text
subtotal = driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[2].text

if header_payment and payment_method:
    order_payment = True
else:
    order_payment = False
time.sleep(5)
Main_Page(driver).click_cart()
header_cart = driver.find_element_by_css_selector('[class="bigEmptyCart center"]>[translate="Your_shopping_cart_is_empty"]')
if header_cart:
    shopping_cart = True
else:
    shopping_cart = False

My_Orders(driver).go_to_my_orders()

detailslist = My_Orders(driver).order_details(0)
time.sleep(3)
print(detailslist)
# print(My_Orders(driver).order_details(1))
# productA = My_Orders(driver).order_product_details(0, 0)
# productB = My_Orders(driver).order_product_details(0, 1)
#
# if detailslist[0] == ordernum and detailslist[1] == order_date and detailslist[2] == subtotal:
#     details = True
# else:
#     details = False
#
# if productA[0] == product1[0] and productA[1] == product1[1] and productA[2] == product1[2]:
#     first_product = True
# else:
#     first_product = False
#
# if productB[0] == product2[0] and productB[1] == product2[1] and productB[2] == product2[2]:
#     second_product = True
# else:
#     second_product = False
#
# if order_payment and shopping_cart and details and first_product and second_product:
#     print('test passed')
# else:
#     print('test failed')
#