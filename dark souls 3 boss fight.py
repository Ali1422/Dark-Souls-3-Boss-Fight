import random
number=int(72)
bosses=["iudex gundyr", "yhorm the giant", "abyss watchers", "high lord wolnir", "old demon king"]
characters=["mage", "assasin", "knight", "warrior", "thief"]
print("the characters you can choose from are",characters)
user_character=input("please eneter the character you would like to play:")
if user_character=="mage":
    print("you have chosen mage")
elif user_character=="assasin":
    print("you have chosen assasin")
elif user_character=="knight":
    print("you have chosen knight")
elif user_character=="warrior":
    print("you have chosen warrior")
elif user_character=="thief":
    print("you haven chosen thief")
else:
    print("error, character not available")
print("the character you have chosen is",user_character)
print("the bosses you can fight are", bosses)
user_boss=input("please select the boss you would like to fight:")
if user_boss=="iudex gundyr":
    print("you have chosen to fight iudex gundyr, the judge of ash and the one who holds the corrupted sword")
elif user_boss=="yhorm the giant":
    print("you have chosen to fight yhorm the giant, the profusive lord of the profaned capital")
elif user_boss=="abyss watchers":
    print("you have chosen to fight the abyss watchers, the ones who control the passing of the soul")
elif user_boss=="high lord wolnir":
    print("you have chosen to fight high lord wolnir, the colossal skeleton imbued with darkness")
elif user_boss=="old demon king":
    print("you have chosen to fight the old demon king, the one who is burning in the smoldering lake")
else:
    print("sorry, boss not recognized")
print("now that you are prepared for your battle, begin the fight with the boss!")
attack_dogde=int(input("enter any number >50 to attack and enter any number <50 to dogde")
if "attack_dogde" > "number":
                 print("you have struck down",user_boss"you have won this fight, find the lords of cinder unkindeled one")
elif "attack_dogde"<"number":
                 print("you have been struck down by",user_boss"YOU DIED")
else:
                 print("error, try again")


