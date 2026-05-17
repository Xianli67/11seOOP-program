# Learning intentions:
# - Create a protected attribute
# - Create a private attribute

class Pet:
    def __init__(self, name, category, age = 0):
        self._name = name
        self.__category = category
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1

    def get_name(self):
        return self._name

    def set_name(self,new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use string as name')

    def vaccinated(self):
        self.vaccinated = True

    def clear_balance(self):
        self.account_balance = 0

    def calculate_human_age(self):
        if self.__category == 'Dog':
            print(self._name,'human age:',self.age*7)
        elif self.__category == 'Cat':
            print(self._name,'human age:',self.age*7)
    
    def __str__(self):
        payment_stat = 'unregistered'
        if len(self.__ccard) == 19:
            payment_stat = 'registered'
        
        my_stat = 'name: '+ self._name + '\ncategory: ' + self.__category + '\nage: ' + str(self.age) + '\npayment status: ' + payment_stat + '\nvaccinated:' + str(self.vaccinated)
        return my_stat
    
p1 = Pet('Bonnie', 'Cat', 10)
p1.set_name('your mom')

print(p1.get_name())
   

#ACTIVITIES:
#1. Make category a private attribute than test to make sure it can't be changed once created
#2. Add another private attribute for breed