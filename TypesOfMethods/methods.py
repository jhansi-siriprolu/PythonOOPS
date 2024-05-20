class SampleClass:
    x = 0
    def __init__(self, y):
        self.y = y
    
    def change_object(self,new_x,new_y):
        self.y = new_y
        
        print("Class Attribute:", self.__class__.x)
        self.__class__.x = new_x
        print("Class Attribute after change object:", self.__class__.x)

    @classmethod
    def class_object_change(cls, new_val):
        cls.x = new_val

    @staticmethod
    def auxiliary_method():
        print("This is a static method")
        

obj = SampleClass(10)
obj.change_object(100,1000)
print(obj.y)

print("Class before attributes:", SampleClass.x)
SampleClass.class_object_change(300)
print("Class after attributes:", SampleClass.x)

obj.auxiliary_method()
SampleClass.auxiliary_method()

