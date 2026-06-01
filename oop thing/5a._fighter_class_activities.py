#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random, time


class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        return print(self.name + ': ' + 'health:'+ str(self.__health))
    
    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(int(self.weapon / 2), int(self.weapon * 2))
        print('attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(int(self.weapon / 2), int(self.weapon * 2))
        target = random.randint(2, 6)
        print(f'Hit timer in exactly {target} secs')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3- abs(target-time_taken)
        if multiplier < 2:
            multiplier = 0

        print('attack power:', attack_power)
        print('multiplier:', multiplier)
        return attack_power*multiplier
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.__health -= damage
            print('damage:', damage)
        else:
            print('no damage')

you = Fighter('You', 100, 60, 20)
troll = Fighter('troll', 200, 30, 10)

you.report()
troll.report()
print(' ')

while True:
    print('you attak troll!')
    troll.defend(you.skill_attack())
    troll.report()
    time.sleep(2)
    print(' ')
    if troll.is_dead():
        print('you win')
        break

    print('troll attack you!')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(2)
    print(' ')
    if you.is_dead():
        print('you lose')
        break


        
