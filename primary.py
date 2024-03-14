import random

class primary():
    def __init__(self, type1):
        self.type1 = type1 
        self.user_type1 = self.better_type
        # Player = self.user_type1
        # CPU = other.user_type1

    def round_winnner(self, other):
        if self.user_type1 > other.user_type:
            print("Your Pokemon has won the round!")
        elif self.user_type1 < other.user_type:
            print("Your Pokemon has fainted. You have lost the round.")
        elif self.user_type1 == other.user_type:
            print(random.choice('It is a draw, but your pokemon has still come out on top!', 'It is a draw but your Pokemon did not quite make it.'))
        else:
            return "Oops, something went wrong."
    
    def better_type(self):
        "Grass" > "Water"
        "Fire" > "Grass"
        "Water" > "Fire"
    
    #def better_type(self):
        # if self.type1 == "Grass":
        #     "Grass" > "Water"
        #     "Grass" < "Fire"
        # elif self.type1 == "Fire":
        #     "Fire" > "Grass"
        #     "Fire" < "Water"
        # elif self.type1 == "Water":
        #     "Water" > "Grass"
        #     "Water" < "Fire"


    
    