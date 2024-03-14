import pokemon
import party
import attack
import primary 

#1 Introduction to the game.
print("Welcome to Pokemon Battle Simulator")
print("To begin, select your starting pokemon.")

#2 3 Pokemon in party to select from.
Venusaur = pokemon.Pokemon("Venusaur", "Grass", "Poison")
Infernape = pokemon.Pokemon("Infernape", "Fire", "Fighting")
Swampert = pokemon.Pokemon("Venusaur", "Water", "Ground")

# 2 Users each have a party of 3 Unique Pokemon
User = party.Party("User")
for pokemon in party:
    party.pokemon.append(input)
Computer = party.Party("Computer")
for pokemon in party:
    party.pokemon.append(input)

# Player Selects Pokemon 1 from party and CPU Selects Pokemon 1 party at random
Ven_Attack = attack.Attack("Grass", "Poison")
Inf_Attack = attack.Attack("Fire", "Fighting")
Smp_Attack = attack.Attack("Water", "Ground")

# Each Pokemon uses their attack

# One Wins, One Loses
primary_type = primary.Primary(self.type1)