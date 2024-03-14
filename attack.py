class Attack():
    def __init__(self, type1, type2):
        self.type1 = type1
        self.type2 = type2 

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

