#!/usr/bin/python3
#Student class inherits objects/methods from Person class 
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        '''when adding an init func, this class will no longer
        inherit the parent's init func, therefore add super() '''
        super().__init__(fname,lname) 
        '''will make this class to inherit methods from Person class''' 
        self.gradyear=year
    def print_welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.gradyear)
xx=Student("Candice","Dare",2018)
xx.print_welcome()

