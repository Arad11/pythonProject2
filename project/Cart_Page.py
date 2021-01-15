class Cart_Page:
    def __init__(self, driver):
        self.driver = driver

    def remove_product_from_cart(self, i):
        return self.driver.find_elements_by_css_selector('[translate="REMOVE"]')[i].click()

    def edit_product_from_cart(self, i):
        return self.driver.find_elements_by_css_selector('[translate="EDIT"]')[i].click()