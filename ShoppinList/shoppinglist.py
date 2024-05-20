# start with smallest class
class Product:
    def __init__(self,title,quantity):
        self.product_name = title
        self.quantity = quantity
    def __str__(self):
        return f'The Product {self.product_name} has {self.quantity} number'
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

class ShoppingList:
    def __init__(self, list_name, items= []):
        self.name = list_name
        self.items = items
    def __str__(self):
        return f'The ShoppingList {self.name} has {len(self.items)} items'
    def add_item(self, item):
        if isinstance(item,Product):
            self.items.append(item)
            print("The new item is sucessfully added")
        else:
            print("This item is not product")
    def show(self):
        print(f"The shoppin lit has {len(self.items)}")
        for item in self.items:
            print(item)
            print(item.quantity,item.product_name)