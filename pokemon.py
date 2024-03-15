import random

### THIS CLASS DEFINES THE NAME OF THE POKEMON BASED ON ITS TYPE COMBINATION ###
class Pokemon():
    outcomes = {"Fire" : "Grass", 
                "Grass" : "Water", 
                "Water" : "Fire"}
    
    # In the future, add type2, add attack?
    def __init__(self, name, type1, attack):
        self.name = name 
        self.type1 = type1
        #self.type2 = type2
        self.attack = attack
        self.defeats = self.outcomes[self.type1]

    ### DESCRIBES AND PRINTS OUT WHAT HAPPENS WHEN ONE TYPE FACES ANOTHER. A DRAW RESULTS IN ONE OF THE TWO POKEMON CHOSEN TO RANDOMLY WIN THE ROUND. ###
    def battle(self, other):
        if self.type1 == other.defeats:
            winner = other
            loser = self
            print(self.name, "has won the round!")
            return winner, loser
        elif other.type1 == self.defeats:
            winner = self
            loser = other
            print(self.name, "has fainted. You have lost the round.")
            return winner, loser
        elif self.type1 == other.type1:
            winner = random.choice([self, other])
            print(winner.name, " is the winner.")

            if winner == self:
                return self, other
            else:
                return other, self
            #print(random.choice(['It is a draw, but your pokemon has still come out on top!', 'It is a draw but your Pokemon did not quite make it.']))
            #print(winner.name, " is the winner.")
        else:
            return "Oops, something went wrong."
    

    
    