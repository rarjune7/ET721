"""
Ravindra Arjune
Python Data and function 
"""

print("---------> Example 1: Dictionary <---------------")

car = {
"brand": "Tesla",
"model":"S",
"year" : 2023,
"last_visit": "March, 2022"
}


print(f"Best car 2022 = {car["brand"]}, model = {car["model"]}")

print("\n -------> Example 2: loop through each key in a dictionary <_-------")
for k in car:
    print(f"{k} has a value of {car[k]}")

print("\n ------> Example 3: among of key-pair in a dictionary <--------")
print(f"dictionary has {len(car)} key-value pairs")

print("\n ------> Example 4: remove a key-value pair from a dictionary<----")
car.pop("year")
print(f"dictionary after removing the 'year' key ")
for k in car:
    print(f"{k} , {car[k]}")

print("\n ------> Example 5: get value of a key<------- ")
look_key = "last_visit"
print(f"The value of key {look_key} is {car.get(look_key)}")

print("\n ------> Example 6: store data in a dictionary <---------")
phrase ="to be or not to be"
phrase = phrase.split()
print(f"phrase after split method {phrase}")
word_count_dict = {} # empty dictionary
# for loop to count how many times a word is in the dictionary
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)

print("\n ------> EXERICSE <-----------")
# given the following user list, find the number of users that use 'gmail', 'hotmail', and 'yahoo

user ="""

peter = ppan@gmail.com
diana = d@hotmail.com
Kent = ckent@yahoo.com
Bruce = bwayne@hotmail.com
tony = tstark@gmail.com
shrek = shrek@gmail.com
"""
user = user.split()
# test
user1 = user[2]
check1 = '@hotmail' in user1
print(check1)
# loop to go through each word
# save the count of emails in a dictionary

