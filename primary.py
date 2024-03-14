import random

### THIS CLASS DETERMINES WHICH TYPES BEAT OUT OTHERS ###
class Primary():

    ### DEFINES TYPE ###
    def __init__(self, type1):
        self.type1 = type1 
        self.user_type1 = self.better_type
        self.round_winner = self.round_win

    ### DETAILS WHICH TYPES ARE BETTER THAN THE OTHERS ###
    def better_type(self):
        "Grass" > "Water"
        "Fire" > "Grass"
        "Water" > "Fire"

    ### DESCRIBES AND PRINTS OUT WHAT HAPPENS WHEN ONE TYPE FACES ANOTHER. A DRAW RESULTS IN ONE OF THE TWO POKEMON CHOSEN TO RANDOMLY WIN THE ROUND. ###
    def round_win(self, other):
        if self.user_type1 > other.user_type:
            print("Your Pokemon has won the round!")
        elif self.user_type1 < other.user_type:
            print("Your Pokemon has fainted. You have lost the round.")
        elif self.user_type1 == other.user_type:
            print(random.choice('It is a draw, but your pokemon has still come out on top!', 'It is a draw but your Pokemon did not quite make it.'))
        else:
            return "Oops, something went wrong."


    
    