import csv
from abc import ABC,abstractmethod ## abc stands for abstract based class

#!Creation of class
class Item(ABC):
    #pass // we use pass if we want to write nothing in the class:
   
    #*like in javascript we have a class attribute that comes before the constructor
    pay_rate=0.8
    all=[]
   ##Constructor
   #*this is how we create a constructor for a class in python
   #*the self parameter simply say that python passes the object itself as a first parameter when you call that method
   #*and we should use self parameter when in the class
   #*the fact that we have self as a parameter here could actually allow us to assign the attribute from the init method
   #*so we'll not not have to assing attributes for each object
    def __init__(self,name:str,price:float,quantity=0): ## we can also initialise a paramater to its default value
                                                        ##when not provided during instanciation like in javascript 
                                                        ##as well as specify the type of parameter like in typescript
        
        #*assert statement is useful when we want to check the validity of parameters and catch errors
        #*before going forward                                               
        assert price >=0, f"Price {price} is not a valid value!"                                            
        assert quantity >= 0, f"Price {quantity} is not a valid value!"
        #!to make an attribute private we put "__" after self. while in javascripte we say: #attribute
        self.__name = name## similar to this.__name=name in javascript
        self.__price = price
        self.__quantity = quantity
        #*create a list of objects
        Item.all.append(self)
    
    
    
    #! Property decorator = read-only attribute : like Getter in javascript
    #*the attribute name is a private attribute, meaning that it can't be accessed from outside the class no matter what
    #*if we want to acces in read-only mode we use @property
    #*this is how we set an attribute to a read-only value
    #*when calling the property name we don't put parenthesis 
    @property
    def getName(self): 
        print("Getting name...")
        return self.__name
    
    @property
    def getPrice(self): 
        print("Getting price...")
        return self.__price
    
    @property
    def getQuantity(self): 
        print("Getting quantity...")
        return self.__quantity
    
    #*if we still want anyway to change a property attribute we use the decorator setter like this:
    @getName.setter #! like setter in javascript
    def setName(self, value):
        #*we can write any code here as well as in the property decorator
        if len(value)>10:
            raise Exception("The name is too long")
        print("Setting name...")
        self.__name = value
    
    @getPrice.setter
    def setPrice(self, value):
        print("setting price...")
        self.__price = value
    
    @getQuantity.setter
    def setQuantity(self, value):
        print("setting quantity...")
        self.__quantity = value 
        
        
    #*the __repr__ method is used to configure the representation of objects in a way we want
    #*it is called implicity when we want to print an object or a list of objects
    #*it's also called a dunder or magic method, and allows us to being able to create our own methods
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.__quantity})"
    
    #*read data from csv file and create insta'nces of Item from csv file
    #*cls is as self but it's the class itself rather than the object that is going to be passed as a parameter
    #*we should have cls for a classmethod
    ##here is how we specify that this method will be a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as fhand:
            # read the csv file and convert it into a dictionnarie
            reader = csv.DictReader(fhand)
            items = list(reader)  # convert the dictionnarie to a list

        for item in items:
            #*instanciation
            Item(
                name=item.get("name"),
                # because items is a list of strings we need to convert price and quantity to a number
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )
    
    #! a static method doesn't need to pass an object or a class as a first parameter
    #! here number is just a simple parameter
    #!both the class and instances can access to a static method unlike in javascript
    #! where a class only can be
   #*verify if a number is an integer or not
    @staticmethod
    def integerOrNot(number):
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
  
  
    #*methods are functions created inside of a class

    #@abstractmethod
    def calculate_total_price(self):
        return self.__price*self.__quantity



    def apply_discount(self):
        #*if we want to apply a dicount for all instances:
        ##Even though pay_rate is declared inside of the class, because it's  class attribute we need to specify the class
        #?object.price=object.price*Item.pay_rate
        #*if want to apply discount for a specific instance:
        self.__price = self.__price*self.pay_rate
        
  
#! Inheritance of classes
#*we put the name of the parent class in parentheses
#*instead of using the "extends" keyword like in javascript    
class Phone(Item):
    listphone=[]

    
    def __init__(self, name:str, price:float, quantity=0,broken_phones=0):
        ##it's very like in javascript or java, for the child class we use the super().__init__() function in python
        ##then the child class inherits all the data and methods from his parent class
        super().__init__(name,price,quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not a valid value!"
        self.broken_phones=broken_phones
        Phone.listphone.append(self)
        

#! Multiple inheritance of classes
#*so we have 2 classes: Item and Phone.
#* Let's say we want to create a class that inherit these 2 classes, like class touchscreen for all touchscreen phones:
#*In order to do that each class must not inherit eachother together
#*But here because Phone is a subclass of Item, we cannot create the touchscreen class from these 2 classes
#*It's like we inherit 2 times the same class, which makes nonsens
#*Let's create an independent class

class Priceless:
    def pricy(self):
        print("this item is priceless")
#*Now we can create our touchscreen class that will inherit Item and Priceless classes
class Touchscreen(Phone,Priceless):
    listpriceless=[]
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)
        Touchscreen.listpriceless.append(self)       
   
def make_class(x):
    class Dog:
        def __init__(self, name):
          self.name = name
        
        def print_value(self):
            print(x)
    
    return Dog

cls=make_class(10)
d=cls("Tim")
print(d.name)
d.print_value()

#!create an instance of class or an object
item1 = Item("phone",100,5)
print(item1.getName)
#!assigning attributes to an object
#*in python we can add attribute to an object even after the object was created
#*but not a best practice as we could use the constructor to do that
#?item1.name = "phone"
#?item1.price = 100
#?item1.quantity = 5

print(item1.calculate_total_price())##so python passes item1 as a first parameter everytime you call calculate_total_price

item2 = Item("laptop",1000,3)

print(item2.getName)
print(item2.calculate_total_price())
print(Item.pay_rate)
#*objects from class Item can access to the class attributes, unlike in javascript when declaring in static mode
print(item1.pay_rate)
print(item2.pay_rate)
item1.apply_discount()
print(item1.getPrice)
item2.pay_rate =0.7
item2.apply_discount()
print(item2.getPrice)



##as we defined __repr__ we can print our list of object or even a simple object:
#print(Item.all)
#print(item1)
#Item.instantiate_from_csv()
#print(Item.all)

print(item1.integerOrNot(19))
#print(Item.integerOrNot(19))

phone1=Phone("samsungS20",500,5)
print(phone1.calculate_total_price())
phone2=Phone("samsungNote10",700,5)
print(Phone.listphone)
print("\n")
print(Item.all)
print("\n")

print(phone1.getName)
print("\n")
phone1.setName ="TabS7Pro"
print("\n")
print(phone1.getName)
print(Item.all)
Priceless1=Touchscreen("Iphone12",2500,40)
print(Priceless1.pricy())
print(Priceless1.getName)

#! Encapsulation refers to a mechanism of restricting the direct access to some of attributes in a program
#! for example restricting the ability to overwrite the value of name within our setters is exactly what encapsulation is

## Abstraction is the concepts of OOP that only shows the necessary attributes or methods and hide the unnecessary information in the instance level or even in the class level
## By making attributes and methods that are not necessary for the user private is what the abstraction is
##For exemple if i were to send items to someone by email with a send_email method, in my class Item making private all the methods/attributes(by adding __ before them for attributes) related to send_email method and that are not necessary 
##for the user so that send_email method can only be accessed from the instance is what we call abstraction
#*we can also abstract a class so that user can't create any instance from that abstracted class
#*To do that we need to import ABC, and abstractmethod from abc. An abstract class is a class that contains one or more abstract methods
#*Let's say that we want to abstract the calculate_total_price() method, Item must inherit from ABC and we just put the @abstractmethod decorator to that

#*Polymorphism is a very important concept in programming, it refers to use a single type of entity to represent different types 
#*in differents scenarios. It is the ability to have different scenarios when we call the exact same entity(an entity could be a function)
#*For example the len() built function knows how to handle different kinds of objects that it receives as an argument 
#*and returns a result accordingly:

#*name="Jim",print(len(name)) will return the number of letters of the name (3)
#*whereas : some_list=["some","name"],print(len(some_list)) will return the number of objects in the list
