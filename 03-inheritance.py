"""
* Taitotalo Python 21.10.2022
* 03-inheritance.py
* Python OOP inheritance
* Created by Samu Reinikainen
"""

class GrandParent:
    def __init__(self):
        print("GrandParent init called...")

    def familySaying(self):
        print("We're bloody Finns!")

#class Parent inherits GrandParent
class Parent(GrandParent):
    pass
    #if class has no __init__ parents __init__ is used
    #def __init__(self):
    #    print("Parent init called...")

#when class inherits another class it gets parent classes methods
anna = Parent()
anna.familySaying()