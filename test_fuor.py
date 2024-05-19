class Marthed:
    def __init__(self,name,age):
        self.__name=name
        self.__age= int(age)
    def check_point(self):
         if self.__age > 18:
           return f"Hello Ms {self.__name} Welcom The Club"
         else:
           return f"Sorry Ms {self.__name} You can\'t joined The Club "

    def get_name(self):
       return self.__name
    def set_name(self,new_name):
       self.__name= new_name
       return self.__name


Marthed_one=Marthed(input("Please Enter You Name:"),input("Enter Your Age: "))
print(Marthed_one.check_point())
#print(Marthed_one._Marthed__name)
#print(Marthed_one.check_point())
print(Marthed_one.get_name())
print(Marthed_one.set_name(input("Enter New Name:")))
print(Marthed_one.check_point())
