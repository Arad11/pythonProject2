from selenium import webdriver
import time

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.My_Orders import My_Orders
from project.CheckOut import CheckOut
from project.Registration_Page import Registration_Page
from project.Actions import Actions


# chromedriver = r'C:\Users\USER4\Desktop\New folder\chromedriver.exe'
chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

Main_Page(driver).click_speakers()
Category_Page(driver).focus_on_a_product(2).click()
product1 = [Product_Page(driver).product_name(), Product_Page(driver).product_quantity(), Product_Page(driver).product_color()]
Product_Page(driver).add_to_cart()
print(product1)

Main_Page(driver).click_main_page()

Main_Page(driver).click_mice()
Category_Page(driver).focus_on_a_product(4).click()
product2 = [Product_Page(driver).product_name(), Product_Page(driver).product_quantity(), Product_Page(driver).product_color()]
Product_Page(driver).add_to_cart()
Main_Page(driver).click_cart()
print(product2)

Cart_Page(driver).check_out()

CheckOut(driver).registration_in_payment()

Actions.details_registration_page(driver, 'Sss11', 'n@gmail.com', 'Sss11', 'sami', 'cohen', '0543008288', 'Israel', 'raanana', 'hertzel 7', 'Israel', '2774938')
time.sleep(3)
CheckOut(driver).next()

CheckOut(driver).safepay()
CheckOut(driver).safepay_username('Ss11-')
CheckOut(driver).safepay_password('Ss11')
CheckOut(driver).pay_now_safepay()

header_payment = driver.find_element_by_css_selector("[translate='ORDER_PAYMENT']").text
time.sleep(4)
payment_method = driver.find_elements_by_css_selector('[class="innerSeccion"]>label')[5].text
ordernum = driver.find_element_by_id("orderNumberLabel").text
order_date = driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[1].text
subtotal = driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[2].text
print(ordernum, order_date, subtotal, payment_method)

if payment_method == 'SafePay':
    print(1)

if header_payment == 'ORDER PAYMENT':
    print(2)

Main_Page(driver).click_cart()
header_cart = driver.find_element_by_css_selector('[class="bigEmptyCart center"]>[translate="Your_shopping_cart_is_empty"]').text
if header_cart == 'Your shopping cart is empty':
    print(3)

My_Orders(driver).go_to_my_orders()
detailslist = My_Orders(driver).order_details(1)
print(detailslist)
if detailslist[0] == ordernum:
    print(4)

if detailslist[2] == subtotal:
    print(5)

productA = My_Orders(driver).order_product_details(1, 0)
productB = My_Orders(driver).order_product_details(1, 1)
print(productA)
print(productB)
if productA[0] == product1[0]:
    print(6)

if productA[1] == product1[2]:
    print(7)

if productA[2] == product1[1]:
    print(8)

if productB[0] == product2[0]:
    print(9)

if productA[1] == product1[2]:
    print(10)

if productA[2] == product1[1]:
    print(11)







# if header_payment and payment_method:
#     order_payment = True
# else:
#     order_payment = False
#
# Main_Page(driver).click_cart()
# header_cart = driver.find_element_by_css_selector('[class="bigEmptyCart center"]>[translate="Your_shopping_cart_is_empty"]')
# if header_cart:
#     shopping_cart = True
# else:
#     shopping_cart = False
#
# My_Orders(driver).go_to_my_orders()
# detailslist = My_Orders(driver).order_details(1)
# print(detailslist)
#
# productA = My_Orders(driver).order_product_details(1, 0)
# productB = My_Orders(driver).order_product_details(1, 1)
# print(productA)
# print(productB)
#
# if detailslist[0] == ordernum and detailslist[2] == subtotal:
#     details = True
# else:
#     details = False
#
# if productA[0] == product1[0] and productA[1] == product1[2] and productA[2] == product1[1]:
#     first_product = True
# else:
#     first_product = False
#
# if productB[0] == product2[0] and productB[1] == product2[2] and productB[2] == product2[1]:
#     second_product = True
# else:
#     second_product = False
#
# if order_payment and shopping_cart and details and first_product and second_product:
#     print('test passed')
# else:
#     print('test failed')