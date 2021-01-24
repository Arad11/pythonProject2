class General:
    def __init__(self, driver):
        self.driver = driver

    def get_products_info_popup(self):
        table = self.driver.find_element_by_css_selector('table[ng-show="cart.productsInCart.length > 0"]')
        rows = table.find_elements_by_tag_name("tr")

        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == 1 and i != len(cells) - 1:
                    names = cells[i].find_element_by_css_selector("h3[class='ng-binding']").text
                    quantity = cells[i].find_element_by_tag_name("label").text
                    color = cells[i].find_element_by_css_selector("span[class='ng-binding']").text
                if i == 2:
                    price = cells[i].find_element_by_tag_name("p").text

        return {"names": names, "quantity": quantity, "color": color, "price": price}

    def change_quantity(self, quantity):
        self.driver.find_element_by_name("quantity").click()
        self.driver.find_element_by_name("quantity").send_keys(quantity)

    def my_orders(self):
        return self.driver.find_element_by_css_selector('[id = "menuUserLink"] > div > [translate = "My_Orders"]').click()