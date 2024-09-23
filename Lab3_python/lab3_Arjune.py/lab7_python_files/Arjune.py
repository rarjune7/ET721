"""
Ravindra Arjune 
Sep 23, Python files
"""

print("\n --------> Example 1: Python files <--------")
# pipe the users.txt file

fileusers = open("users.text", "r")

# use loop to go through each line of the file 

for eachline in fileusers:
    print(eachline)

#alternative: print(fileusers.read())

print("\n --------> Example 2: Python limit to read files <--------")
#read the first 10 characters
print(fileusers.read(10))


# close file
fileusers.close()

print("\n --------> Example 3: Python read files with 'with' and 'r' <--------")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.read()
    print(eachlines[2])

print("\n --------> Example 4: Python read files with 'split()' <--------")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    for line in eachlines:
        word = line.split()
        print(word[2])


print("\n --------> Example 4: Python read files with 'split()' <--------")

# loop to the 'users txt file and check how many users are named 'Bruce'
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    usercounter = 0 
    for line in eachlines:
        word = line.split()
        if word == "Bruce":
            usercounter += 1

print("There is {usercounter} with the name 'Bruce' ")

print("\n --------> Example 5: Python read file and check for a specific item <--------")
#loop to the 'users' txt file and check how many users are named "bruce"
def finduser(textfile,username):
    with open(textfile, "r") as fileusers:
        eachlines = fileusers.readlines()
        usercounter = 0
        for line in eachlines:
            word = line.split()
            for eachword in word:
                if eachword == username:
                    usercounter += 1
    return usercounter

user = "Bruce"
usercounter = finduser("users.txt" , user)
print(f"There is {usercounter} with the name '{user}'")

print("\n --------> Example 6: Python write file <--------")

def userreport (totalcount, username):
    with open("writeresult.txt", "w") as writeuserresult:
        writeuserresult.write(f"There is {totalcount} with the name '{username}'")

userreport(usercounter, user)

print("\n --------> Example 7: Python appending data into a file <--------")
def adduser(newuser, city, age, userfilename):
    try:
        with open(userfilename, "a") as fileusers:
            fileusers.write(f"{newuser}, {city},{age}")
    except IOError:
        print(f"Error! couldn't find file named {userfilename}")

# calling function
newusername = "Kate Spade"
city = "NYC"
age = 38
adduser(newusername, city, age, "users.txt")

print("\n --------> Exercise: <--------")

