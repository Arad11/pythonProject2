from selenium import webdriver

from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page

chromedriver = r'C:\Users\USER4\Desktop\New folder\chromedriver.exe'
#chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

Main_Page(driver).click_speakers()
Category_Page(driver).focus_on_a_product(2).click()
Product_Page(driver).add_to_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_mice()
Category_Page(driver).focus_on_a_product(4).click()
Product_Page(driver).add_to_cart()

Main_Page(driver).click_cart()
header = driver.find_element_by_css_selector('a[class="select  ng-binding"]')

if header.text == 'SHOPPING CART':
    print('test passed')
else:
    print('test failed')