import datetime
class car_Indstre:
    def __init__(self,name,module,color,price):
        self.name = name
        self.module = module
        self.color = color
        self.price = price
    def propertes(self):
        return f"The Name : {self.name}\nThe Module : {self.module}\nThe Color : {self.color}\nThe Price : {self.price}"
    def Indestre(self,EXP):
        self.EXP= EXP
        return f"The Car Indestre IN :{self.EXP}"

class Bradn(car_Indstre):
    def __init__(self,name,module,color,price,company):
        super().__init__(name,module,color,price)
        self.company=company
    def company_module(self,module_of_company):
        self.module_of_company=module_of_company
        return f"The Module of This is company is : {module_of_company}"
      
class Buy_car(Bradn):

   pass

Car_one=car_Indstre("FG4","Firreri","Selver",3000000)
print(Car_one.propertes())
Date_indster= datetime.datetime(2022,2,1)
print(Car_one.Indestre(Date_indster.strftime("%d %B %Y")))
print("="*40)
Car_two=Bradn("FES45","Marsedes","Red",500000,"DGS")
print(Car_two.propertes())
print(Car_two.company_module("Foswagend"))
Date_indestre_two=datetime.datetime(2023,5,1)
print(Car_two.Indestre(Date_indestre_two.strftime("%d %B %Y")))
print("="*40)
Car_three= Buy_car("rs","Marthed","Black",23000,"DEA")
print(Car_three.propertes())
print(Car_three.company_module("MSA"))

