"""
Ravindra Arjune
Sep 16, Python Functions
"""

import math
import random

# Example 1: define a function to print a message. This is a function that doesn't return nor pass a value

def hellofunction():
    print("Welcome to function! ")

# Example 2: Function that passes a user as argument, but it doesn't return any value

def greeting(username):
    print(f"Good Afternoon {username}")

# Example 3: Function with default parameter, but it doesn't return any value

def usercountry(countryname = "USA"):
    print(f"I am from {countryname}")

# Example 4: Function that passes and returns value 

def triplenumber(num=0):
    return 3*num

# Example 5: Function that passes two numbers and check if the two numbers are divisible by each other. The function returns True if they are divisble and and False if they are not divisable.

def isdivisible(n1,n2):
    if(n1%n2 == 0 or n2%n1 == 0):
        return True
    else:
        return False 
    
# Example 6: Function that passes a radius and returns the circumference 

def circumference(radius):
    return 2 * math.pi

# Example 8: Function that returns a random number between 1 and 6

def rolldice():
    return random. randint (1,6)

#call a function that doesn't return no pass a value

print("\n ----------> Example 1 <--------- ")
hellofunction()
hellofunction()


print("\n -----> Example 2 <----------")
username =  "peterpan123"
greeting (username) 

print("\n ----> Example 3: function with default parameter <------") 
usercountry ("China")
usercountry()

print("\n ------>Example 4: function that passes a number and returns the triple of that number <-------")
n = 9
print(f"The triple of number {n} is {triplenumber(n) }")


print("\n ---> Example 5: function that passes two numbers and returns True or False <-----")
n1 = 10
n2 = 50
check1 = isdivisible(n1,n2)
print(f"Is {n1} and {n2} divisibled? {check1}")

print("\n -----> Example 6: function that passes a radius and returns the circumference <-----")

r = 5
c = circumference(r)
print(f"A circle with radius {r} has a circumference of {c: .2f}")

print("\n -------> Example 7: random numbers <-------- ")

print(f"random number {random. random ( )}")
print(f" random uniform {random. uniform(-5,5)}")
print(f" random randint {random.randint (-10,10)}")

print("\n -------> Example 8: roll a dice <-------- ")
print(f"dice number = {rolldice()}")



print("---------> Exercise <---------")

import random

def random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def compare_number(guess, random_num):
    if random_num < guess:
        print("The number is smaller than the guess number")
    elif random_num > guess:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")


guess_number = 7
random_num = random_number(1, 10)
compare_number(guess_number, random_num)


#lucky number is 7 :)
