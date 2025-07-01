'''
def greet(mate):
    print(f"HEllo, {mate}")
    
greet("Alice")

def add(a, b):
    return a + b

result = add(2, 5)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(mate, greeting="Hello"):
    print(f"{greeting}, {mate}")
    

greet("Bob", "Good Morning")    