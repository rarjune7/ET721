"""
Ravindra Arjune
Lab 3, Python review
"""

print("---------> Example 1: control flow <----------- ")
labs = int(input("Enter labs' grade: "))
exams = int(input("Enter exams' grade: "))
gpa = ''
finalgrade = 0


if (0<=labs<=100 and 0<=exams<=100):
    finalgrade = (labs + exams) / 2
    
if (100>= finalgrade>=90):
    gpa = 'A'
    
elif (90>finalgrade>=80):
    gpa = 'B'
    
elif (80>finalgrade>=70):
    gpa = 'C'
    
elif (70>finalgrade>=60):
    gpa = 'D'
    
elif (60>finalgrade>=0):
    gpa = 'F'

else:
    if not(0<=labs<=100):
        print(f"Grade for lab {labs} is invalid")
    elif not(0<=labs<=100):
        print(f"Grade for exams {exams}is invalid")
    else:
        print(f"Grade for labs {labs} and {exams} are invalid")
    gpa = 'UNDEFINED'

print(f"Your final grade in the class is {finalgrade} = {gpa}")


print("---------> Example 2: Loops <--------------")

SECRET = 8

userguest = int(input("Guess a number between 1 and 10: "))
while not(SECRET ==userguest):
    userguest = int(input("Wrong guess :( Guess again: "))

print(f"congrats! {userguest} is the right number :)  ")

print("---------> Example 3: Loops, break statement <--------------")

balance = 1000
widthdraw = 0
deposit = 0

while True:
    userinput = input("Do you want to widthdraw, w or deposit, d ? ") 
    if userinput == 'w' or userinput == 'W':
       W_amount = int(input('How much do you wnat ot widthdraw? '))
       if W_amount>balance:
           print(f"Unsuficient funds ! You can't withdraw more than {balance}")
       else:
        balance -= W_amount
    elif userinput == 'd' or userinput == 'D':
        d_amount = int(input('How much do you want to deposit? '))
        balance += d_amount
        print(f"Your new balance is {balance}")
    else:
        print("Invalid selection!")
       
    choice = input("Would you like to do another transaction? (y,n)")
    if not(choice =='y' or choice == 'Y'):
        break

print("Thank you for banking with us! ")
    



