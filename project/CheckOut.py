
class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    def insert_username_in_payment(self, username):
        return self.driver.find_element_by_name("usernameInOrderPayment").send_keys(username)

    def insert_password_in_payment(self, password):
        return self.driver.find_element_by_name("passwordInOrderPayment").send_keys(password)

    def log_in(self):
        return self.driver.find_element_by_name('login_btnundefined').click()

