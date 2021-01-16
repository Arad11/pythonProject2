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


# Main_Page(driver).click_mice()
# Category_Page(driver).focus_on_a_product(1).click()
# Product_Page(driver).add_one()
# Product_Page(driver).add_to_cart()
# driver.find_element_by_css_selector('[ng-click="go_up()"]').click()

###################################################################################################
# run it together why it does not works
# Main_Page(driver).click_mice()
# Category_Page(driver).focus_on_a_product(3).click()
# # time.sleep(5)
# # Category_Page(driver).focus_main_page().click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR('div[class="logo"]')))
# driver.find_element_by_css_selector('div[class="logo"]').click()
###################################################################################################
# print(Product_Page(driver).product_color())
# Main_Page(driver).creat_user_new_user_pop_up()
# li = driver.find_elements_by_css_selector('[ng-show="welcome"]>nav>ul>li')
# for i in range(1, len(li) + 1, 1):
#     if i == 3:
#         li[i].click()
#         break
time.sleep(2)
driver.find_element_by_id('menuUserLink').click()
User_Pop_Up(driver).inser_user_name()
User_Pop_Up(driver).insert_user_password()
User_Pop_Up(driver).sign_in()
