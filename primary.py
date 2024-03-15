#import random

### THIS CLASS DETERMINES WHICH TYPES BEAT OUT OTHERS ###
class Primary():
    ### DEFINES TYPE ###
    def __init__(self, type1, defeats):
        self.type1 = type1 
        self.defeats = defeats
        #self.user_type1 = self.better_type()
        #self.round_winner = self.round_win()

    ### DETAILS WHICH TYPES ARE BETTER THAN THE OTHERS ###
    #def better_type(self):
        "Grass" > "Water"
        "Fire" > "Grass"
        "Water" > "Fire"

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.primary = Primary()

fire = Primary("Fire", "Grass")
grass = Primary("Grass", "Water")
water = Primary("Water", "Fire")


    
    