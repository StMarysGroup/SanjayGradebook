import random

class Pokeman(object):  #creates a class Pokeman
    def __init__(self, name, attackingpower, healpower, healthpoints): #players info
        self.name = name
        self.attackingpower = attackingpower
        self.healpower = healpower
        self.health = healthpoints
        self.maxhealth = healthpoints


    def takeTurn(self, other):   #a function set to demonstrate the players behaviour
        if self.health == self.maxhealth:  #checks the health
            other.takedamage(self.attackingpower)
            return self.name + " did " + str(self.attackingpower) + " damages to " + other.name
        elif self.health <=3:  #if the health is less than 3 then it will heal automatically
            self.heal()
            return self.name + " healed"
        else: #if the health is max  and health is not less than 3 then it will choose a random number and go from there
            roll = random.randint(1,10)  #give a random number between 1 to 10
            if roll < 5:
                other.takedamage(self.attackingpower)  # attacks
                return self.name + " did " + str(self.attackingpower) + " to " + other.name
            else:
                self.heal()    #else heals
                return self.name + " healed"

    def takedamage(self, damage):   # function reduces the health by the amount of other players attacking power
        self.health = self.health - damage

    def heal(self):  #heals the player by its healing power
        self.health = self.healpower + self.health
        if self.health > self.maxhealth:  #checks if the health exceeds its limit
            self.health = self.maxhealth  #make the health to default

def battle(p1, p2):  #battles between player taking 2 classes)
    while p1.health > 0 and p2.health > 0:  #loops if both the health of the players is greater than 0
        print(p1.takeTurn(p2))   #calls the class function
        print(p2.takeTurn(p1))
        print(p1.name + " has " + str(p1.health))
        print(p2.name + " has " + str(p2.health))

    if p1.health < 0:   #if the one players health is greater than 0 then the
        print(p2.name, " wins")
    else:   #else the other players win
        print(p1.name, " wins")

def main():
    pokeman1 = Pokeman("Blasto", 3, 5, 11)  #sets players info in the class
    pokeman2 = Pokeman("Pikachu",7,4,18)
    battle(pokeman1, pokeman2)
main()
