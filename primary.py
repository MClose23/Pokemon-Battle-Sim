#import random

### THIS CLASS DETERMINES WHICH TYPES BEAT OUT OTHERS ###
class Primary():
    ### DEFINES TYPE ###
    def __init__(self, type1, type2, defeats):
        self.type1 = type1 
        self.type2 = type2
        self.defeats = defeats
        #self.user_type1 = self.better_type()
        #self.round_winner = self.round_win()
 
        #NORMAL
        "Normal" > "Ghost"
        "Normal" < "Fighting" and "Rock" and "Steel"

        #FIRE
        "Fire" > "Grass" and "Ice" and "Bug" and "Steel" and "Fairy"
        "Fire" < "Water" and "Rock" and "Ground" and "Dragon"

        #WATER
        "Water" > "Fire" and "Ice" and "Steel" and "Ground" and "Rock"
        "Water" < "Grass" and "Electric" and "Dragon"

        #ELECTRIC
        "Electric" > "Flying" and "Steel" and "Water"
        "Electric" < "Ground" and "Grass" and "Dragon"

        #GRASS
        "Grass" > "Water" and "Electric" and "Ground" and "Rock"
        "Grass" < "Fire" and "Ice" and "Poison" and "Flying" and "Bug" and "Dragon" and "Steel"

        #ICE
        "Ice" > "Grass" and "Ground" and "Flying" and "Dragon"
        "Ice" < "Fire" and "Fighting" and "Rock" and "Steel" and "Water"

        #FIGHTING
        "Fighting" > "Bug" and "Rock" and "Dark" and "Normal" and "Ice" and "Steel"
        "Fighting" < "Flying" and "Psychic" and "Fairy" and "Poison" and "Bug"

        #POISON
        "Poison" > "Grass" and "Fighting" and "Bug" and "Fairy"
        "Poison" < "Ground" and "Psychic" and "Rock" and "Ghost" and "Steel"

        #GROUND
        "Ground" > "Poison" and "Rock" and "Electric" and "Fire" and "Steel"
        "Ground" < "Water" and "Grass" and "Ice" and "Bug"

        #FLYING
        "Flying" > "Grass" and "Fighting" and "Bug"
        "Flying" < "Electric" and "Ice" and "Rock" and "Steel"

        #PSYCHIC
        "Psychic" > "Fighting" and "Poison"
        "Psychic" < "Steel" and "Bug" and "Ghost" and "Dark"

        #BUG
        "Bug" > "Grass" and "Psychic" and "Dark" and "Ground"
        "Bug" < "Fire" and "Poison" and "Flying" and "Ghost" and "Steel" and "Fairy" and "Rock"

        #ROCK
        "Rock" > "Fire" and "Ice" and "Flying" and "Bug" and "Normal" and "Flying" and "Poison"
        "Rock" < "Fighting" and "Ground" and "Steel" and "Water" and "Grass"

        #GHOST
        "Ghost" > "Psychic" and "Poison" and "Bug"
        "Ghost" < "Dark" and "Normal"

        #DRAGON
        "Dragon" > "Fire" and "Water" and "Electric" and "Grass"
        "Dragon" < "Steel" and "Ice" and "Fairy"

        #DARK
        "Dark" > "Psychic" and "Ghost"
        "Dark" < "Fighting" and "Fairy" and "Bug"

        #STEEL
        "Steel" > "Ice" and "Rock" and "Fairy" and "Grass" and "Normal" and "Flying" and "Psychic" and "Bug" and "Dragon"
        "Steel" < "Fire" and "Water" and "Electric" and "Fighting" and "Ground"

        #FAIRY
        "Fairy" > "Fighting" and "Dragon" and "Dark" and "Bug"
        "Fairy" < "Fire" and "Poison" and "Steel"

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.primary = Primary()

fire = Primary("Fire", "Grass")
grass = Primary("Grass", "Water")
water = Primary("Water", "Fire")


    
    