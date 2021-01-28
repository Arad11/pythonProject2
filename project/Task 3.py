from selenium import webdriver

from project.Main_Page import Main_Page
from project.Cart_Page import Cart_Page
from project.Actions import Actions


chromedriver = r'C:\Users\USER4\Desktop\New folder\chromedriver.exe'
#chromedriver = '/Users/nitzanwexler/Desktop/QA/selenium/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("http://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)

Actions.add_3_products('mice')

names = []
colors = []
quantity = []
price = []
Actions().take_details_from_pop_up_cart(names, colors, quantity, price)

Main_Page(driver).click_cart()

deleted_product_name = [driver.find_element_by_css_selector("h3[class='ng-binding']").text]
Cart_Page(driver).remove_product_from_cart()

Main_Page(driver).click_main_page()

Main_Page(driver).click_cart()

names2 = []
colors2 = []
quantity2 = []
price2 = []
Actions().take_details_from_pop_up_cart(names2, colors2, quantity2, price2)

if names != names2 and deleted_product_name not in names2:
    print('test passed')
else:
    print('test failed')