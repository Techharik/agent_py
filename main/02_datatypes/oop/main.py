class chaiOrder:
    def __init__(self):
        pass

    def action(self):
        return

class masalaChai(chaiOrder):
    def __init__(self):
      pass

class another(masalaChai , chaiOrder):  # first parent is masalaChai and second parent is chaiOrder
    def __init__(self):
        super().__init__()    # get all the methods from the parent;

# another.__mro__ returns the prototype inhertated parent class in orders. 

#static - methods - access come with class ot with object; single instance like a private method for the class;

class utlis:
    @staticmethod
    def clean(text):
        return 'Hai'

text = utlis.clean("hello") # here object is not initalized only class 

# classmethod vs static method
#  class method has access to class instance itself help to create more contructor inisde


class more:
    def __init__(self, size , max):
        self.size = size
        self.max = max
    
    @classmethod            # the contructor is taken and created a another method on top it , object instance
    def fromString(cls , order):
        size , max = order.split("-")
        return cls(size , max)
    
    @staticmethod          #the static method class is  taken we can access it via class , class instance
    def private_method(size):
        return size
    
# property decorator:
# helps to update the property getter and setter

class deco:
    def __init__(self , age):
        self._age = age
    
    @property
    def age(self):
        return self._age + 2   #getter for thr property
    
    @age.setter                      #setter
    def age(self, age):
         self._age = age
         return None
  

obj = deco(1)
print(obj.age)
obj.age = 2
print(obj.age)

# getter setter which obj instace change the property inside the class helpfull for validation input into the objects.
