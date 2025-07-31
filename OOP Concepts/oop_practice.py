# University Management System
# OOP Concepts Practice


class Course:

    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

class User:

    def __init__(self):
        pass

    def login():
        pass

    def getRole():
        print("User")


class Employee(User):
    def __init__(self, empID, salary):
        super().__init__()
        self.empID = empID
        self.salary = salary

    

class Admin(Employee):
    def __init__(self, empID, salary):
        super().__init__(empID, salary)

    def manageUsers():
        pass

    def getRole():
        print("Admin")


class Student(User):

    def __init__(self, name, id, email, phone):
        self.name = name
        self.id = id
        self.courses = []
        self.profile = Profile(email, phone)

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} was successfully enrolled in {course.code}: {course.name}!")

    def viewCourses(self):
        for course in self.courses:
            print(f"{course.code}: {course.name} [{course.credits} Credits]")

    def getRole():
        print("Student")
        

class Profile:

    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

class Faculty(User):

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.courses = []

    def teach(self, course):
        self.courses.append(course)

    def getRole():
        print("Faculty")


class Researcher():
    def publishPaper():
        pass

class ResearchStudent(Student, Researcher):
    pass






# 🔹 8. Compile-time Polymorphism
# Create a class Calculator with add() method:

# add(a, b)

# add(a, b, c)

# Achieve this using default parameters or type checking in Python

# 🧱 PART 4: Abstraction (5 mins)
# 🔹 9. Abstraction
# Create an abstract base class Person with abstract methods getDetails()

# User inherits from it and implements the method


course1 = Course("DSA", "COMP200", 3)
course2 = Course("Basic Electronics", "CSCS105", 3)
course3 = Course("OS", "COMP301", 3)

student1 = Student("Amal Basit", "0391", "amalbasit2004@gmail.com", +923211199954)

student1.enroll(course1)
student1.enroll(course2)
student1.enroll(course3)

student1.viewCourses()