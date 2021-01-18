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
from project.general_functions import General


# chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
# driver = webdriver.Chrome(chromedriver)

# driver.get("http://advantageonlineshopping.com/#/")
# driver.maximize_window()

# driver.implicitly_wait(10)

driver = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

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

product1_data = []
product1_data.append(Product_Page(driver).product_name())
product1_data.append(Product_Page(driver).product_color())
product1_data.append(Product_Page(driver).product_quantity())
product1_data.append(Product_Page(driver).product_price())

General(driver).change_quantity(3)
Product_Page(driver).add_to_cart()
Cart_Page(driver).edit_product_from_cart(1)

product2_data = []
product2_data.append(Product_Page(driver).product_name())
product2_data.append(Product_Page(driver).product_color())
product2_data.append(Product_Page(driver).product_quantity())
product2_data.append(Product_Page(driver).product_price())

General(driver).change_quantity(5)
Product_Page(driver).add_to_cart()

table = driver.find_element_by_css_selector('table[class="fixedTableEdgeCompatibility"]')
rows = table.find_elements_by_tag_name("tr")
data1 = []
data2 = []

for row in range(len(rows)):
    if row == 0:
        cells = rows[row].find_elements_by_tag_name("td")
        for i in range(len(cells)):
            if i == 1 and i != len(cells) - 1:
                data1.append(cells[i].find_element_by_tag_name("label").text)
            if i == 3:
                data1.append(cells[i].find_element_by_css_selector('label[class="roboto-light mobileViewer ng-binding"]').text)
            if i == 4:
                data1.append(cells[i].find_element_by_css_selector("label[class='ng-binding']").text)
            if i == 5:
                data1.append(cells[i].find_element_by_tag_name("p").text)

    if row == 1:
        cells = rows[row].find_elements_by_tag_name("td")
        for i in range(len(cells)):
            if i == 1 and i != len(cells) - 1:
                data2.append(cells[i].find_element_by_tag_name("label").text)
            if i == 3:
                data1.append(cells[i].find_element_by_css_selector('label[class="roboto-light mobileViewer ng-binding"]').text)
            if i == 4:
                data1.append(cells[i].find_element_by_css_selector("label[class='ng-binding']").text)
            if i == 5:
                data2.append(cells[i].find_element_by_tag_name("p").text)

print(product1_data)
print(product2_data)
print('------------------')
print(data1)
print(data2)

if product1_data[0] == data1[0] and product1_data[1] == data1[1] and data1[2] == 3 and product1_data[0]*3 == data1[3]:
    print('product 1 - test passed')
else:
    print('product 1 - test failed')

if product2_data[0] == data2[0] and product2_data[1] == data2[1] and data2[2] == 5 and product2_data[0]*5 == data2[3]:
    print('product 2 - test passed')
else:
    print('product 2 - test failed')