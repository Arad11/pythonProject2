class User_Pop_Up:
    def __init__(self, driver):
        self.driver = driver

    def inser_user_name(self):
        return self.driver.find_element_by_name("username").send_keys("aaAA11")

    def insert_user_password(self):
        return self.driver.find_element_by_name("password").send_keys("aaAA11")

    def sign_in(self):
        return self.driver.find_element_by_id("sign_in_btnundefined").click()

    def sign_out(self):
        return self.driver.find_element_by_css_selector('[ng-click="signOut($event)"]').click()

    def next(self):
        return self.driver.find_element_by_id('next_btn').click()

    def safepay(self):
        return self.driver.find_element_by_name("safepay").click()

    def safepay_username(self, username):
        return self.driver.find_element_by_name('safepay_username').send_keys(username)

    def safepay_password(self, password):
        return self.driver.find_element_by_name('safepay_password').send_keys(password)

    def pay_now(self):
        return self.driver.find_element_by_id('pay_now_btn_SAFEPAY').click()






    ########## nitzan
    """
    def insert_user_name(self, username):
        return self.driver.find_element_by_name("username").send_keys(username)

    def insert_user_password(self, password):
        return self.driver.find_element_by_name("password").send_keys(password)

    def sign_in(self):
        return self.driver.find_element_by_id("sign_in_btnundefined").click()

    def sign_out(self):
        return self.driver.find_element_by_css_selector('[ng-click="signOut($event)"]').click()
    """