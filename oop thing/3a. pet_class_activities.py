# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet
class Pet:
    def  __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = False
        self.card = 'unknwon'
        self.owner_name = 'unknown'
        sefl.balance = 0
p1 = Pet('bonnie', 'cat', 3)

print(p1.name)



name = 'Bonnie'
animal_category = 'Cat'
age = 4
vaccinated = False
ccard = '3423 2326 7543 1234'
billing_address = '17 parak street, The Shire 2695'
owner_name = 'Alex Jones'
account_balance = 104.95


#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)