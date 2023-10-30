class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(self.name)
        print(self.id)
class emp(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        person.name=name
        person.id=id
    def details(self):
        print("name",self.name)
        print("id",self.id)
        print("Post",self.post)

a=emp("Rahul",10,10000,"Developer")
a.display()
a.details()
