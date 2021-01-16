from selenium import webdriver
import time
# from config import DRIVER_PATH
# from config import URL
from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

def remember_details(driver, names, price, colors, quantity):
    """this function remember the details about products before adding to the cart
       specely for task 2
    """
    quantity.append(Product_Page(driver).product_quanity())
    names.append(Product_Page(driver).product_name())
    price.append(Product_Page(driver).product_price())
    colors.append(Product_Page(driver).product_color())


driver = webdriver.Chrome(executable_path= r"D:\python\chromedriver.exe")
#driver = webdriver.Chrome(executable_path= DRIVER_PATH)
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
time.sleep(3)

"""this opening is match to task 1 - 6. opening for task 7 will be down there"""
"""
names = []
quantity = []
price = []
colors = []
# add 3 products to the cart
for i in range(0,4,1):
    # Go into the mice page
    Main_Page(driver).click_mice()
    # choose an product
    Category_Page(driver).focus_on_a_product(i).click()
    # add amount
    for t in range(1, i, 1):
        Product_Page(driver).add_one()
    # keeps it's values for Q2
    remember_details(driver,names,price,colors,quantity)
    # add product to the cart
    Product_Page(driver).add_to_cart()
    # try to go back to the main page
    Product_Page(driver).click_main_page()
time.sleep(2)
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
"""
# ###############################################################################
# """FIRST TASK"""
# ###############################################################################
'''
def values_from_a_table(table_css_selector, place):
    """this function gets a table's css_selectors, place of the value you want.
       the function return the value in a list.
       in this case it's calculat how much products are in the cart
    """
    table = driver.find_element_by_css_selector(f"{table_css_selector}")
    rows = table.find_elements_by_tag_name("tr")
    answer = []
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        for i in range(len(cells)):
            if i == place and i != len(cells) - 1:
                answer.append(cells[i].text)
    return answer


y = values_from_a_table( "[class='fixedTableEdgeCompatibility']", 4)
total_amount = 0
for i in y:
    total_amount += int(i)
if total_amount == int(driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text):
    print("True")

'''
# ################################################################
# """FIRST TASK ARE DONE!"""
# ################################################################
# """task 2"""
# ################################################################
"""
# get access to the pop-up-table
table = driver.find_element_by_css_selector("[ng-show='cart.productsInCart.length > 0']")
# get access to the table's rows. get list of lists
rows = table.find_elements_by_tag_name("tr")
pop_up_products_names = []
pop_up_products_color = []
pop_up_products_quantity =[]
pop_up_products_price = []
# run all over the list's list
for row in rows:
    # Defines list of cells
    cells = row.find_elements_by_tag_name("td")
    # run through all the cells
    for i in range(len(cells)):
        if i == 1 and i != len(cells) - 1:
            # collect information about the product
            pop_up_products_names.append(cells[i].find_element_by_tag_name("h3").text)
            pop_up_products_color.append(cells[i].find_elements_by_class_name("ng-binding")[2].find_element_by_tag_name("span").text)
            pop_up_products_quantity.append(cells[i].find_element_by_tag_name("label").text)
        if i == 2:
            pop_up_products_price.append(cells[i].find_element_by_tag_name("p").text)
            # clean the quantity list to only number
for i in range(len(pop_up_products_quantity)):
    pop_up_products_quantity[i].split()
    pop_up_products_quantity[i] = pop_up_products_quantity[i].split()[1]
    #while information are go into the cart it goes upside down so we do the same for the lists.
    #important to keep transitivation - all the pop-up lists are gonna be upside down or the other lists
if pop_up_products_names == names[::-1]:
    print("True")
else:
    print("False")
if pop_up_products_quantity == quantity[::-1]:
    print("True")
else:
    print("False")
for i in range(len(price)):
    price[i] = price[i].replace("$","")
for i in range(len(pop_up_products_price)):
    pop_up_products_price[i] = float(pop_up_products_price[i].replace("$",""))
total_price = []
for i in range(len(price)):
    total_price.append(float(price[i])*float(quantity[i]))
if total_price[::-1] == pop_up_products_price:
    print("True")
else:
    print("False")
if colors[::-1] == pop_up_products_color:
    print("True")
else:
    print("False")
"""
# ##################################################
# """DONE!"""
# ##################################################
# #gets values from the table at the cart page
# table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
# rows = table.find_elements_by_tag_name("tr")
# products_names = []
# products_color = []
# products_quantity =[]
# products_price = []
# for row in rows:
#     cells = row.find_elements_by_tag_name("td")
#     for i in range(len(cells)):
#         # if i == 1 and i != len(cells) - 1:
#         #     products_names.append(cells[i].text)
#         # if i == 3 and i != len(cells) - 1:
#         #     products_color.append(cells[i].find_element_by_tag_name("span").get_attribute("title"))
#         if i == 4 and i != len(cells) -1:
#             products_quantity.append(cells[i].text)
#         if i == 5:
#             products_price.append(cells[i].find_element_by_tag_name("p").text)

# if pop_up_products_quantity == products_quantity:
#     print("equal quantity")
# else:
#     print("not equal quantity")
# if products_color == pop_up_products_color:
#     print("equal colors")
# else:
#     print("not equal colors")
# if pop_up_products_names == products_names:
#     print("same names")
# else:
#     print("not same names")
# if pop_up_products_price == products_price:
#     print("same price")
# else:
#     print("not same price")
# ##################################################
# """DONE!"""
# ##################################################
# """task 5""" what should I show? back here later
# ##################################################
# #gets values from the table at the cart page
"""
table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
rows = table.find_elements_by_tag_name("tr")
products_names = []
products_color = []
products_quantity =[]
products_price = []
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for i in range(len(cells)):
        # if i == 1 and i != len(cells) - 1:
        #     products_names.append(cells[i].text)
        # if i == 3 and i != len(cells) - 1:
        #     products_color.append(cells[i].find_element_by_tag_name("span").get_attribute("title"))
        if i == 4 and i != len(cells) -1:
            products_quantity.append(cells[i].text)
        if i == 5:
            products_price.append(cells[i].find_element_by_tag_name("p").text)

products_number = 0
count_price = 0
for i in products_quantity:
    products_number += int(i)
print(products_number)
for i in range(len(products_price)):
     count_price += float(products_price[i].replace("$",""))
print(count_price)
#access to the price in the cart shopping
#if i print count price the cart price does not shown and the oposite.

print(driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text.replace("$",""))
# pricr_pop_up = driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text
cart_price = driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text.replace("$","")
if cart_price == count_price:
    print("True")
elif cart_price - count_price < 0.1:
    print("True")
else:
    print("False")
"""
# ################################################################
# """task 7"""
# ################################################################
"""
Main_Page(driver).click_tablets()
Category_Page(driver).focus_on_a_product(1).click()
Product_Page(driver).add_to_cart()
Product_Page(driver).back_to_category_page()
if driver.current_url == "https://www.advantageonlineshopping.com/#/category/Tablet/3":
    print("True")
Category_Page(driver).focus_main_page()
if driver.current_url == "https://www.advantageonlineshopping.com/#/":
    print("True")
"""
# # ################################################################
# # """DONE!"""
# # ################################################################
# # ################################################################
# # """task 10"""
# # ################################################################
