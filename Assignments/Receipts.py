
#Homework

#Bonus item - keep the screen clean (google)

#Require proper login, 3 attempts - if failed, exit app with a message like "Unable to login at this time."
#Receipt calculator - Ask the user for the amounts, Take in x amount of receipts. 
#Print receipts taken in line by line, sort list by least expensive to most expensive, $xx.xx 
#When done, display the rounded total, $xxxx 


#Begin Login portion of homework 
'''
print('Enter username and password to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='admin123' and username=='receipt_admin':
        print('Welcome!')
        break
    else:
        print('Access denied. Try again.')
        count += 1
else: print('Hacker! No more tries!')
'''
#End Login portion of homework 



import os # needed for the clear command 
clear = lambda: os.system('clear') # could also make an alias from cls to clear
import hashlib # module to allow you to hash your values 


def askForItems():
    print("How many items do you have to add to your list")
    itemCount = input() # set the value of itemCount to whatever the user puts in
    if itemCount.isdigit(): # if the users input is a digit
        clear()
        return int(itemCount) #ensure that what you return is an integer by piping what user gave you through the int function
    else:
        print("Looks like you had an error, valid inputs are numbers.") # tell them they messed up
        askForItems() #restart the function
        clear()



print('Enter correct username and password combo to continue')
count=0 #we want count to start at 0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    username = str(hashlib.sha256(username.encode('utf-8')).hexdigest())
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    if password == "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9" and username == "461916d8b01e9626c4d403f555e6d95fa6f7fc47fd8cc36b0df171f7231643f6":
        print('Welcome!')
        break
    else:
        print('Access denied. Try again.')
        count += 1 #count equals count + 1
else:
    clear()
    print(
'''
                                                                                                                     
 @@@@@@    @@@@@@@   @@@@@@@  @@@@@@@@   @@@@@@    @@@@@@      @@@@@@@   @@@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@      @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  !@@       !@@       @@!       !@@       !@@          @@!  @@@  @@!       @@!@!@@@  @@!  @@!       @@!  @@@  
!@!  @!@  !@!       !@!       !@!       !@!       !@!          !@!  @!@  !@!       !@!!@!@!  !@!  !@!       !@!  @!@  
@!@!@!@!  !@!       !@!       @!!!:!    !!@@!!    !!@@!!       @!@  !@!  @!!!:!    @!@ !!@!  !!@  @!!!:!    @!@  !@!  
!!!@!!!!  !!!       !!!       !!!!!:     !!@!!!    !!@!!!      !@!  !!!  !!!!!:    !@!  !!!  !!!  !!!!!:    !@!  !!!  
!!:  !!!  :!!       :!!       !!:            !:!       !:!     !!:  !!!  !!:       !!:  !!!  !!:  !!:       !!:  !!!  
:!:  !:!  :!:       :!:       :!:           !:!       !:!      :!:  !:!  :!:       :!:  !:!  :!:  :!:       :!:  !:!  
::   :::   ::: :::   ::: :::   :: ::::  :::: ::   :::: ::       :::: ::   :: ::::   ::   ::   ::   :: ::::   :::: ::  
 :   : :   :: :: :   :: :: :  : :: ::   :: : :    :: : :       :: :  :   : :: ::   ::    :   :    : :: ::   :: :  :  
                                                                                                                   
'''
)
    quit()



clear()
print(
'''
   ___              _      __    _____     __         __     __          
  / _ \___ _______ (_)__  / /_  / ___/__ _/ /_____ __/ /__ _/ /____  ____
 / , _/ -_) __/ -_) / _ \/ __/ / /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/
/_/|_|\__/\__/\__/_/ .__/\__/  \___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/  
                  /_/                                                    

'''
    )
numberOfReceiptItems = 0 # declaring a variable and setting it to zero
itemsEntered = 0 # declaring a variable and setting it to zero

numberOfReceiptItems = askForItems() #number of Receipt Items = the result of askForItems
receiptList = [] #creating an empty receipt list

while numberOfReceiptItems > 0 and itemsEntered < numberOfReceiptItems: # while # of items is something, and items entered is less than total items, keep asking.
    print("Enter your line item")
    item = input() #giving user chance to enter their cost
    receiptList.append(item) #append what they give you to the empty receipt list we made
    itemsEntered += 1 #items entered increase by one
    clear()



convertedList = list(map(float, receiptList ))  # new converted list, but map each of those to a float equivalent, using the variables in receiptList
totaledList = sum(convertedList) # get me a sum of all the floats in the new converted list
sortTotaledList = sorted(convertedList) #take the converted list and sort them least to greatest
clear()
print('Your list of receipt costs:')
print(*sortTotaledList, sep = "\n") #print everything in sorted list, but separate those with a new line each
print('Total Items Equal: ' + str(round(totaledList)))
# /n is a new line
# /r is a carriage return (enter key)

# try and except 

