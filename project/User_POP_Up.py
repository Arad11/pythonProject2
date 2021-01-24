class User_Pop_Up:
    def __init__(self, driver):
        self.driver = driver

    def insert_user_name(self):
        return self.driver.find_element_by_name("username").send_keys("aaAA11")

    def insert_user_password(self):
        return self.driver.find_element_by_name("password").send_keys("aaAA11")

    def sign_in(self):
        return self.driver.find_element_by_id("sign_in_btnundefined").click()

    def sign_out(self):
        return self.driver.find_element_by_css_selector('[ng-click="signOut($event)"]').click()