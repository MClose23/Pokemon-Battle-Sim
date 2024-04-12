import pokemon
import random
import player

print()
print("**************** ||| POKEMON BATTLE SIMULATOR ||| ****************")
print("  - - - - - Program made by Matthew Close and Eli Combs - - - - - ")
print()
print('                               ***               ')
print('                        *****************        ')
print('                    *************************    ')
print('                  *****************************  ')
print('                 ******************************* ')
print('                *********************************')
print('                *************       *************')
print('                ************         ************')
print('                *          **       **          *')
print('                *             ** **             *')
print('                 *                             * ')
print('                  *                           *  ')
print('                    **                     **    ')
print('                        ***           ***        ')
print('                               ***               ')
print()
print()
print("Choose Your party of 6 Pokemon from the Displayed Pokemon Below...")
print()


#GRASS POKEMON
Venusaur = pokemon.Pokemon("Venusaur", "Grass", "Poison", "Frenzy Plant", "Venoshock")
Torterra = pokemon.Pokemon("Torterra", "Grass", "Ground", "Leaf Storm", "Earthquake")
Ferrothorn = pokemon.Pokemon("Ferrothorn", "Grass", "Steel", "Power Whip", "Gyro Ball")

#FIRE POKEMON
Charizard = pokemon.Pokemon("Charizard", "Fire", "Flying", "Blast Burn", "Air Slash")
Infernape = pokemon.Pokemon("Infernape", "Fire", "Fighting", "Flare Blitz", "Close Combat")
Magcargo = pokemon.Pokemon("Magcargo", "Fire", "Rock", "Flamethrower", "Rock Slide")

#WATER POKEMON
Empoleon = pokemon.Pokemon("Empoleon", "Water", "Steel", "Hydro Cannon", "Metal Claw")
Swampert = pokemon.Pokemon("Swampert", "Water", "Ground", "Muddy Water", "Mud Bomb")
Lapras = pokemon.Pokemon("Lapras", "Water", "Ice", "Hydro Pump", "Sheer Cold")

#GROUND POKEMON
Hippowdon = pokemon.Pokemon("Hippowdon", "Ground", "Ground", "Bulldoze", "Earth Power")
Rhyperior = pokemon.Pokemon("Rhyperior", "Ground", "Rock", "Drill Run", "Rock Wrecker")
Gliscor = pokemon.Pokemon("Gliscor", "Ground", "Flying", "High Horsepower", "Aerial Ace")

#ROCK POKEMON
Aerodactyl = pokemon.Pokemon("Aerodactyl", "Rock", "Flying", "Ancient Power", "Wing Attack")
Golem = pokemon.Pokemon("Golem", "Rock", "Ground", "Stone Edge", "Stomping Tantrum")
Gigalith = pokemon.Pokemon("Gigalith", "Rock", "Rock", "Power Gem", "Rock Blast")

#STEEL POKEMON
Klinklang = pokemon.Pokemon("Klinklang", "Steel", "Steel", "Gear Grind", "Mirror Shot")
Metagross = pokemon.Pokemon("Metagross", "Steel", "Psychic", "Meteor Mash", "Psyshock")
Mawile = pokemon.Pokemon("Mawile", "Steel", "Fairy", "Iron Head", "Draining Kiss")

#ICE POKEMON
Glaceon = pokemon.Pokemon("Glaceon", "Ice", "Ice", "Freeze-Dry", "Ice Shard")
Walrein = pokemon.Pokemon("Walrein", "Ice", "Water", "Ice Fang", "Brine")
Mamoswine = pokemon.Pokemon("Mamoswine", "Ice", "Ground", "Blizzard", "Sand Tomb")

#POISON POKEMON
Galarian_Slowking = pokemon.Pokemon("Galarian Slowking", "Poison", "Psychic", "Acid", "Confusion")
Toxicroak = pokemon.Pokemon("Toxicroak", "Poison", "Fighting", "Sludge Bomb", "Brick Break")
Drapion = pokemon.Pokemon("Drapion", "Poison", "Dark", "Cross Poison", "Crunch")

#ELECTRIC POKEMON
Pikachu = pokemon.Pokemon("Pikachu", "Electric", "Electric", "Wild Charge", "Thunder Bolt")
Heliolisk = pokemon.Pokemon("Heliolisk", "Electric", "Normal", "Thunder", "Razor Wind")
Magnezone = pokemon.Pokemon("Magnezone", "Electric", "Steel", "Zap Cannon", "Flash Cannon")

#DARK POKEMON
Weavile = pokemon.Pokemon("Weavile", "Dark", "Ice", "Night Slash", "Avalanche")
Scrafty = pokemon.Pokemon("Scrafty", "Dark", "Fighting", "Beat Up", "Low Sweep")
Honchkrow = pokemon.Pokemon("Honchkrow", "Dark", "Flying", "Dark Pulse", "Fly")

#GHOST POKEMON
Chandelure = pokemon.Pokemon("Chandelure", "Ghost", "Fire", "Shadow Ball", "Overheat")
Trevenant = pokemon.Pokemon("Trevenant", "Ghost", "Grass", "Shadow Claw", "Wood Hammer")
Gengar = pokemon.Pokemon("Gengar", "Ghost", "Poison", "Phantom Force", "Sludge Wave")

#PSYCHIC POKEMON
Alakazam = pokemon.Pokemon("Alakazam", "Psychic", "Psychic", "Future Sight", "Psywave")
Gallade = pokemon.Pokemon("Gallade", "Psychic", "Fighting", "Psycho Cut", "Drain Punch")
Gardevoir = pokemon.Pokemon("Gardevoir", "Psychic", "Poison", "Psychic", "Dazzling Gleam")

#FAIRY POKEMON
Clefable = pokemon.Pokemon("Clefable", "Fairy", "Poison", "Moonblast", "Disarming Voice")
Togekiss = pokemon.Pokemon("Togekiss", "Fairy", "Flying", "Fairy Wind", "Air Slash")
Tinkaton = pokemon.Pokemon("Tinkaton", "Fairy", "Steel", "Play Rough", "Gigaton Hammer")

#DRAGON POKEMON
Garchomp = pokemon.Pokemon("Garchomp", "Dragon", "Ground", "Dragon Rush", "Dig")
Dragonite = pokemon.Pokemon("Dragonite", "Dragon", "Flying", "Draco Meteor", "Hurricane")
Haxorus = pokemon.Pokemon("Haxorus", "Dragon", "Dragon", "Outrage", "Dual Chop")

#FIGHTING POKEMON
Lucario = pokemon.Pokemon("Lucario", "Fighting", "Steel", "Aura Sphere", "Iron Tail")
Medicham = pokemon.Pokemon("Medicham", "Fighting", "Psychic", "High Jump Kick", "Zen Headbutt")
Machamp = pokemon.Pokemon("Machamp", "Fighting", "Fighting", "Dynamic Punch", "Cross Chop")

#FLYING POKEMON
Altaria = pokemon.Pokemon("Altaria", "Flying", "Dragon", "Sky Attack", "Dragon Pulse")
Staraptor = pokemon.Pokemon("Staraptor", "Flying", "Normal", "Brave Bird", "Take Down")
Drifblim = pokemon.Pokemon("Drifblim", "Flying", "Ghost", "Acrobatics", "Ominous Wind")

#BUG POKEMON
Accelgor = pokemon.Pokemon("Accelgor", "Bug", "Bug", "Bug Buzz", "Signal Beam")
Yanmega = pokemon.Pokemon("Yanmega", "Bug", "Flying", "Bug Bite", "Air Cutter")
Scizor = pokemon.Pokemon("Scizor", "Bug", "Steel", "X-Scissor", "Bullet Punch")

#NORMAL POKEMON
Snorlax  = pokemon.Pokemon("Snorlax", "Normal", "Normal", "Body Slam", "Snore")
Braviary = pokemon.Pokemon("Braviary", "Normal", "Flying", "Thrash", "Sky Drop")
Diggersby = pokemon.Pokemon("Diggersby", "Normal", "Ground", "Giga Impact", "Scorching Sands")


pokemon_list = [Venusaur, Torterra, Ferrothorn, Charizard, Infernape, Magcargo, Empoleon, Swampert, Lapras, 
                Hippowdon, Rhyperior, Gliscor, Aerodactyl, Golem, Gigalith, Klinklang, Metagross, Mawile, 
                Glaceon, Walrein, Mamoswine, Galarian_Slowking, Toxicroak, Drapion, Pikachu, Heliolisk, Magnezone, 
                Weavile, Scrafty, Honchkrow, Chandelure, Trevenant, Gengar, Alakazam, Gallade, Gardevoir, 
                Clefable, Togekiss, Tinkaton, Garchomp, Dragonite, Haxorus, Lucario, Medicham, Machamp, 
                Altaria, Staraptor, Drifblim, Accelgor, Yanmega, Scizor, Snorlax, Braviary, Diggersby]
pokemon_names = ["venusaur", "torterra", "ferrothorn", "charizard", "infernape", "magcargo", "empoleon", "swampert", "lapras", "hippowdon", "rhyperior", "gliscor", "aerodactyl", "golem", "gigalith", "klinklang", "metagross", "mawile", "glaceon", "walrein", "mamoswine", "galarian slowking", "toxicroak", "drapion", "pikachu", "heliolisk", "magnezone", "weavile", "scrafty", "honchkrow", "chandelure", "trevenant", "gengar", "alakazam", "gallade", "gardevoir", "clefable", "togekiss", "tinkaton", "garchomp", "dragonite", "haxorus", "lucario", "medicham", "machamp", "altaria", "staraptor", "drifblim", "accelgor", "yanmega", "scizor", "snorlax", "braviary", "diggersby"]

### EXTEND 6 INPUT POKEMON FROM AN INITIAL EMPTY LIST (POKEMON PARTY) ###
#PLAYERS CREATED
me = player.Player("Eli")
for i, item in enumerate(pokemon_list, 1):
        print(item, end='\n' if i % 9 == 0 else ' | ')
print()
while len(me.party) < 6:
    if len(me.party) == 0:
        user_choice = input("Select your 1st pokemon from the list: ").lower()
    elif 0 < len(me.party) < 2:
        user_choice = input("Select your 2nd pokemon from the list: ").lower()
    elif 1 < len(me.party) < 3:
        user_choice = input("Select your 3rd pokemon from the list: ").lower()
    elif 2 < len(me.party) < 4:
        user_choice = input("Select your 4th pokemon from the list: ").lower()
    elif 3 < len(me.party) < 5:
        user_choice = input("Select your 5th pokemon from the list: ").lower()
    elif 4 < len(me.party) < 6:
        user_choice = input("Select your final pokemon from the list: ").lower()
    while user_choice not in pokemon_names:
        print("Your Pokemon Does Not Exist On This List!")
        user_choice = input("Please select your next Pokemon: ").lower()
    ###TODO: match the string to a name and add to the user's party###
    for p in pokemon_list:
        if p.name.lower() == user_choice:
            me.party.append(p)
            break

them = player.Player("Matthew")

###TODO: Random choice from a list
while len(them.party) < 7:
    p = random.choice(pokemon_list)
    them.party.append(p)
    pokemon_list.remove(p)

intro_string = ""
#USER CHOOSES POKEMON

me.names = []
for p in me.party:
    me.names.append(p.name.lower())

print(intro_string)
print("Your 6 Pokemon are:")
for p in me.party:
    print(p, end = ' | ')
print()
#GAMEPLAY BATTLEs
while len(me.party) != 0 and len(them.party) != 0:
    #####FOR TESTING####
    ###TODO: Move and change
    cpu_pokemon_choice = random.choice(them.party)
    print("The opponent has chosen", cpu_pokemon_choice.name)

    user_pokemon_name_choice = input("Select your next Pokemon to battle: ").lower()
    ### INSTEAD OF "PLACEHOLDER", PROMPT THE USER TO INSERT A VALID POKEMON NAME IF 1 OF THE 3 POKEMON HAVE BEEN MISPELLED OR REPEATED (THEY HAVE ALREADY FAINTED) ###
    while user_pokemon_name_choice not in me.names:
        print("That Pokemon is not in your Party")
        user_pokemon_name_choice = input("Select your next Pokemon to battle: ").lower()
    #user_pokemon_choice = pokemon.Pokemon("Pokemon", "type1", "type2", "attack1", "attack2")
    for p in me.party:
        if p.name.lower() == user_pokemon_name_choice:
            user_pokemon_choice = p
            break

    #COMPUTER RANDOMLY CHOOSES POKEMON
    #cpu_pokemon_choice = random.choice(them.party)
    #cpu_pokemon_choice = Swampert

    
    #BATTLE
    print("##########")
    print("BATTLE!")
    print("Your", user_pokemon_choice.name, "used", user_pokemon_choice.attack1)
    print("Their", cpu_pokemon_choice.name, "used", cpu_pokemon_choice.attack1)
          
    winner, loser = user_pokemon_choice.battle(cpu_pokemon_choice)
      
    #print(winner.name, "has won the round.")

    if loser in them.party:
        them.party.remove(loser)
    elif loser in me.party:
        me.party.remove(loser)
        name = loser.name.lower()
        me.names.remove(name)
    print("The pokemon left in your party are:")
    for p in me.party:
        print(p, end = ' | ')
    print()


if len(them.party) == 0:
    print("Congratulations! You have won the game!")
elif len(me.party) == 0:
    print("You have no more Pokemon that can battle. You blacked out and rushed to a Pokecenter.")
else:
    print("There is an error.")

# battle(cpu_pokemon_choice)

# cpu_pokemon_party = [Venusaur, Infernape, Swampert]

# #1 Introduction to the game; there are 3 Pokemon in your party to choose from:
# def game_intro():
#     print("Welcome to Pokemon Battle Simulator!")
#     print("To begin, select your starting Pokemon.")      
#     print(str(user_pokemon_party))
#     response = ''
#     while response.lower() not in user_pokemon_party:
#         response = input('Please select your starter:')
#     #return response
#     me = player.Player()
#     me.party.append(Venusaur)

#     print(them.party)
#     print(me.party)

#     user_pokemon_name_choice = input("Select a Pokemon to battle:", me.party)
#     user_pokemon_choice = Venusaur
#     for p in me.party:
#         if p.name == user_pokemon_name_choice:
#             user_pokemon_choice = p

#     user_pokemon_choice = me

    

# #2 The player chooses the starter Pokemon:
# starter_pokemon = game_intro()

# #3 The CPU (Opponent) chooses 1 of 3 Pokemon at random:
# cpu_starter = random.choice(cpu_pokemon_party)

######################################## LATER BUILDS ###########################################

### FIRST USER ATTACK ###
# def first_user_sequence():
#     user_pokemon_party.remove(starter_pokemon)
#     if starter_pokemon == Venusaur:
#         return "Venusaur used" + Ven_Attack.attack1
#     elif starter_pokemon == Infernape:
#         return "Infernape used" + Inf_Attack.attack1
#     elif starter_pokemon == Swampert:
#         return "Venusaur used" + Smp_Attack.attack1
#     else:
#         return "Oops, something happened."

# ### FIRST CPU ATTACK ###
# def first_cpu_sequence():
#     cpu_pokemon_party.remove(cpu_starter)
#     if cpu_starter == Venusaur:
#         return "The opponent chose Venusaur! The opponent's Venusaur used" + Ven_Attack("Grass")
#     elif cpu_starter == Infernape:
#         return "The opponent chose Infernape! The opponent's Infernape used" + Inf_Attack("Fire")
#     elif cpu_starter == Swampert:
#         return "The opponent chose Swampert! The opponent's Swampert used" + Smp_Attack("Water")
#     else:
#         return "Oops, something happened."
    
# #4 First 2 Pokemon Battle, which results in a winner
# first_user_sequence()
# if starter_pokemon < cpu_starter:
#     first_cpu_sequence()
# first_round_winner = primary(round_winner)  #### STUCK HERE ####
# print(first_round_winner)

# ### IF USER POKEMON LOSES, PROMPTED TO CHOOSE FROM REMAINING POKEMON ###
# def new_pokemon_prompt():
#     print("Who do you choose next? " + str(user_pokemon_party))
#     response = ''
#     while response not in user_pokemon_party:
#         response = input('Please enter your next pokemon:')
#     return response

# ### ATTACK FOR NEW USER POKEMON ###
# def remaining_user_sequence():
#     next_pokemon = new_pokemon_prompt(input)
#     user_pokemon_party.remove(next_pokemon)
#     if next_pokemon == Venusaur:
#         return "Venusaur used" + Ven_Attack.attack1
#     elif next_pokemon == Infernape:
#         return "Infernape used" + Inf_Attack.attack1
#     elif next_pokemon == Swampert:
#         return "Venusaur used" + Smp_Attack.attack1
#     else:
#         return "Oops, something happened."

# ### ATTACK FOR NEW CPU POKEMON, A POKEMON CHOSEN AT RANDOM UNIQUE FROM ONE ALREADY CHOSEN ###
# def remaining_cpu_sequence():
#     cpu_next = random.choice(cpu_pokemon_party)
#     cpu_pokemon_party.remove(cpu_next)
#     if cpu_next == Venusaur:
#         return "The opponent chose Venusaur! The opponent's Venusaur used" + Ven_Attack.attack1
#     elif cpu_next == Infernape:
#         return "The opponent chose Infernape! The opponent's Infernape used" + Inf_Attack.attack1
#     elif cpu_next == Swampert:
#         return "The opponent chose Swampert! The opponent's Swampert used" + Smp_Attack.attack1
#     else:
#         return "Oops, something happened."

# #Easier Way? 'For' loop or 'While' loop?

# #5 Depending on the number of Pokemon remaining in each party, the game continues, removing elements from list until a player has no more Pokemon.
# if len(user_pokemon_party) == 0:
#     print("It appears you are all of of Pokemon. You have lost the game.")
#     pass   
# elif len(cpu_pokemon_party) == 0:
#     print("You have defeated all of the opponent's Pokemon. Congratulations!")
#     pass
# elif len(user_pokemon_party) < 1:
#     new_pokemon_prompt()
#     remaining_user_sequence()
# elif len(cpu_pokemon_party) < 1:
#     remaining_cpu_sequence()
# elif len(user_pokemon_party) < 2:
#     new_pokemon_prompt()
#     remaining_user_sequence()
# elif len(cpu_pokemon_party) < 2:
#     remaining_cpu_sequence()
# else:
#     print("Oops, something went wrong.")

# ### FUNCTION FOR HOW THE GAME WRAPS UP AFTER THE USER WINS OR LOSES ###
# def end_game():
#     print("Would you like to play again?")
#     response = ''
#     while response not in {"yes", "no"}:
#         response = input("Please enter yes or no: ")
#     return response == "yes"

# #6 User is asked to play again or exit the game.
# if end_game() == "yes":
#     game_intro()
# else:
#     exit()
