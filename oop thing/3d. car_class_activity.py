# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.sale = False

    def __str__(self):
        return '| Make: ' + self.make + ' | model: ' + self.model + ' | For sale: ' + str(self.sale)


c1 = Car('Mazda','6',2005)
c2 = Car('Totoya', '67', 2067)

cars = [c1]
cars.append(c2)

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop