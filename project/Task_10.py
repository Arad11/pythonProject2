import time
from project.Main_Page import Main_Page
from project.User_POP_Up import User_Pop_Up
from project.Actions import Actions

driver = Actions.open_web()
Main_Page(driver).creat_user_new_user_pop_up()
User_Pop_Up(driver).insert_user_name()
User_Pop_Up(driver).insert_user_password()
User_Pop_Up(driver).sign_in()
time.sleep(1)
login_ = driver.find_elements_by_css_selector('[data-ng-show="userCookie.response"]')
if login_[1].get_attribute("class") == 'hi-user containMiniTitle ng-binding':
    print("True")
else:
    print("False")
Main_Page(driver).creat_user_new_user_pop_up()
User_Pop_Up(driver).sign_out()
time.sleep(1)
if login_[1].get_attribute("class") == 'hi-user containMiniTitle ng-binding ng-hide':
    print("True")
else:
    print("False")