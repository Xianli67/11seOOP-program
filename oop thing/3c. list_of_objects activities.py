# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    
    def __str__(self):
        payment_stat = 'unregistered'
        if len(self.ccard) == 19:
            payment_stat = 'registered'
        
        my_stat = 'name: '+ self.name + '\ncategory: ' + self.category + '\nage: ' + str(self.age) + '\npayment status: ' + payment_stat + '\nvaccinated:' + str(self.vaccinated)
        return my_stat
    
p1 = Pet('bonnie', 'dog', 2,)
p2 = Pet('Robbert', 'rabbit', 10)
p3 = Pet(category = 'cat', name = 'ruffs', age = 67)

pets = [p1, p2, p3]
for pet in pets:
    print(pet)
    print(' ')

#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list