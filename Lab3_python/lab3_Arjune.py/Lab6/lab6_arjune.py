""""

Ravindra Arjune
Sep 20, Python classes

"""


print("\n -------> Example 1: exception handling <---------")
def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        hours /= h # hours = hours/h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined")
    except ValueError:
        print(f"Input value was not a number.")
    except:
        print("Program has error")
# calling the function

print(hour_ratio())
print("\n ------ > End of program <--------")
