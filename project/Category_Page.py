from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Category_Page:
    def __init__(self, driver):
        self.driver = driver

    def focus_on_a_product(self, i):
        return self.driver.find_elements_by_css_selector('[class="cell categoryRight"]>ul>li')[i]

    def focus_main_page(self):
        return self.driver.find_element_by_css_selector('[ng-click="go_up()"]').click()
