from unittest import TestCase
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from project.Actions import Actions
from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.User_POP_Up import User_Pop_Up
from project.CheckOut import CheckOut
from project.My_Orders import My_Orders
from project.Cart_Page import Cart_Page


class All_Tests(TestCase):
    def setUp(self):
        print("setUp")
        self.driver = Actions.open_web()

    def tearDown(self):
        print("tearDown")

    def test_1(self):
        Actions.add_3_products(self.driver, "mice")
        self.driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
        y = Actions.values_from_a_table(self.driver, "[class='fixedTableEdgeCompatibility']", 4)
        total_amount = 0
        for i in y:
            total_amount += int(i)
        self.assertEqual(total_amount, int(self.driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text))

    def test_2(self):
        names = []
        quantity = []
        price = []
        colors = []
        pop_up_products_names = []
        pop_up_products_color = []
        pop_up_products_quantity = []
        pop_up_products_price = []
        total_price = []

        Actions.add_3_products_and_save_details(self.driver, "mice", names, price, colors, quantity)
        Actions.take_details_from_pop_up_cart(self.driver, pop_up_products_names, pop_up_products_color,
                                              pop_up_products_quantity, pop_up_products_price)
        # clean the quantity list to only number
        for i in range(len(pop_up_products_quantity)):
            pop_up_products_quantity[i].split()
            pop_up_products_quantity[i] = pop_up_products_quantity[i].split()[1]

        # clean the price lists from $
        for i in range(len(price)):
            price[i] = price[i].replace("$", "")
        for i in range(len(pop_up_products_price)):
            pop_up_products_price[i] = float(pop_up_products_price[i].replace("$", ""))

        # count the total price of each product we ordered (price per unit * units)
        for i in range(len(price)):
            total_price.append(float(price[i]) * float(quantity[i]))

        # while information are go into the cart it goes upside down so we do the same for the lists.
        # important to keep transitivation - all the pop-up lists are gonna be upside down or the other lists
        self.assertEqual(pop_up_products_names, names[::-1])
        self.assertEqual(pop_up_products_quantity, quantity[::-1])
        self.assertEqual(pop_up_products_price, total_price[::-1])
        self.assertEqual(pop_up_products_color, colors[::-1])

    def test_3(self):
        Actions.add_3_products(self.driver, 'mice')
        # Making a list of the products in the cart.
        names = []
        colors = []
        quantity = []
        price = []
        Actions.take_details_from_pop_up_cart(self.driver, names, colors, quantity, price)
        Main_Page(self.driver).click_cart()

        # Delete one product from the cart and refreshing the cart's page.
        deleted_product_name = [self.driver.find_element_by_css_selector("h3[class='ng-binding']").text]
        Cart_Page(self.driver).remove_product_from_cart(2)
        Main_Page(self.driver).click_main_page()
        Main_Page(self.driver).click_cart()

        # Making a list of the products in the cart.
        names2 = []
        colors2 = []
        quantity2 = []
        price2 = []
        Actions.take_details_from_pop_up_cart(self.driver, names2, colors2, quantity2, price2)

        # Compering both lists to see that the deleted item was removed.
        self.assertNotEqual(names, names2)
        self.assertNotIn(deleted_product_name, names2)

    def test_4(self):
        # Adding products to the cart.
        Main_Page(self.driver).click_speakers()
        Category_Page(self.driver).focus_on_a_product(2).click()
        Product_Page(self.driver).add_to_cart()

        Main_Page(self.driver).click_main_page()

        Main_Page(self.driver).click_mice()
        Category_Page(self.driver).focus_on_a_product(4).click()
        Product_Page(self.driver).add_to_cart()

        # Moving to the cart's page.
        Main_Page(self.driver).click_cart()
        header = self.driver.find_element_by_css_selector('a[class="select  ng-binding"]')

        self.assertEqual(header.text, 'SHOPPING CART')

    def test_5(self):
        Actions.add_3_products(self.driver, "mice")
        time.sleep(2)
        self.driver.find_element_by_css_selector("[href='#/shoppingCart']").click()

        # gets values from the table at the cart page
        table = self.driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
        rows = table.find_elements_by_tag_name("tr")
        products_quantity = []
        products_price = []
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == 4 and i != len(cells) - 1:
                    products_quantity.append(cells[i].text)
                if i == 5:
                    products_price.append(cells[i].find_element_by_tag_name("p").text)

        products_number = 0
        count_price = 0
        # total ordered units
        for i in products_quantity:
            products_number += int(i)

        # total price
        for i in range(len(products_price)):
            count_price += float(products_price[i].replace("$", ""))

        # access to the price in the cart shopping
        cart_price = self.driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text.replace("$", "")
        print(cart_price)
        # access to the products count - pop-up
        pop_up_count = self.driver.find_element_by_css_selector('[class="roboto-regular ng-binding"]').text.split()[0]

        self.assertEqual(float(cart_price), count_price)
        self.assertEqual(int(pop_up_count[-1]), int(products_number))

    def test_6(self):
        names = []
        color = []
        quantity = []
        price = []

        # Adding products to the cart and keeping it's details in lists.
        Main_Page(self.driver).click_tablets()
        Category_Page(self.driver).focus_on_a_product(2).click()
        Actions.remember_details(self.driver, names, price, color, quantity)
        Product_Page(self.driver).add_to_cart()

        Main_Page(self.driver).click_main_page()

        Main_Page(self.driver).click_laptops()
        Category_Page(self.driver).focus_on_a_product(0).click()
        Actions.remember_details(self.driver, names, price, color, quantity)
        Product_Page(self.driver).add_to_cart()

        Main_Page(self.driver).click_cart()

        # Editing the products' quantity.
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'li>[id="toolTipCart"]' )))
        Cart_Page(self.driver).edit_product_from_cart(0)
        Actions.change_quantity(self.driver, 3)
        Product_Page(self.driver).add_to_cart()

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'li>[id="toolTipCart"]' )))
        Cart_Page(self.driver).edit_product_from_cart(1)
        Actions.change_quantity(self.driver, 5)
        Product_Page(self.driver).add_to_cart()

        # Keeping the new information in different lists.
        changes = Cart_Page(self.driver).cart_products_details()

        # Compering the lists to make sure the quantity has changed.
        self.assertEqual(names[0], changes[0][1])
        self.assertEqual(names[1], changes[0][0])
        self.assertEqual(color, changes[1])
        self.assertEqual(changes[2], [3, 5])

    def test_7(self):
        Main_Page(self.driver).click_tablets()
        Category_Page(self.driver).focus_on_a_product(1).click()
        Product_Page(self.driver).add_to_cart()
        Product_Page(self.driver).back_to_category_page()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/category/Tablet/3")
        Category_Page(self.driver).focus_main_page()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/")

    def test_8(self):

        # Adding products to the cart and keeping it's details in lists.
        Main_Page(self.driver).click_speakers()
        Category_Page(self.driver).focus_on_a_product(2).click()
        product1 = [Product_Page(self.driver).product_name(), Product_Page(self.driver).product_quantity(), Product_Page(self.driver).product_color()]
        Product_Page(self.driver).add_to_cart()

        Main_Page(self.driver).click_main_page()

        Main_Page(self.driver).click_mice()
        Category_Page(self.driver).focus_on_a_product(4).click()
        product2 = [Product_Page(self.driver).product_name(), Product_Page(self.driver).product_quantity(), Product_Page(self.driver).product_color()]
        Product_Page(self.driver).add_to_cart()
        Main_Page(self.driver).click_cart()

        # Checking out and filling the register page in the payment class.
        Cart_Page(self.driver).check_out()
        CheckOut(self.driver).registration_in_payment()
        Actions.details_registration_page(self.driver, 'Sss11', 'n@gmail.com', 'Sss11', 'sami', 'cohen', '0543008288', 'Israel', 'raanana', 'hertzel 7', 'Israel', '2774938')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'next_btn')))
        CheckOut(self.driver).next()

        CheckOut(self.driver).safepay()
        CheckOut(self.driver).safepay_username('Ss11-')
        CheckOut(self.driver).safepay_password('Ss11')
        CheckOut(self.driver).pay_now_safepay()

     # Checking if the order made was successfully.
        header_payment = self.driver.find_element_by_css_selector("[translate='ORDER_PAYMENT']").text
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'orderNumberLabel')))
        ordernum = self.driver.find_element_by_id("orderNumberLabel").text
        subtotal = self.driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[2].text
        self.assertEqual(header_payment, 'ORDER PAYMENT')

        Main_Page(self.driver).click_cart()
        header_cart = self.driver.find_element_by_css_selector(
            '[class="bigEmptyCart center"]>[translate="Your_shopping_cart_is_empty"]').text
        self.assertEqual(header_cart, 'Your shopping cart is empty')

        # Compering the information from the order page - right after payment, to the order in 'my orders' page.
        My_Orders(self.driver).go_to_my_orders()
        detailslist = My_Orders(self.driver).order_details(1)
        self.assertEqual(detailslist[0], ordernum)
        self.assertEqual(detailslist[2], subtotal)

        productA = My_Orders(self.driver).order_product_details(1, 0)
        productB = My_Orders(self.driver).order_product_details(1, 1)
        self.assertEqual(productA[0], product1[0])
        self.assertEqual(productA[1], product1[2])
        self.assertEqual(productA[2], product1[1])
        self.assertEqual(productB[0], product2[0])
        self.assertEqual(productB[1], product2[2])
        self.assertEqual(productB[2], product2[1])

    def test_9(self):

        # Adding products to the cart and keeping it's details in lists.
        Main_Page(self.driver).click_speakers()
        Category_Page(self.driver).focus_on_a_product(2).click()
        product1 = [Product_Page(self.driver).product_name(), Product_Page(self.driver).product_quantity(),Product_Page(self.driver).product_color()]
        Product_Page(self.driver).add_to_cart()
        Main_Page(self.driver).click_main_page()

        Main_Page(self.driver).click_mice()
        Category_Page(self.driver).focus_on_a_product(4).click()
        product2 = [Product_Page(self.driver).product_name(), Product_Page(self.driver).product_quantity(),Product_Page(self.driver).product_color()]
        Product_Page(self.driver).add_to_cart()
        Main_Page(self.driver).click_cart()

        # Checking out and filling the user information in the payment class.
        Cart_Page(self.driver).check_out()
        CheckOut(self.driver).insert_username_in_payment('aaAA11')
        CheckOut(self.driver).insert_password_in_payment('aaAA11')
        CheckOut(self.driver).log_in()
        Actions.checkout_details(self.driver, '1234567891234567', '123', '01', '2022', 'nitzan')

        # Checking if the order made was successfully.
        header_payment = self.driver.find_element_by_css_selector("[translate='ORDER_PAYMENT']").text
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'orderNumberLabel')))
        ordernum = self.driver.find_element_by_id("orderNumberLabel").text
        subtotal = self.driver.find_elements_by_css_selector('[class="innerSeccion"]>label>a')[2].text
        self.assertEqual(header_payment, 'ORDER PAYMENT')

        Main_Page(self.driver).click_cart()
        header_cart = self.driver.find_element_by_css_selector(
            '[class="bigEmptyCart center"]>[translate="Your_shopping_cart_is_empty"]').text
        self.assertEqual(header_cart, 'Your shopping cart is empty')

        # Compering the information from the order page - right after payment, to the order in 'my orders' page.
        My_Orders(self.driver).go_to_my_orders()
        detailslist = My_Orders(self.driver).order_details(-2)
        self.assertEqual(detailslist[0], ordernum)
        self.assertEqual(detailslist[2], subtotal)

        productA = My_Orders(self.driver).order_product_details(1, 0)
        productB = My_Orders(self.driver).order_product_details(1, 1)
        self.assertEqual(productA[0], product1[0])
        self.assertEqual(productA[1], product1[2])
        self.assertEqual(productA[2], product1[1])
        self.assertEqual(productB[0], product2[0])
        self.assertEqual(productB[1], product2[2])
        self.assertEqual(productB[2], product2[1])

    def test_10(self):
        Main_Page(self.driver).create_user_new_user_pop_up()
        User_Pop_Up(self.driver).insert_user_name()
        User_Pop_Up(self.driver).insert_user_password()
        User_Pop_Up(self.driver).sign_in()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[style="top: 5%;"]')))
        login_ = self.driver.find_elements_by_css_selector('[data-ng-show="userCookie.response"]')
        self.assertEqual(login_[1].get_attribute("class"), "hi-user containMiniTitle ng-binding")
        Main_Page(self.driver).create_user_new_user_pop_up()
        User_Pop_Up(self.driver).sign_out()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, 'loginMiniTitle')))
        self.assertEqual(login_[1].get_attribute("class"), 'hi-user containMiniTitle ng-binding ng-hide')
