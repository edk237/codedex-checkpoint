# Initialisation des variables
wizard = swordsman = archer = asshole = 0
hp = attack = mana = dodge = 0
character = ""

# Messages de bienvenue
print("Greetings stranger! I heard you wanted to join a guild.")
print("Let me ask you some questions first: \n")

# Questions et collecte des réponses
answers = [
    int(input("In a fight, would you rather: \n 1) Stay back \n 2) Go to the front \n 3) Analyze the situation?\n Answer:")),
    int(input("\nWhat is your favorite element?\n 1) Air and precision\n 2) Metal and strength \n 3) Fire, water, earth, mystique?\n Answer:")),
    int(input("\nWhat equipment attracts you the most?\n 1) Bow and arrows\n 2) Sword or armor\n 3) Magical staff or spellbook?\n Answer:"))
]

# Attribution des points en fonction des réponses
archer += answers.count(1)
swordsman += answers.count(2)
wizard += answers.count(3)

# Détermination du caractère final
if wizard > swordsman and wizard > archer:
    print("\nYou're for sure a wizard!")
    character = "wizard"
elif swordsman > wizard and swordsman > archer:
    print("\nYou're for sure a swordsman!")
    character = "swordsman"
elif archer > wizard and archer > swordsman:
    print("\nYou're for sure an archer!")
    character = "archer"
else:
    print("\nHmm... You don't fit into any category. You're an asshole!")
    character = "asshole"

# Assignation des stats en fonction du personnage
if character == "archer":
    hp = 300
    mana = 50
    attack = 100
    dodge = 35
elif character == "wizard":
    hp = 500
    mana = 300
    attack = 50
    dodge = 25
elif character == "swordsman":
    hp = 400
    mana = 0
    attack = 200
    dodge = 15

# Affichage des résultats
print(f"\nWell, well because you're a {character} you have: \n {hp} hp\n {mana} mana\n {attack} attack\n {dodge} dodge\n")
