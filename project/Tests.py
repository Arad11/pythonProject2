from project.Actions import Actions
import time

driver = Actions.open_web()
Actions.add_3_products(driver, "mice")
time.sleep(2)
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()

products_quantity =[]
products_price = []

table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
rows = table.find_elements_by_tag_name("tr")
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for i in range(len(cells)):
        if i == 4 and i != len(cells) -1:
            products_quantity.append(cells[i].text)
        if i == 5:
            products_price.append(cells[i].find_element_by_tag_name("p").text)

print(products_price)
print(products_quantity)