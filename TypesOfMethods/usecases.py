from datetime import datetime
class Developer:
    LIMIT = 3
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.skills = []
    def __str__(self):
        return f"{self.__class__.__name__} ,name: {self.name}, age: {self.age}"
    def add_skill(self, new_skill):
        if len(self.skills) < self.__class__.LIMIT:
            self.skills.append(new_skill)
            print(f"New skill {new_skill} is added")
        else:
            print(f"Number of skills exceeded {self.__class__.LIMIT}")

    @classmethod
    def change_limit(cls,new_limit):
        cls.LIMIT = new_limit

    @classmethod
    def birthyear2age(cls,name,birthyear):
        present_year = Developer.present_year_extraction()
        return cls(name,present_year - birthyear)
    

    
    @staticmethod
    #this does not require nor self nor cls
    def present_year_extraction():
        current_year = datetime.today().year
        return current_year
d = Developer("Jhansi",18)
d.add_skill("Python")
d.add_skill("Apache Spark")
d.add_skill("Hadoop")
d.change_limit(5)
d.add_skill("ML")
d.add_skill("AI")
print(d)
d2 = Developer.birthyear2age("Vimudha",1990)
print(d2)