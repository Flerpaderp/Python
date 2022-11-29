# 1. Allow user to pick the file 
# 2. Check if the file exists.  If exists, add to it.  If doesn't, create it.
# 3. Use a loop and write some numbers to the file
# 4. Add extras if you like.


import os
clear = lambda: os.system('clear')

userfile = input("enter the name of the file you would like to create or add to: ")
f = open(userfile, "a")

def userinput():
    userinput = input("what would you like to add? ")
    f.write(userinput)

def askForItems():
    print("How many items do you have to add to your list")
    itemCount = input()
    if itemCount.isdigit():
        return int(itemCount)
    else:
        print("Looks like you had an error, valid inputs are numbers.")
        askForItems()

numberOfReceiptItems = 0
itemsEntered = 0

numberOfReceiptItems = askForItems()

while numberOfReceiptItems > 0 and itemsEntered < numberOfReceiptItems:
    itemsEntered += 1
    clear()
    print("Enter your line item", "(",itemsEntered,"/",numberOfReceiptItems,")")

    userinput()

f.close()
file1 = open(userfile, "r")
print(file1.read())




