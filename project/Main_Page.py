import time


class Main_Page:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")

    def click_speakers(self):
        return self.driver.find_element_by_id("speakersImg").click()

    def click_tablets(self):
        return self.driver.find_element_by_id("tabletsImg").click()

    def click_laptops(self):
        return self.driver.find_element_by_id("laptopsImg").click()

    def click_mice(self):
        return self.driver.find_element_by_id("miceImg").click()

    def click_headphones(self):
        return self.driver.find_element_by_id("headphonesImg").click()

    def click_cart(self):
        return self.driver.find_element_by_id("shoppingCartLink").click()

    def click_main_page(self):
        return self.driver.find_element_by_css_selector('[ng-click="go_up()"]').click()

    def create_user_new_user_pop_up(self):
        time.sleep(2)
        return self.driver.find_element_by_id('menuUserLink').click()
