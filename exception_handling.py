
x = 10  # Define x before using it

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went well")
    
x = -1

if x < 0:
    raise Exception("Sorry, no number below zero")    