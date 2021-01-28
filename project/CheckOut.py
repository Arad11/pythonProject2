class CheckOut:
    """This class refers to the CheckOut process."""

    def __init__(self, driver):
        self.driver = driver

    def registration_in_payment(self):
        return self.driver.find_element_by_id("registration_btnundefined").click()

    def insert_username_in_payment(self, username):
        return self.driver.find_element_by_name("usernameInOrderPayment").send_keys(username)

    def insert_password_in_payment(self, password):
        return self.driver.find_element_by_name("passwordInOrderPayment").send_keys(password)

    def log_in(self):
        return self.driver.find_element_by_id('login_btnundefined').click()

    def next(self):
        return self.driver.find_element_by_id('next_btn').click()

    def safepay(self):
        return self.driver.find_element_by_name("safepay").click()

    def masterCredit(self):
        return self.driver.find_element_by_name('masterCredit').click()

    def safepay_username(self, username):
        return self.driver.find_element_by_name('safepay_username').send_keys(username)

    def safepay_password(self, password):
        return self.driver.find_element_by_name('safepay_password').send_keys(password)

    def pay_now_safepay(self):
        return self.driver.find_element_by_id('pay_now_btn_SAFEPAY').click()

    def edit_details(self):
        return self.driver.find_element_by_css_selector('[translate="Edit"').click()

    def enter_card_num(self, cardnum):
        self.driver.find_element_by_id("creditCard").clear()
        return self.driver.find_element_by_id("creditCard").send_keys(cardnum)

    def enter_cvv_number(self, cvvnum):
        self.driver.find_element_by_name('cvv_number').clear()
        return self.driver.find_element_by_name('cvv_number').send_keys(cvvnum)

    def enter_expiration_mm(self, month):
        self.driver.find_element_by_name('mmListbox').click()
        return self.driver.find_element_by_css_selector(f'[label="{month}"').click()

    def enter_expiration_yy(self, year):
        self.driver.find_element_by_name('yyyyListbox').click()
        return self.driver.find_element_by_css_selector(f'[label="{year}"').click()

    def enter_cardholder_name(self, name):
        self.driver.find_element_by_name('cardholder_name').clear()
        return self.driver.find_element_by_name('cardholder_name').send_keys(name)

    def pay_now_masterCredit(self):
        return self.driver.find_element_by_id('pay_now_btn_ManualPayment').click()
