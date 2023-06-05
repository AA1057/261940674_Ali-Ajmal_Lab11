###  Q1
class Shape:
    def __init__(self,sides):
        self.sides = sides
        
    def ComputeArea(self):
        pass

class Triangle(Shape):
    def __init__(self, sides,base,height):
        super().__init__(sides)
        self.base = base
        self.height = height

    def ComputeArea(self):
        super().ComputeArea()
        print("Area of Triangle: ",1/2*self.base*self.height)

class Circle(Shape):
    def __init__(self, sides,radius):
        super().__init__(sides)
        self.radius = radius

    def ComputeArea(self):
        super().ComputeArea()
        print("Area of Circle: ",3.14*self.radius*self.radius)

def main():
    triangle = Triangle(3,4,2.4)
    circle = Circle(0,3)
    triangle.ComputeArea()
    circle.ComputeArea()
main()

###  Q2
class Employee:
    def __init__(self,EmpName,EmpID,Salary):
        self.EmpName = EmpName
        self.EmpID = EmpID
        self.salary = Salary
    
    def SalaryStatus(self):
        pass

    def display(self):
        pass

class BuildingManager(Employee):
    def __init__(self, EmpName, EmpID, Salary):
        super().__init__(EmpName, EmpID, Salary)

    def SalaryStatus(self):
        super().SalaryStatus()
        return self.salary
    
    def display(self):
        super().display()
        print(self.EmpName, self.EmpID, self.salary)
    
class ProcurementManager(Employee):
    def __init__(self, EmpName, EmpID, Salary):
        super().__init__(EmpName, EmpID, Salary)

    def SalaryStatus(self):
        super().SalaryStatus()
        return self.salary
    
    def display(self):
        super().display()
        print(self.EmpName, self.EmpID, self.salary)
    
class LogisticsManager(Employee):
    def __init__(self, EmpName, EmpID, Salary):
        super().__init__(EmpName, EmpID, Salary)
    
    def SalaryStatus(self):
        super().SalaryStatus()
        return self.salary
    
    def display(self):
        super().display()
        print(self.EmpName, self.EmpID, self.salary)

def main():
    Emplst = []
    Emplst.append(BuildingManager("Ali","695",10000))
    Emplst.append(ProcurementManager("Hamza","158",12000))
    Emplst.append(LogisticsManager("Bilal","196",15000))
    print(Emplst[0].display())
    print(Emplst[1].display())
    print(Emplst[2].display())
    print(Emplst[0].SalaryStatus())
    print(Emplst[1].SalaryStatus())
    print(Emplst[2].SalaryStatus())
main()