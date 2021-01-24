from project.Actions import Actions
import time


driver = Actions.open_web()
Actions.add_3_products(driver, "mice")
time.sleep(2)
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()

# gets values from the table at the cart page
table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
rows = table.find_elements_by_tag_name("tr")
products_quantity =[]
products_price = []
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for i in range(len(cells)):
        if i == 4 and i != len(cells) -1:
            products_quantity.append(cells[i].text)
        if i == 5:
            products_price.append(cells[i].find_element_by_tag_name("p").text)

products_number = 0
count_price = 0
# total ordered units
for i in products_quantity:
    products_number += int(i)

# total price
for i in range(len(products_price)):
     count_price += float(products_price[i].replace("$", ""))

# access to the price in the cart shopping
cart_price = driver.find_element_by_css_selector('[class="roboto-medium cart-total ng-binding"]').text.replace("$", "")
print(cart_price)
# access to the products count - pop-up
pop_up_count = driver.find_element_by_css_selector('[class="roboto-regular ng-binding"]').text.split()[0]
# print(pop_up_count)
# print(pop_up_count[-1])

# why can't convert string to float?
if float(cart_price) == count_price:
    print("True")
# elif cart_price - count_price < 0.1:
#     print("True")
else:
    print("False")

if int(pop_up_count[-1]) == int(products_number):
    print("True")
else:
    print("False ")