### THIS CLASS DETERMINES WHICH THE NAMES OF THE ATTACKS SPECIFIC TO THE POKEMON. ###
### SINCE EACH POKEMON REPRESENTS A TYPE, IT WILL BE GIVEN ITS OWN UNIQUE ATTACK. ###
class Attack():

    ### DEFINES PRIMARY AND SECONDARY ATTACKS. AT THIS POINT IN OUR PROGRESS ONLY PRIMARY ATTACKS ARE BEING USED IN THE GAME ###
    def __init__(self, attack1, attack2, type1, type2):
        self.attack1 = attack1
        self.attack2 = attack2
        self.type1 = type1
        self.type2 = type2 

    ### ATTACKS ARE NAMED AND STORED BASED ON THE COMBINATION OF PRIMARY AND SECONDARY TYPES ###
    ### AGAIN EACH POKEMON HAS A COMBINATION OF TYPES UNIQUE TO THEM, MEANING THEY HAVE THEIR OWN UNIQUE MOVESET ###
    def store_attack(self):
        #Venusaur
        if self.type1 == "Grass" and self.type2 == "Poison":
            attack1 = "Frenzy Plant"
            attack2 = "Venoshock"
        #Infernape
        elif self.type1 == "Fire" and self.type2 == "Fighting":
            attack1 = "Flare Blitz"
            attack2 = "Close Combat"
        #Swampert
        elif self.type1 == "Water" and self.type2 == "Ground":
            attack1 = "Muddy Water"
            attack2 = "Mud Bomb"

