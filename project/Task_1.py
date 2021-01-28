from project.Actions import Actions
import time

driver = Actions.open_web()
Actions.add_3_products(driver, "mice")
time.sleep(2)
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
y = Actions.values_from_a_table(driver, "[class='fixedTableEdgeCompatibility']", 4)
total_amount = 0
for i in y:
    total_amount += int(i)
if total_amount == int(driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text):
    print("True")
else:
    print("False")