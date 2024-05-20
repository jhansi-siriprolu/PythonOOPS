#Method resolution order -- accessing parent classes from left to right in definition

#the methods and attributes are searched in BFS- breadth first search in the parents and parents of parents classes

class A:
    def __init__(self):
        self.x = 100
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        self.y = 30
        self.x = 10
class D(C,B):
    pass


d1 = D()
print(d1.x)
print(d1.y)