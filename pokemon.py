import random

### THIS CLASS DEFINES THE NAME OF THE POKEMON BASED ON ITS TYPE COMBINATION ###
class Pokemon():
    outcomes = {"Normal" : "Ghost", 
                "Fire" : ["Grass" , "Ice" , "Bug" , "Steel" , "Fairy"], 
                "Water" : ["Fire" , "Ice" , "Steel" , "Ground" , "Rock"],
                "Electric" : ["Flying" , "Steel" , "Water"], 
                "Grass" : ["Water" , "Electric" , "Ground" , "Rock"], 
                "Ice" : ["Grass" , "Ground" , "Flying" , "Dragon"],
                "Fighting" : ["Bug" , "Rock" , "Dark" , "Normal" , "Ice" , "Steel"], 
                "Poison" : ["Grass" , "Fighting" , "Bug" , "Fairy"], 
                "Ground" : ["Poison" , "Rock" , "Electric" , "Fire" , "Steel"],
                "Flying" : ["Grass" , "Fighting" , "Bug"], 
                "Psychic" : ["Fighting" , "Poison"], 
                "Bug" : ["Grass" , "Psychic" , "Dark" , "Ground"],
                "Rock" : ["Fire" , "Ice" , "Flying" , "Bug" , "Normal" , "Flying" , "Poison"],
                "Ghost" : ["Psychic" , "Poison" , "Bug"], 
                "Dragon" : ["Fire" , "Water" , "Electric" , "Grass"], 
                "Dark" : ["Psychic" , "Ghost"],
                "Steel" : ["Ice" , "Rock" , "Fairy" , "Grass" , "Normal" , "Flying" , "Psychic" , "Bug" , "Dragon"], 
                "Fairy" : ["Fighting" , "Dragon" , "Dark" , "Bug"]}
    
    def __init__(self, name, type1, type2, attack1, attack2):
        self.name = name 
        self.type1 = type1
        self.type2 = type2
        self.attack1 = attack1
        self.attack2 = attack2
        self.defeats1 = self.outcomes[self.type1]
        self.defeats2 = self.outcomes[self.type2]

    ### DESCRIBES AND PRINTS OUT WHAT HAPPENS WHEN ONE TYPE FACES ANOTHER ###
    def battle(self, other):
        if self.type1 in other.defeats1:
            winner = other
            loser = self
            print("Their", winner.name, "has won the round.")
            print("Your", loser.name, "has fainted." )
            return winner, loser
        elif other.type1 in self.defeats1:
            winner = self
            loser = other
            print("Your", winner.name, "has won the round.")
            return winner, loser
        else:
            print("The Pokemon are evenly matched and attack again!")
            if self.type2 in other.defeats2:
                winner = other
                loser = self
                print("Your", loser.name, "used", loser.attack2)
                print("Their", winner.name, "used", winner.attack2)
                print("Their", winner.name, "has won the round.")
                print("Your", loser.name, "has fainted." )
                return winner, loser
            elif other.type2 in self.defeats2:
                winner = self
                loser = other
                print("Your", winner.name, "used", winner.attack2)
                print("Their", loser.name, "used", loser.attack2)
                print("Your", winner.name, "has won the round.")
                return winner, loser
            else:
                result = [self, other]
                winner = random.choice(result)
                if winner == self:
                    winner = self
                    loser = other
                    print("Your", winner.name, "used", winner.attack2)
                    print("Their", loser.name, "used", loser.attack2)
                    print("It is still even! We'll see who's tougher...")
                    print("Your", winner.name, "has won the round.")
                else:
                    winner = other
                    loser = self
                    print("Your", loser.name, "used", loser.attack2)
                    print("Their", winner.name, "used", winner.attack2)
                    print("It is still even! We'll see who's tougher...")
                    print("Their", winner.name, "has won the round")
                    print("Your", loser.name, "has fainted." )

            if winner == self:
                return self, other
            else:
                return other, self
            #print(random.choice(['It is a draw, but your pokemon has still come out on top!', 'It is a draw but your Pokemon did not quite make it.']))
            #print(winner.name, " is the winner.")
    
    ## TODO: decide how to print pokemon
    def __str__(self):
        return self.name
    
    