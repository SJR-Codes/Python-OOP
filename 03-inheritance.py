"""
* Taitotalo Python 21.10.2022
* 03-inheritance.py
* Python OOP inheritance
* Created by Samu Reinikainen
"""

class GrandParent:
    def __init__(self):
        print("GrandParent init called...")

#class parent inherits GrandParent
class Parent(GrandParent):
    def __init__(self):
        print("Parent init called...")

        