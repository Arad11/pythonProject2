from selenium import webdriver
import time
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.CheckOut import CheckOut
from project.Registration_Page import Registration_Page


class Actions:
    def open_web():
        """this action opening the driver"""
        #driver = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
        driver = webdriver.Chrome(executable_path='/Users/nitzanwexler/Desktop/QA/selenium/chromedriver')
        # driver = webdriver.Chrome(executable_path= DRIVER_PATH)
        driver.implicitly_wait(10)
        driver.get("https://www.advantageonlineshopping.com/#/")
        driver.maximize_window()
        time.sleep(3)
        return driver

    def add_3_products(driver, category):
        """this action gets a driver and a category. the user will get 3 products for his cart"""
        # add 3 products to the cart
        categorys_dickt = {"speakers": "speakersImg", "tablets": "tabletsImg", "leptops": "laptopsImg", "mice": "miceImg", "headphones": "headphonesImg"}
        for i in range(0, 3, 1):
            # Go into the category page
            driver.find_element_by_id(categorys_dickt[category]).click()
            # choose an product
            Category_Page(driver).focus_on_a_product(i).click()
            # add amount
            for t in range(1, i, 1):
                Product_Page(driver).add_one()
            # add product to the cart
            Product_Page(driver).add_to_cart()
            # try to go back to the main page
            Product_Page(driver).click_main_page()

    def values_from_a_table(driver, table_css_selector, place):
        """this function gets a table's css_selectors, place of the value you want.
           the function return the value in a list.
           in this case it calculates how much products are in the cart.
        """
        table = driver.find_element_by_css_selector(table_css_selector)
        rows = table.find_elements_by_tag_name("tr")
        answer = []
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == place and i != len(cells) - 1:
                    answer.append(cells[i].text)
        return answer

    def remember_details(driver, names, price, colors, quantity):
        """this function remember the details about products before adding to the cart
        """
        quantity.append(Product_Page(driver).product_quantity())
        names.append(Product_Page(driver).product_name())
        price.append(Product_Page(driver).product_price())
        colors.append(Product_Page(driver).product_color())

    def add_3_products_and_save_details(driver, category, names, price, colors, quantity):
        """this action gets a driver category and 4 lists. the user will get 3 products for his cart and information
        about products he chose """
        # add 3 products to the cart
        categories_dickt = {"speakers": "speakersImg", "tablets": "tabletsImg", "leptops": "laptopsImg", "mice": "miceImg", "headphones": "headphonesImg"}
        for i in range(0, 3, 1):
            # Go into the category page
            driver.find_element_by_id(categories_dickt[category]).click()
            # choose an product
            Category_Page(driver).focus_on_a_product(i).click()
            # add amount
            for t in range(1, i, 1):
                Product_Page(driver).add_one()
            Actions.remember_details(driver,names,price,colors,quantity)
            # add product to the cart
            Product_Page(driver).add_to_cart()
            # try to go back to the main page
            Product_Page(driver).click_main_page()

    def take_details_from_pop_up_cart(driver, names, colors, quantity, price):
        """this action takes all details about the products from the pop up cart"""
        # get access to the pop-up-table
        table = driver.find_element_by_css_selector("[ng-show='cart.productsInCart.length > 0']")
        # get access to the table's rows. get list of lists
        rows = table.find_elements_by_tag_name("tr")
        # run all over the list's list
        for row in rows:
            # Defines list of cells
            cells = row.find_elements_by_tag_name("td")
            # run through all the cells
            for i in range(len(cells)):
                if i == 1 and i != len(cells) - 1:
                    # collect information about the product
                    names.append(cells[i].find_element_by_tag_name("h3").text)
                    colors.append(cells[i].find_elements_by_class_name("ng-binding")[2].find_element_by_tag_name("span").text)
                    quantity.append(cells[i].find_element_by_tag_name("label").text)
                if i == 2:
                    price.append(cells[i].find_element_by_tag_name("p").text)

    def change_quantity(driver, quantity):
        """This action changes the product's quantity in the product's page."""
        driver.find_element_by_name("quantity").click()
        driver.find_element_by_name("quantity").send_keys(quantity)

    def checkout_details(driver, card_num, cvv_number, expiration_mm, expiration_yy, cardholder_name):
        """This action fills the masterCredit's details in the CheckOut page."""
        CheckOut(driver).next()
        CheckOut(driver).masterCredit()
        CheckOut(driver).edit_details()
        CheckOut(driver).enter_card_num(card_num)
        CheckOut(driver).enter_cvv_number(cvv_number)
        CheckOut(driver).enter_expiration_mm(expiration_mm)
        CheckOut(driver).enter_expiration_yy(expiration_yy)
        CheckOut(driver).enter_cardholder_name(cardholder_name)
        CheckOut(driver).pay_now_masterCredit()

    def details_registration_page(driver, username, email, password, first_name, last_name, phone_number, country, city, address, state, postal_code):
        """This action fills the registration's details in the CheckOut page."""
        Registration_Page(driver).enter_username(username)
        Registration_Page(driver).enter_email(email)
        Registration_Page(driver).enter_password(password)
        Registration_Page(driver).confirm_password(password)
        Registration_Page(driver).enter_first_name(first_name)
        Registration_Page(driver).enter_last_name(last_name)
        Registration_Page(driver).enter_phone_number(phone_number)
        Registration_Page(driver).enter_country(country)
        Registration_Page(driver).enter_city(city)
        Registration_Page(driver).enter_address(address)
        Registration_Page(driver).enter_state(state)
        Registration_Page(driver).enter_postal_code(postal_code)
        Registration_Page(driver).agreement()
        Registration_Page(driver).register()


