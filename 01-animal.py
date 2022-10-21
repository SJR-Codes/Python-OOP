"""
* Taitotalo Python 21.10.2022
* 01-animal.py
* object oriented programming with python
* Created by Samu Reinikainen
"""

class Animal:

    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.pocket = []


    def sleep(self):
        print(f"Shhh... {self.name} is sleeping...")

    def giveItem(self, item):
        self.pocket.append(item)

    def itemsInPocket(self):
        pocket = ""
        if len(self.pocket) > 0:
            pocket = " and has"
            for item in self.pocket:
                pocket += " " + item + " &"
            pocket = pocket[:-1]
            pocket += "in pocket."

        return pocket


    #define what class instance prints when print() or str()
    def __str__(self):
        return f"{self.name} likes to eat {self.food}s" + self.itemsInPocket()


#instanssin eli olion luonti luokasta 
ape = Animal("Cheetah", "banana")
coder = Animal("Samu", "nut")

print(ape)
ape.sleep()
coder.giveItem("Calculator")
coder.giveItem("Pen")
print(coder)
