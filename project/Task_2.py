from project.Actions import Actions

driver = Actions.open_web()
names = []
quantity = []
price = []
colors = []
pop_up_products_names = []
pop_up_products_color = []
pop_up_products_quantity =[]
pop_up_products_price = []
total_price = []

Actions.add_3_products_and_save_details(driver, "mice", names, price, colors, quantity)
Actions.take_details_from_pop_up_cart(driver, pop_up_products_names, pop_up_products_color, pop_up_products_quantity, pop_up_products_price)

# clean the quantity list to only number
for i in range(len(pop_up_products_quantity)):
    pop_up_products_quantity[i].split()
    pop_up_products_quantity[i] = pop_up_products_quantity[i].split()[1]

# clean the price lists from $
for i in range(len(price)):
    price[i] = price[i].replace("$", "")
for i in range(len(pop_up_products_price)):
    pop_up_products_price[i] = float(pop_up_products_price[i].replace("$", ""))

# count the total price of each product we ordered (price per unit * units)
for i in range(len(price)):
    total_price.append(float(price[i])*float(quantity[i]))

# while information are go into the cart it goes upside down so we do the same for the lists.
# important to keep transitivation - all the pop-up lists are gonna be upside down or the other lists
if pop_up_products_names == names[::-1]:
    print("True")
else:
    print("False")

if pop_up_products_quantity == quantity[::-1]:
    print("True")
else:
    print("False")

if total_price[::-1] == pop_up_products_price:
    print("True")
else:
    print("False")

if colors[::-1] == pop_up_products_color:
    print("True")
else:
    print("False")