import time
class My_Orders:
    def __init__(self, driver):
        self.driver = driver

    def go_to_my_orders(self):
        """This action takes you to the user's orders list."""
        self.driver.find_element_by_id('menuUserLink').click()
        return self.driver.find_element_by_css_selector('[id = "menuUserLink"] > div > [translate = "My_Orders"]').click()

    def order_details(self, ordernum):
        # order = self.driver.find_elements_by_class_name('products ng-scope')[ordernum]
        # details = self.driver.find_elements_by_class_name("orderDetails")[ordernum]
        time.sleep(2)
        order_num = self.driver.find_elements_by_css_selector('[class="left ng-binding"]')
        order_date = self.driver.find_elements_by_css_selector('[class="center ng-binding"]')[ordernum].text
        total_price = self.driver.find_elements_by_css_selector('[class="right ng-binding"]')[ordernum].text

        return (order_num[ordernum], type(order_num[ordernum]), len(order_num))
        # return {'order_num': order_num, 'order_date': order_date, 'total_price': total_price}

    def order_product_details(self, ordernum, product_num):
        order = self.driver.find_elements_by_css_selector('[class="tabletsSection"]>[class="products ng-scope"]')[ordernum]
        products = order.find_elements_by_tag_name("div")[1]
        product = products.find_elements_by_tag_name("div")[product_num]
        name = product.find_elements_by_css_selector('div>span')[product_num].text
        quantity = product.find_elements_by_tag_name('label')[0].text
        color = product.find_elements_by_css_selector('div>label>span')[product_num].text
        return {'name': name, 'quantity': quantity, 'color': color}

