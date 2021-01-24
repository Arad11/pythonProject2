from selenium import webdriver

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
from project.general_functions import General
from project.Actions import Actions

# outside functions are not running
chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)


Main_Page(driver).click_tablets()
Category_Page(driver).focus_on_a_product(2)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_tablets()
Category_Page(driver).focus_on_a_product(0)
Product_Page(driver).add_to_cart()

Main_Page(driver).click_cart()

Cart_Page(driver).edit_product_from_cart(0)
Product_Page(driver).add_to_cart()

Cart_Page(driver).edit_product_from_cart(0)

names = [Product_Page(driver).product_name()]
color = [Product_Page(driver).product_color()]
quantity = [Product_Page(driver).product_quantity()]
price = [Product_Page(driver).product_price()]


General(driver).change_quantity(3)
Product_Page(driver).add_to_cart()
Cart_Page(driver).edit_product_from_cart(1)

names.append(Product_Page(driver).product_name())
color.append(Product_Page(driver).product_color())
quantity.append(Product_Page(driver).product_quantity())
price.append(Product_Page(driver).product_price())

General(driver).change_quantity(5)
Product_Page(driver).add_to_cart()

names2 = [Actions().values_from_a_table('table[class="fixedTableEdgeCompatibility"]', 1)]
color2 = [Actions().values_from_a_table('table[class="fixedTableEdgeCompatibility"]', 3)]
quantity2 = [Actions().values_from_a_table('table[class="fixedTableEdgeCompatibility"]', 4)]
price2 = [Actions().values_from_a_table('table[class="fixedTableEdgeCompatibility"]', 5)]

if names == names2 and color == color2 and quantity2 == [3, 5] and price2 == [price[0]*3, price[1]*5]:
    print('test passed')
else:
    print('test failed')




# table = driver.find_element_by_css_selector('table[class="fixedTableEdgeCompatibility"]')
# rows = table.find_elements_by_tag_name("tr")
#
#
# for row in range(len(rows)):
#     if row == 0:
#         cells = rows[row].find_elements_by_tag_name("td")
#         for i in range(len(cells)):
#             if i == 1 and i != len(cells) - 1:
#                 data1.append(cells[i].find_element_by_tag_name("label").text)
#             if i == 3:
#                 data1.append(cells[i].find_element_by_css_selector('label[class="roboto-light mobileViewer ng-binding"]').text)
#             if i == 4:
#                 data1.append(cells[i].find_element_by_css_selector("label[class='ng-binding']").text)
#             if i == 5:
#                 data1.append(cells[i].find_element_by_tag_name("p").text)
#
#     if row == 1:
#         cells = rows[row].find_elements_by_tag_name("td")
#         for i in range(len(cells)):
#             if i == 1 and i != len(cells) - 1:
#                 data2.append(cells[i].find_element_by_tag_name("label").text)
#             if i == 3:
#                 data1.append(cells[i].find_element_by_css_selector('label[class="roboto-light mobileViewer ng-binding"]').text)
#             if i == 4:
#                 data1.append(cells[i].find_element_by_css_selector("label[class='ng-binding']").text)
#             if i == 5:
#                 data2.append(cells[i].find_element_by_tag_name("p").text)
#
# print(product1_data)
# print(product2_data)
# print('------------------')
# print(data1)
# print(data2)
