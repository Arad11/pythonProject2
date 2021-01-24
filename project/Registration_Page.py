class Registration_Page:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        return self.driver.find_element_by_name('usernameRegisterPage').send_keys(username)

    def enter_email(self, email):
        return self.driver.find_element_by_name('emailRegisterPage').send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element_by_name('passwordRegisterPage').send_keys(password)

    def confirm_password(self, password):
        return self.driver.find_element_by_name('confirm_passwordRegisterPage').send_keys(password)

    def enter_first_name(self, firstname):
        return self.driver.find_element_by_name('first_nameRegisterPage').send_keys(firstname)

    def enter_last_name(self, lastname):
        return self.driver.find_element_by_name('last_nameRegisterPage').send_keys(lastname)

    def enter_phone_number(self, phonenum):
        return self.driver.find_element_by_name('phone_numberRegisterPage').send_keys(phonenum)

    def enter_country(self, country):
        self.driver.find_element_by_name('countryListboxRegisterPage').click()
        return self.driver.find_element_by_css_selector(f'[label={country}').click()

    def enter_city(self, city):
        return self.driver.find_element_by_name('cityRegisterPage').send_keys(city)

    def enter_address(self, address):
        return self.driver.find_element_by_name('addressRegisterPage').send_keys(address)

    def enter_state(self, state):
        return self.driver.find_element_by_name('state_/_province_/_regionRegisterPage').send_keys(state)

    def enter_postal_code(self, postalcode):
        return self.driver.find_element_by_name('postal_codeRegisterPage').send_keys(postalcode)

    def agreement(self):
        return self.driver.find_element_by_name('i_agree').click()

    def register(self):
        return self.driver.find_element_by_id('register_btnundefined').click()
