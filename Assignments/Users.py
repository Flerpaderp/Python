users = {"Sansa" : "Sansa Stark", "Dany" : "Daenerys Targaryen", "John" : "John Snow"}

def checkUser (username):
    if username in users:
        return True
    else:
        return False 

def getUser (username):
    fullname = users[username]
    return fullname 

def login ():
    print("Enter your user name:")
    username = input()
    return username 

user = login()
validUser = checkUser(user)
if validUser == False:
    print("Login Failed")

while(validUser == False):
    user = login()
    validUser = checkUser(user)

print("Login Successful: Welcome " + getUser(user))






    


# Homework 
'''
Using the login above, use a while loop
to make the system keep asking for a username 
until the user provides a username from your list.

If it's in the list, say "Login Successful"
If not in the list, say "Login Failed" + ask for the
username again 
'''


