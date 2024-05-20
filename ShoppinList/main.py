from shoppinglist import ShoppingList,Product

#create a shopping list
l1 = ShoppingList("Groceries")
print(l1)
print(l1.show())


##create Some products

p1 = Product("tomato",2)
p2 = Product("onion",2)
p3 = Product("Milk",1)
p4 = Product("bread",10)

l1.add_item(p1)
l1.add_item(p2)
l1.add_item(p3)
l1.add_item(p4)

l1.add_item("Bambino")

l1.show()