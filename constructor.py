class car:
    category = "SUV"
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname, self.year)
c1 = car("Nexon",2024)
print(c1.category)
c1.display()
print(c1.__module__)
print(c1.__dict__)


