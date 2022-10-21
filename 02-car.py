"""
* Taitotalo Python 21.10.2022
* 02-car.py
* OOP exercizing continued
* Created by Samu Reinikainen
"""

class Car():
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} {str(self.year)}"

skoda = Car("Skoda","Fabia",2000)
volkkari = Car("Volkswagen","Golf Variant",2022)

print(skoda)
print(volkkari)
