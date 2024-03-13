class Pokemon():
    def __init__(self, name, type1, type2):
        self.name = name 
        self.type1 = type1
        self.type2 = type2
    
    def round_winner(self, other):
        if self.type1 >= self.other 