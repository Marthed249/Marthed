import re
class Multplae:
    syntax_name= r"[A-Z][a-z]{2,}"
    Employes_num= 0
    @classmethod
    def NUM_OF_USER(cls):
       print(f"THE NUMBER OF USER Is =>{cls.Employes_num}<= IN THE SYSTEM")
    
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        Multplae.Employes_num+=1
    
    
    def Who_are_you(self): 
        if not(re.match(self.syntax_name,self.name)):
           raise NameError("Name Not Allowed")
        else:
         if self.gender=="Male":

          return f"The Name Of Emplaye Ms {self.name} Your Age Is {self.age}"
         elif self.gender=="Female":
          return f"The Name Of Emplaye Mis {self.name} Your Age Is {self.age}"
         else:
            return f"The Name Of Emplaye {self.name} YOur Age Is {self.age}"
    
    def Delete_user(self):
       Multplae.Employes_num-=1
       return f"The Number is User is :{Multplae.Employes_num}"
     
one_mutpeal=Multplae(input("What is Your name of Employee : "),int(input("What is Your age: ")),input("What is Your gender: "))
print(one_mutpeal.Who_are_you())
   
two_mutpeal=Multplae(input("What is Your name of Employee: "),int(input("What is Your age: ")),input("What is Your gender: "))
print(two_mutpeal.Who_are_you())
print(Multplae.Employes_num)
print(two_mutpeal.Delete_user())

Multplae.NUM_OF_USER()
