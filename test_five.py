from abc import ABCMeta , abstractmethod
class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

class python:
    
    def has_oop(self):
        return "Yes"
    
class C:
    def has_oop(self):
        return "Yes"

class pascal:
    def has_oop(self):
        return "No"
one=python()
print(one.has_oop())
two=C()
print(two.has_oop())
three=pascal()
print(three.has_oop())



