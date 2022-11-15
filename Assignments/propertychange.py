# Assignment
# Display 3 Properties
# Allow the user to change one of the properties using the key
# System will generate a random property and display all 3 properties again
'''
Initial properties will be randomly generated

1 Strength 210
2 Armor 156
3 Resistance 95

Which property would you like to change?
1

randomize
1 Life Steal 5%
2 Armor 156
3 Resistance 95

Loop until user is happy!

==========================
GIT COMMANDS TO SAVE FILES
==========================
1. Make sure you are in the root python folder
2. git status - tell us about any changes in our directory 
3. git add [file] - add file to our list of items to be committed
4. git status - should show all our changes in green
5. git commit -m "message for commit"
6. git push - sends the data to the remote repository
'''

import random
import os 

clear = lambda: os.system('clear')
clear()
propertiesList = { 1 : "Poison Resist" ,  2 : "Strength" , 3 : "Walking Speed" , 4 : "Armor" , 
5 : "Vitality" , 6 : "Mana Siphon" , 7 : "Critical Hit Chance" , 8 : "Critical Hit Damage" , 9 : "Vitality Siphon" }

def propertyValue():
     number = random.randint(50, 1500)
     return number

def giveProperty():
    value = random.choice(list(propertiesList.values()))
    return value

print ("Here are your initial values:")

attribute = giveProperty()
points = propertyValue()
skillsDictonary = {1:(str(giveProperty())) + " " + str(propertyValue()), 2: (str(giveProperty()) + " " + str(propertyValue())), 3: (str(giveProperty()) + " " + str(propertyValue()))}
print(skillsDictonary)

print("Are you happy with your selection?")
satisfied = input()
if satisfied == 'Y' or satisfied == 'y':
    quit()
if satisfied == 'N' or satisfied == 'n':
    print("Which Selection Would You Change?")
    choice = int(input())
    clear()
    print("Here is your updated list:")
    skillsDictonary.update({choice:(str(giveProperty())) + " " + str(propertyValue())})
    print(skillsDictonary)


