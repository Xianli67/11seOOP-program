# Learning intentions:
# - Create some default attributes of the class
# - Create the special print method that prints the status of the object

class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.ccard = 'unknown'
        self.vaccinated = False
    
    def __str__(self):
        payment_stat = 'unregistered'
        if len(self.ccard) == 19:
            payment_stat = 'registered'
        return self.name + self.category + str(self.age) + payment_stat + '\nvaccinated:' + str(self.vaccinated)
    
p1 = Pet('bonnie', 'dog', 2,)
print(p1)


#ACTIVITIES:
#1. Add a default new credit card value  of unknown

#2. In the __str__ method, let the user know if the pet has registered payment details  

#3. Add the vaccinated status  and include it in the special __str__ function