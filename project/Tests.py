from selenium import webdriver
import time
from project.User_POP_Up import User_Pop_Up
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from config import DRIVER_PATH
from selenium.webdriver.support.ui import WebDriverWait
from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.Cart_Page import Cart_Page
driver = webdriver.Chrome(executable_path= r"D:\python\chromedriver.exe")
#driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
time.sleep(3)


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
    # add product to the cart
    Product_Page(driver).add_to_cart()
    # try to go back to the main page
    Product_Page(driver).click_main_page()
time.sleep(2)
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()

y = values_from_a_table( "[class='fixedTableEdgeCompatibility']", 4)
total_amount = 0
for i in y:
    total_amount += int(i)
if total_amount == int(driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text):
    print("True")
