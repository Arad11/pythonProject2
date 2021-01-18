class Product_Page:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        return self.driver.find_element_by_name("save_to_cart").click()

    def focus_plus_one(self):
        return self.driver.find_element_by_css_selector('[class ="plus"]')
    def add_one(self):
        self.focus_plus_one().click()

    def focus_minus_one(self):
        return self.driver.find_element_by_css_selector('[class="minus disableBtn"]')
    def minus_one(self):
        return self.focus_minus_one().click()

    def click_main_page(self):
        return self.driver.find_element_by_css_selector('[ng-click="go_up()"]').click()

    def focus_cart_page(self):
        return self.driver.find_element_by_id("shoppingCartLink")
    def click_cart_page(self):
        return self.focus_cart_page().click()

    def product_name(self):
        return self.driver.find_element_by_css_selector('[class="roboto-regular screen768 ng-binding"]').text
    def product_quanity(self):
        return self.driver.find_element_by_css_selector('[name="quantity"]').get_attribute("value")
    def product_price(self):
        return self.driver.find_element_by_css_selector('[class="roboto-thin screen768 ng-binding"]').text
    def product_color(self):
        colors_list = self.driver.find_elements_by_css_selector('[id="rabbit"]')
        for i in colors_list:
            if "colorSelected" in i.get_attribute("class").split():
                return  i.get_attribute("class").split()[-1]

    def back_to_category_page(self):
        # try to find other selector
        self.driver.find_element_by_css_selector("body > div.uiview.ng-scope > nav > a:nth-child(2)").click()
