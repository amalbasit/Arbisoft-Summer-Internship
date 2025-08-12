# Amal Basit
# OOP Concepts

# ----- Basic Classes and Objects -----

class Restaurant:

    totalBranches = 0

    def __init__(self, bLocation, isOpen):
        self.isOpen = isOpen
        self.bLocation = bLocation
        Restaurant.totalBranches += 1 

    def getIsOpen(self):

        return self.isOpen
    
    def setIsOpen(self, newIsOpen):

        self.isOpen = newIsOpen

    def getbLoc(self):

        return self.bLocation
    
    def setbLoc(self, newLoc):

        self.bLocation = newLoc

    def noOfBranches():
        return Restaurant.totalBranches

    def __str__(self):
        status = "open" if self.isOpen else "closed"
        return f"The restaurant location is {self.bLocation} and it is {status}."
    


res1 = Restaurant("DHA", True)
res2 = Restaurant("Gulberg", False)
res3 = Restaurant("Cantt", False)

print(f"Total Branches: {Restaurant.noOfBranches()}")
print("\n")

res4 = Restaurant("Model Town", True)

# res 1
res1.setIsOpen(False)
print(res1) # calling __str__
print("\n")


# res 2
print(f"Res 2 Location: {res2.getbLoc()}")
print(f"Res 2 isOpen: {res2.getIsOpen()}")
print("\n")


# res 3
res3.setbLoc("Bahria Town")
print(res3)
print("\n")

# res 4
print(res4)
print("\n")



# ----- Single Inheritance -----
# ----- Dervived class inherites from a single base class -----

import random

class User:

    def __init__(self, name, email):

        self.id = random.randint(0000, 9999)
        self.name = name
        self.email = email

    def printName(self):
        print(f"Name: {self.name}")

    def __str__(self):
        return f"User has ID: {self.id}, Name: {self.name} and Email: {self.email}"
    

user1 = User("Amal Basit", "amal@gmail.com")
print("Parent Class")
print(user1)
print("\n")

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email)
        self.address = address

    def setAddress(self, newAddress):
        self.address = newAddress

    def __str__(self):
        return super().__str__() + f" and Address: {self.address}"


c1 = Customer("Sahar Basit", "sahar@gmail.com", "14-G Street 5 DHA")

print("Child Class")
c1.printName() # parent method
c1.setAddress("15-G Street 5 DHA") # child method
print(c1) 


# ----- Multiple Inheritance -----
# ----- Derived class inherites from two or more base classes -----

class Athlete:
    def __init__(self, name, sport, position):
        self.athleteName = name
        self.sport = sport
        self.position = position

    def playSport(self):
        return f"I am playing {self.sport} as a {self.position}."

class Musician:
    def __init__(self, name, instrument):
        self.musicianName = name
        self.instrument = instrument

    def playInstrument(self):
        return f"I am playing {self.instrument}."

class MultiTalentedPerson(Athlete, Musician):
    def __init__(self, name, sport, position, instrument):
        Athlete.__init__(self, name, sport, position)
        Musician.__init__(self, name, instrument)

personA = MultiTalentedPerson("Amal", "Cricket", "Batter", "Piano")
print(personA.playSport())
print(personA.playInstrument())


# ----- Multilevel Inheritance -----
# ----- Chain-like structure, grandchild inherits from child, which inherits from parent and so on -----

class Vehicle:
    def start(self):
        print("The vehicle has started.")

class Car(Vehicle):
    def drive(self):
        print("The car is being driven.")

class ElectricCar(Car):
    def charge(self):
        print("The electric car is charging.")


carObj = Car()
elecCarObj = ElectricCar()

elecCarObj.start()
elecCarObj.drive()
elecCarObj.charge()


# ----- Runtime Polymorphism -----
# Can be achieved by method overriding

class Animal:
    def makeSound(self):
        pass

class Cat(Animal):
    def makeSound(self):
        print("Meow.")

class Dog(Animal):
    def makeSound(self):
        print("Woof.")


dogObj = Dog()
catObj = Cat()

catObj.makeSound()
dogObj.makeSound()



# ----- Compile-Time Polymorphism -----
# ----- Can be achieved by operator overloading -----

class Vector:

    def __init__(self, i, j , k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, vec):
        return Vector(self.i + vec.i, self.j + vec.j, self.k + vec.k)
    
    def __str__(self):
        return f"{self.i}, {self.j}, {self.k}"


vec1 = Vector(2, 4, 6)
vec2 = Vector(3, 5, 7)

print(vec1 + vec2)


# ----- Abstraction & Interfaces -----

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)


    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round((self.width * 2) + (self.height * 2), 2)
    

circleObj = Circle(4)
print(f"Circle Area: {circleObj.area()}")
print(f"Circle Perimeter: {circleObj.perimeter()}")

rectObj = Rectangle(3, 4)
print(f"\nRectangle Area: {rectObj.area()}")
print(f"Rectangle Perimeter: {rectObj.perimeter()}")


# ----- Encapsulation -----


class Public:

    def __init__(self, publicAttr):
        self.publicAttr = publicAttr

    def publicMember(self):
        print("This is a public member.")


class Protected:

    def __init__(self, protectAttr):
        self._protectAttr = protectAttr

    def _protectedMember(self):
        print("This is a protected member.")


class Private:

    def __init__(self, privateAttr):
        self.__privateAttr = privateAttr

    def __privateMember(self):
        print("This is a private member.")

    def accessPrivate(self): # to access private attribute
        print("\n")
        print(self.__privateAttr)
        self.__privateMember()


pub = Public("Public Value")
pro = Protected("Protected Value")
priv = Private("Private Value")

# Public 
print(pub.publicAttr)
pub.publicMember()

# Protected 
print("\n" + pro._protectAttr)     
pro._protectedMember()        

# Private - Not directly accessible (use public member to access private attribute and member)

priv.accessPrivate()


# ----- Composition ----- Strong Has-A Relationship

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine has started."

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower) # Composition

    def drive(self):
        return f"{self.make} {self.model} is being driven. {self.engine.start()}"

carObj = Car("Honda", "Civic", 190)
print(carObj.drive())


# ----- Aggregation ----- Loose Has-A Relationship, aren't dependent on each other

class Library:
    
    def __init__(self, name):
        self.libName = name
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print(f"{book.name} has been added to {self.libName}.")

    def displayBooks(self):
        print(f"Books in {self.libName}:")
        for i in self.books:
            print(f"\n{i.name} by {i.author}")


class Book:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author


book1 = Book("Salt to the Sea", "Ruta Sepetys")
book2 = Book("Harry Potter and the Prisoner of Azkaban","J.K Rowling")

libraryObj = Library("Lahore Public Library")
libraryObj.addBook(book1) # Aggregation
libraryObj.addBook(book2) # Aggregation

libraryObj.displayBooks()


# ----- Association ----- Uses-A Relationship, one class uses object of another (independent)

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        print(f"{self.name} is teaching {student.name}.")
        student.study()

student1 = Student("Amal")
teacher1 = Teacher("Mr. Hamid")

teacher1.teach(student1) # Association