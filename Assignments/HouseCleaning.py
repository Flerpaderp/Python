import os
clear = lambda: os.system('clear')
from random import randint, random

class HouseCleaning:
    Duration = 0
    SqFt = 0
    Stories = 0

    def __init__(this, time, sqft, stories):
        this.Duration = time
        this.SqFt = sqft
        this.Stories = stories

    def findCost(this, time, sqft, stories):
        timeSpent = int(time) * 65
        sqftCost = int(sqft) * 0.10
        storyCost = int(stories) * 50
        supplies = 50
        total = timeSpent + sqftCost + storyCost + supplies
        return total

time = input("How many hours were spent cleaning?: ")
sqft = input("How many sqft is your house?: ")
stories = input("How many stories is the house?: ")
discount = input("Are you a member of the armed services? Y or N: ")

clean = HouseCleaning(time, sqft, stories)
cleanTotal = clean.findCost(time, sqft, stories)

if discount == "Y" or "y" or "yes" or "Yes":
    newCleanTotal = cleanTotal - 75
else:
    newCleanTotal = cleanTotal

print("Your total today is", newCleanTotal, "$")