class ShoppingList:
    def __init__(self,items):
        self.items = items
    def __str__(self):
        return f"{self.__class__.__name__} ITEMS: {self.items}"
    @classmethod
    def from_string(cls,items):
        if isinstance(items,str):
            items_list = items.split(',')
            return cls(items_list)
s1 = ShoppingList(["Apples","Bananas"])
print(s1)
s2 = ShoppingList.from_string("Mangoes,oranges,pine-apples")
print(s2)