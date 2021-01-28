class My_Orders:
    """This class refers to the My Orders page and the information in it."""

    def __init__(self, driver):
        self.driver = driver

    def go_to_my_orders(self):
        """This action takes you to the user's orders list."""
        self.driver.find_element_by_id('menuUserLink').click()
        return self.driver.find_element_by_css_selector('[id = "menuUserLink"] > div > [translate = "My_Orders"]').click()

    def order_details(self, ordernum):
        """This action returns a list of the order's details - order number, order date and subtotal."""
        table = self.driver.find_element_by_css_selector('#myAccountContainer > div > table')
        row = table.find_elements_by_tag_name("tr")[ordernum]
        answer = []
        cells = row.find_elements_by_tag_name("td")
        for i in range(len(cells)):
            if i == 0:
                answer.append(cells[i].text)

            if i == 1:
                answer.append(cells[i].text)

            if i == 6:
                answer.append(cells[i].find_element_by_tag_name('label').text)
        return answer

    def order_product_details(self, ordernum, product_num):
        """This action returns a list of the product's details in a specific order - product name, color, quantity."""
        if product_num == 0:
            table = self.driver.find_element_by_css_selector('#myAccountContainer > div > table')
            row = table.find_elements_by_tag_name("tr")[ordernum]
            answer = []
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == 3:
                    answer.append(cells[i].find_element_by_tag_name('span').text.upper())

                if i == 4:
                    answer.append(cells[i].find_element_by_tag_name('div').get_attribute('title').upper())

                if i == 5:
                    answer.append(cells[i].text)

        if product_num > 0:
            table = self.driver.find_element_by_css_selector('#myAccountContainer > div > table')
            row = table.find_elements_by_tag_name("tr")[ordernum+product_num]
            answer = []
            cells = row.find_elements_by_tag_name("td")
            for i in range(len(cells)):
                if i == 0:
                    answer.append(cells[i].text.upper())

                if i == 1:
                    answer.append(cells[i].find_element_by_tag_name('div').get_attribute('title').upper())

                if i == 2:
                    answer.append(cells[i].text)

        return answer

