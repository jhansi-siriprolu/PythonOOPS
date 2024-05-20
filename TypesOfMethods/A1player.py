class Player:
    MAX_HEARTS = 3
    def __init__(self,name):
        self.name = name
        self.hearts = Player.MAX_HEARTS
    def __str__(self):
        return f"{self.__class__.__name__} name: {self.name} hearts:{self.hearts}"
    @classmethod
    def modify_hearts(cls,new_val):
        cls.MAX_HEARTS = new_val
    
    def lose(self):
        if self.hearts == 1:
            print("Game over")
        else:
            self.hearts -= 1
            print(f"You lost, you still have {self.hearts}")

p = Player("John")
print(p)
print(Player.MAX_HEARTS)
p.lose()
p.lose()
p.lose()
p.lose()
Player.modify_hearts(1)
p2 = Player("Jane")
print(p2)
p2.lose()
p2.lose()