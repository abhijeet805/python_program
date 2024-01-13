class Emp:
    def accept(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal
    def display(self):
        print("Emp no=",self.eno)
        print("Emp name=",self.name)
        print("Emp salary=",self.sal)

ob=Emp()
ob.accept(101,"om",50000)
d={"eno":ob.eno,"name":ob.name,"salary":ob.sal}        
print(d)
