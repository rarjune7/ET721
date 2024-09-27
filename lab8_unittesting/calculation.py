"""
Ravindra Arjune
Example 2: Calculation Testing

"""

def addthreenumbers(n1=0, n2=0, n3 = 0):
    return n1+n2+n3

def subtracttwonumbers(n1=0,n2=0):
    return n1-n2

def mutiplythreenumbers(n1=1, n2=1, n3=1):
    return n1*n2*n3

def dividetwonumbers(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Error! can't divide by zero")
    except ValueError:
        print("Error! not a nuerical value")
    except:
        print("Error! Can't divide the numbers")