# 1. what is oops?
# 2. what is class and objects with real world example?
# 3. how to define empty class
# 4. types of variables
# 5. types of methods
# 6. variables and methods in a single class
#    - objects create
#    - variables -- kaha access, kaha define, kaha delete, kaha modify  -- inside the class, outside the class
#    - 
# 7. class Product -- 100 objects --  function that returns 100 objects
# 8. what is destructor -- with example
# 9. what is constructor, example, 5 sentenses
# 10. Bank application
# 11. Employee Registration  - with abstraction class
# 	Employee Class, common list of emps, class employee method -- emp_registration()- add in list, 
# 	delete emp from list, modify emp, read emps, read emp, show details() , aisi ek method -- average_salary(), 
# 12. interface -- file open, close --- excel, text, pdf -- actually open
# 13. count number of objects of any class 
# 14. what is polymorphism?
# 15. operating overloading with example of book pages
# 16. method overloading? is it possible in Python? If Yes, tell the ways
# 17. method overriding example?
# 18. access specifiers with examples 
# 19. name mangling
# 20. inheritance? -- types, diamond problem, how diamond problem is fixed? -- sab types ek ek example
# 21. super() -- atleast 2 examples with different context
		
		



# pep8 rule
# docstring
# comments


# 1. what is oops?
# Answer - every object oriented programing language supports oops, there are 4 pillars of oops
# they are polymorphism, encapsulation, inheritance, abstraction.

# ----------------------------------------------------------------------------------------------
# 2. what is class and objects with real world example?

# Answer - Every thing in a python is a object, object is created using modal or plan or blueprint, which is nothing but a class.
# Object is real existence of a class, there can be number of ojects for indiviual class

class Student:
    def __init__(self, name, age, grade, marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks

    def __str__(self) -> str:
        return f"{self.__dict__}"
    
    def __repr__(self) -> str:
        return str(self)

s1 = Student('Pankaj', 14, 10, 76) #this is a object 1
s2 = Student('Onkar', 16, 12, 89) #this is object 2...in this way we can create n number of obejects

print(s1)
print(s2)



# --------------------------------------------------------------------------------------
#3. how to define empty class

class Vechicle:
    '''This class maintains details of vechicles, for time being this is empty'''



# ------------------------------------------------------------------------------------------------
#4. types of variables

# Answer - There are three types of variables in the class
# instance variable (object level variables)
# static variable (class level variables)
# local variable  (temporary variables)
# Here when memory varies from object to object i.e every instance variable refers to different memory
# here class has common memory for static variables


# -------------------------------------------------------------------------------------------------
# 5. types of methods

# Answer - There are three types of methods in the class
# instance method - The method which contains instance variable inside it, its first argument should be self.
# class method - The method which contains static variable or class variable inside it, its firs argument should be cls, followed by class method decorator
# static method - This method is like normal function which does not contains any self or cls..we can define static methods in two ways. one is using staticmethod decorator and another ways as we define normal function.

# -------------------------------------------------------------------------------------------------
# 6. variables and methods in a single class
# We can declare instance variable inside constructor, instance method using self and using reference variable outside the class
# We can declare static/class variable directly outside the class, using self and classname we can declare inside the instance method, using cls and classname we can declare inside the class method, using classname we can declare inside inside static method

# we can access instance variable inside constructor, instance method using self and outside the class using reference variables
# we can access static variable inside constructor, instance method using self and classname, Inside class method using cls and classname, inside static method using classname, we can use reference variable and class name to access static variable outside the class

# instance variable can be modified inside instance method using self and outside the class using reference variable
# static/class variable can be modified inside class method using cls and classname
# inside static method using classname

# Note - if we try to modify class variable using self or reference variable then it will considered as instance for that object

# instance variable can be deleted using del self and outside the class using del reference variable

# static variable can be deleted using classname and cls inside class method and outside the class using classname

class Vehicle:
    
    showroom = "Sonak Toyota"  #declaring static varible outside the class
    showroom_location = "Bavdhan"

    def __init__(self, vecname, veccolor, vecgeartype):
        self.vehiclename = vecname #declaring instance variable inside constructor
        self.vehiclelcolor = veccolor
        self.vehiclelgeartype = vecgeartype
        Vehicle.RTO = 'Pune' #declaring staic variable inside constructor/instahce method using class name

    def __str__(self):
        return f"{self.__dict__}"
        

    def display_details(self):
        # accessing instance variable inside instance method using self.
        # We can access class variable inside instance method using self and classname
        print(f'''
        Name of Vehicle - {self.vehiclename} 
        Vehicle Color - {self.vehiclelcolor}
        Vehicle Gear Type - {self.vehiclelgeartype}
        Showroom - {self.showroom}
        RTO - {Vehicle.RTO}
        ''')

    @classmethod
    def get_showroom_rto_details(cls):
        print(f"Name of the showroom - {cls.showroom}") #accessing class variable inside class method using cls 
        print(f"Name of rto - {Vehicle.RTO}") #accessing class varibale inside class method using class name

    
    @staticmethod
    def get_location():
        print(f"The location of showroom - {Vehicle.showroom_location}")
    
    def modify_details(self, vecname):
        self.vehiclename = vecname #modify instance variable inside instance method using self
        del self.vehiclelcolor #deleted instance variable inside instance method using del self

    @classmethod
    def modify_showroom_details(cls):
        cls.showroom = 'DSK Toyota' #modifying using cls
        Vehicle.showroom_location = 'Satara' #modifying usinf classname

v1 = Vehicle('innova crysta', 'white', 'manual')
v2 = Vehicle('urban cruiser', 'grey', 'automatic')

v1.fueltype = "petrol" #declaring instance variable for object v1 outside the class, this will not reflected for other objects
print(v1)
    
# ------------------------------------------------------------------------------------------------------------------------------------------
# 7. class Product -- 100 objects --  function that returns 100 objects

import random

PROUDCT_CATEGORY = ["household", "Personal accessories", "detergent", "Electronics"]

PRODUCT_SIZE = ["Small", "Medium", "Large"]

class Product:
    '''This is product class'''

    def __init__(self, id, name, price, size, category):
        self.productid = id
        self.productname = name
        self.productprice = price
        self.productsize = size
        self.productcategory = category

    def __str__(self):
        return f"{self.__dict__}"
    
    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def display_all_products(all_products):
        for product in all_products:
            print(product)


def product_name():
    name = ""
    for i in range(random.randint(5,7)):
        char = chr(64+random.randint(4, 7))
        name+=char
    return name

    
def generate_product(num):
    all_product = []
    for i in range(1, num+1):
        name = product_name()
        price = random.randint(100, 4200)
        size = random.choice(PRODUCT_SIZE)
        category = random.choice(PROUDCT_CATEGORY)
        prod = Product(id=i, name=name, price=price, size=size, category=category)
        all_product.append(prod)
    return all_product

all_product = generate_product(100)

Product.display_all_products(all_product)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# 9. what is constructor, example, 5 sentenses

# Answer - 1. constructor is a special or magic/dunder method which gets invoke automatically when object of class is created.
# 2. constructor is a defined with __init__ method
# 3. constructor is the first method which gets invoke, it is responsible to instance variables or database resources
# 4. python provides default constructor in back end, if programmer does not provide constructor.
# 5. there can be default constructor as well as argument constructor.but its first argument should be 'self'.

class Person:
    '''This is person class, give details related to person'''

    def __init__(self, name, age, gender, complexion, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.__dict__}"
        

    def get_person_details(self):
        print(f'''
        Name - {self.name}
        Age - {self.age}
        Gender - {self.gender}
        Complexion - {self.complexion}
        Height - {self.height}
        Weight - {self.weight}
        ''')

p1 = Person('Sayali', 23, 'female', 'fair', 5.3, 58)
p2 = Person('vinod', 36, 'male', 'brown', 5.8, 76)

p1.get_person_details()

print(p2)
print()
    
# 10. Bank application

from datetime import datetime
import random

class Bank:
    '''This is Bank Application'''

    BankName = "ICICI"
    BankBalance = 0
   

    def __init__(self, name, accnumber, acctype, accbalance = 5000):
        self.accountname = name
        self.accountnumber = accnumber
        self.accounttype = acctype
        self.accountbalance = accbalance
        Bank.BankBalance += accbalance
    
    @classmethod
    def get_bank_details(cls):
        print(f"The Bank name - {cls.BankName}")
    
    def get_account_details(self):
        print(f'''\n
        Account Name - {self.accountname}
        Account Number - {self.accountnumber}
        Account Type - {self.accounttype}
        Account Balance - {self.accountbalance}
        ''')

    def get_balance(self):
        print(f"\n {self.accountname} balance is {self.accountbalance} at {datetime.now()}")
        print(f"\n Bank Balance is {Bank.BankBalance} at {datetime.now()}")
    
    def withdraw(self, amt):
        if self.accountbalance > amt:
            if amt % 500 == 0:
                self.accountbalance-=amt
                Bank.BankBalance-=amt
                self.get_balance()
            else:
                print("\n Please provide value in multiple 500 denominte")
        else:
            print("\n Insufficient account balance to withdraw the amount..!!")
    

    def deposit(self, amt):
        self.accountbalance+=amt
        Bank.BankBalance+=amt
        self.get_balance()

    def loan(self, amt):
        if self.accountbalance >= 10000:
            if amt < self.accountbalance * 5:
                self.accountbalance+=amt
                Bank.BankBalance-=amt
                self.get_balance()
            else:
                print("\n Here loan is not satisfying your condition")
        else:
            print("\n Your not eligible for loan...!!")


b1 = Bank('Athrav', 414142, 'savings', 50000)
b2 = Bank('Sujit', 1233, 'savings', 50000 )
b1.get_account_details()
b1.get_balance()
b1.deposit(1000)
b1.withdraw(5000)
b1.loan(35000)

# 13. count number of objects of any class
class Check:
    '''This class counts the number of object of class'''
    count = 0

    def __init__(self):
        Check.count+=1
    
    @classmethod
    def get_totalcount(cls):
        print(f"\n total objects of Check class are {Check.count}")

    @classmethod
    def generate_objects(cls,number):
        for i in range(1, number+1):
            total = Check()
        Check.get_totalcount()

Check.generate_objects(5)
print()

# 14. what is polymorphism?

# Answer - Polymorphism is one of the oops pillar. polymorphism allows to object to perform same actions in different way. in simple terms polymorhism means many form i.e same method having different behavior
# polymorphism can be achieved using below
 # Duck Typing philosophy
 # overloading
 # overriding
# python supports operator overloading, method and constructor overloading is not possible in python as python will considered as lastly defined method 

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 15. operating overloading with example of book pages

# Answer - overloading means methods having same name, but different arguments 
# '+' operator is best example of operator overloading, here with integer we perform addition, but we use same '+' operator with string then it concatenate. so here it show same actions in different ways
# we have special methods eg __add__, __mul__, __div__ to acheive operator overloading

class Book:
    '''This is book class'''

    def __init__(self, name, price):
        self.bookname = name
        self.bookprice = price

    def __str__(self):
        return f"{self.__dict__}"
        

    def __add__(self, others):
        return self.bookprice + others.bookprice
    
b1 = Book('lifeinprison', 345.90)
b2 = Book('fire', 430.00)

print(f"The total prices of the books are {b1 + b2}")
print()

# ----------------------------------------------------------------------------------------------
# 16. method overloading? is it possible in Python? If Yes, tell the ways

# Answer - No, method overloading and constructor overloading is not possible in python, python will considered lastly defined method. here but we can manage to implement method overloading using default argument and variable lenght argument

class Method:
    '''This class is used to acheive method overloading'''

    @classmethod
    def addition(cls,a=None, b=None, c=None):
        if a and b and c:
            print(f"\n The addition of three numbers are {a+b+c}")
        elif a and b:
            print(f"\n The addition of two numbers is {a+b}")
        elif a:
            print("\n addition of single digit is not possible")
    
    @classmethod
    def summation(cls, *args):
        try:
            if args:
                print(f"\n The summations is {sum(args)}")
        except TypeError:
            print("\n Please provide only numberical values")

# calling same method with different arguments
Method.addition(10, 20, 30) 
Method.addition(100, 200)
Method.addition(30.30)
           
Method.summation(200, 400, 500, 600)
Method.summation(100.10, 200.20)
Method.summation('abc', 'xyz')
print()

# -------------------------------------------------------------------------------------------------

# 17. method overriding example?

# answer - method overriding is implement there own definations in its child class, method overriding can be acheived using inheritance concept
# we can do method as well as constructor overriding.

class Father:
    '''This is a Father class'''

    def __init__(self, name, complexion, age):
        self.fathername = name
        self.fathercomplexion = complexion
        self.fatherage = age
    
    def marry(self):
        print("\n Father married to payal")

class Child(Father):
    '''This is a Child class'''

    def __init__(self, fname, fcomplexion, fage, cname, ccomplexion, cage): #here constructor is overridden
        super().__init__(fname, fcomplexion, fage)
        self.childname = cname
        self.childcomplexion = ccomplexion
        self.childage = cage
    
    def marry(self): #here method is overridden
        print("\n Child married to seema")
    
    def get_family_details(self):
        print(f'''
    Father Name - {self.fathername}
    Father Age - {self.fatherage}
    Father Complexion - {self.fathercomplexion}

    Child Name - {self.childname}
    Child Age - {self.childage}
    Child Complexion - {self.childcomplexion}

        ''')

if __name__ == '__main__':

    c1 = Child('Ram', 'Brown', 63, 'Sushant', 'fair', 29)
    c1.marry()
    c1.get_family_details()
print()
        
# ------------------------------------------------------------------------------------   

#  18. access specifiers with examples

# Answer - There are three types of access specifiers in class
# public - this can be accessed within the class, outside the class, anywhere
# protected - this can be accessed within the class and its subclass, it is defined with single underscore
# private - this can be accessed only within the class, it is defined using __private. we can also access private member outside the class using name jangling concept

class Company:
    '''This Company class'''

    def __init__(self, name, strength):
        self.companyname = name #declaring public member
        self._companynamestrength = strength #declaring protected member
        self.__companypolicies = "Bond non-breakable" #declaring private member

    def get_company_details(self):
        # accessing pubic, protected, private inside class
        print(f''' 
        Company Name - {self.companyname}
        Company Strength - {self._companynamestrength}
        Company Policies - {self.__companypolicies}
        ''')

# c1 = Company('RajaSoftware', 300)
# c1.get_company_details()

# print(c1.companyname) #accessing public method outside the class
# print(c1._companynamestrength) #accessing protected method outside the class, but this is not recommended to perform
# print(c1.__companypolicies) #we cannot access private method outside the class..if we want to access then we can use name jangling concept to acheive it.


class Employee(Company):
    '''This is Employee class, inherited Company class'''

    def __init__(self, name, strength, ename, esalary):
        super().__init__(name, strength)
        self.employeename = ename
        self.employeesalary = esalary
        
    
    def get_employee_details(self):
        # accessing public member and protected member of parent class inside child class
        print(f'''
        Employee Name - {self.employeename}
        Employee Salary - {self.employeesalary}
        Employee Company Name - {self.companyname}
        Employee Company Strength - {self._companynamestrength}

        ''')

if __name__ == '__main__':
    e1 = Employee('RajaSoft', 400, 'Sushant', 45000)
    e1.get_employee_details()

# ------------------------------------------------------------------------------------------------------------------------------------
# 19. name mangling

# Answer - name mangling allows to us to access private members inside outside the class and in subclass using _classname__membername

class Company:
    '''This Company class'''

    def __init__(self, name, strength):
        self.companyname = name #declaring public member
        self._companynamestrength = strength #declaring protected member
        self.__companypolicies = "Bond non-breakable" #declaring private member

    def get_company_details(self):
        # accessing pubic, protected, private inside class
        print(f''' 
        Company Name - {self.companyname}
        Company Strength - {self._companynamestrength}
        Company Policies - {self.__companypolicies}
        ''')
c1 = Company('Neosoft', 450)
print(c1._Company__companypolicies) #accessing private members outside the class using name jangling concept

class Employee(Company):
    '''This is Employee class, inherited Company class'''

    def __init__(self, name, strength, ename, esalary):
        super().__init__(name, strength)
        self.employeename = ename
        self.employeesalary = esalary
        
    
    def get_employee_details(self):
        # accessing private member inside child class using name jangling concept
        print(f'''
        Employee Name - {self.employeename}
        Employee Salary - {self.employeesalary}
        Employee Company Name - {self.companyname}
        Employee Company Strength - {self._companynamestrength}
        Employee Company Policies - {self._Company__companypolicies}

        ''')

if __name__ == '__main__':
    e1 = Employee('RajaSoft', 400, 'Sushant', 45000)
    e1.get_employee_details()
         

        



        

