from unittest import TestCase
from project.Actions import Actions
import time
from project.Main_Page import Main_Page
from project.Category_Page import Category_Page
from project.Product_Page import Product_Page
from project.User_POP_Up import User_Pop_Up



class All_Tests(TestCase):

    def setUp(self):
        print("setUp")
        self.driver = Actions.open_web()

    def tearDown(self):
        print("tearDown")

    def test_1(self):
        self.skipTest()
        Actions.add_3_products(self.driver, "mice")
        time.sleep(2)
        self.driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
        y = Actions.values_from_a_table(self.driver, "[class='fixedTableEdgeCompatibility']", 4)
        total_amount = 0
        for i in y:
            total_amount += int(i)
        self.assertEqual(total_amount, int(self.driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text))

    def test_2(self):
        self.skipTest()
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
        self.skipTest()

    def test_4(self):
        self.skipTest()

    def test_5(self):
        Actions.add_3_products(self.driver, "mice")
        time.sleep(2)
        self.driver.find_element_by_css_selector("[href='#/shoppingCart']").click()

        # #gets values from the table at the cart page
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
        cart_price = self.driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text.replace(
            "$", "")
        print(cart_price)
        # access to the products count - pop-up
        pop_up_count = self.driver.find_element_by_css_selector('[class="roboto-regular ng-binding"]').text.split()[0]

        # why can't convert string to float?
        if float(cart_price) == count_price:
            print("True")

        else:
            print("False")

        if int(pop_up_count[-1]) == int(products_number):
            print("True")
        else:
            print("False ")
        self.assertEqual(float(cart_price), count_price)
        self.assertEqual(int(pop_up_count[-1]), int(products_number))

    def test_6(self):
        self.skipTest()

    def test_7(self):
        self.skipTest()
        Main_Page(self.driver).click_tablets()
        Category_Page(self.driver).focus_on_a_product(1).click()
        Product_Page(self.driver).add_to_cart()
        Product_Page(self.driver).back_to_category_page()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/category/Tablet/3")
        Category_Page(self.driver).focus_main_page()
        self.assertEqual(self.driver.current_url, "https://www.advantageonlineshopping.com/#/")


    def test_8(self):
        self.skipTest()

    def test_9(self):
        self.skipTest()

    def test_10(self):
        self.skipTest()
        Main_Page(self.driver).creat_user_new_user_pop_up()
        User_Pop_Up(self.driver).inser_user_name()
        User_Pop_Up(self.driver).insert_user_password()
        User_Pop_Up(self.driver).sign_in()
        time.sleep(1)
        login_ = self.driver.find_elements_by_css_selector('[data-ng-show="userCookie.response"]')
        self.assertEqual(login_[1].get_attribute("class"), 'hi-user containMiniTitle ng-binding')
        # if login_[1].get_attribute("class") == 'hi-user containMiniTitle ng-binding':
        #     print("True")
        # else:
        #     print("False")
        Main_Page(self.driver).creat_user_new_user_pop_up()
        User_Pop_Up(self.driver).sign_out()
        time.sleep(1)
        self.assertEqual(login_[1].get_attribute("class"), 'hi-user containMiniTitle ng-binding ng-hide')
        # if login_[1].get_attribute("class") == 'hi-user containMiniTitle ng-binding ng-hide':
        #     print("True")
        # else:
        #     print("False")