class Cart_Page:
    """This class refers to the Cart page and it's actions."""

    def __init__(self, driver):
        self.driver = driver

    def remove_product_from_cart(self, i):
        return self.driver.find_elements_by_css_selector('[translate="REMOVE"]')[i].click()

    def edit_product_from_cart(self, i):
        return self.driver.find_elements_by_css_selector('[translate="EDIT"]')[i].click()

    def check_out(self):
        return self.driver.find_element_by_css_selector('[colspan="5"]>button').click()

    def cart_products_details(self):
        table = self.driver.find_element_by_css_selector('[class="fixedTableEdgeCompatibility"]>tbody')
        rows = table.find_elements_by_tag_name("tr")
        name = []
        color = []
        quantity = []
        price = []

        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == 1:
                    name.append(cells[i].text)
                if i == 3:
                    color.append(cells[i].find_element_by_tag_name('span').get_attribute('title'))
                if i == 4:
                    quantity.append(cells[i].text)
                if i == 5:
                    price.append(cells[i].find_element_by_tag_name('p').text)
        return name, color, quantity, price

    def click_body(self):
        self.driver.find_element_by_class_name('sp').click()
