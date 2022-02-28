# In this simple RPG game, the hero fights the goblin. He has the options to:

# This set of code is part 1, steps 1 - 7 ()

#from socket import herror

#========================================================================
# --> Felipe/Chewie's RPG <--

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        
        if self.health > 0:
            return True
        else:
            return False
        
#--------------------------------------------------------------------
        
class Hero(Character):
    def __init__(self, health, power):
        super(Hero, self).__init__(health, power)
    def attack(self, enemy):
        enemy.health -= self.power 
    def print_status(self):
            print(f"You have {self.health} health and {self.power} attack power.")


class Goblin(Character):
    def __init__(self, health, power):
        super(Goblin, self).__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power 

    def print_status(self):
        print(f"The rancid goblin has {self.health} health and {self.power} attack power.")


class Zombie(Character):
    def __init__(self, health, power):
        super(Zombie, self).__init__(health, power)

    def attack(self, enemy):
        enemy.health != self.power

    def print_status(self):
        print(f"The shambling zombie has {self.health} health and {self.power} attack power.")

#--------------------------------------------------------------------

hero = Hero(10, 5)      
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)
# medic = Medic(8, 2)
# shadow = Shadow(1, 2)
# behemoth = Behemoth(15, 30)
# golem = Golem(25, 2)

#--------------------------------------------------------------------
def main():
    
    while goblin.alive() > 0 and hero.alive(): 
        
        hero.print_status()
        goblin.print_status()
        print()
        print("What will you do, Hero?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            
            hero.attack(goblin) 
            print("You do {} damage to the goblin.".format(hero.power))
            not (False)
            if not goblin.alive():
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive(): 
            
            goblin.attack(hero) 
            print("The goblin does {} damage to you.".format(goblin.power))
            if not hero.alive():
                print("You are dead.")

main()

