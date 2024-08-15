def add(a, b):
    c = a+b
    return(c)

def subtract(a, b):
    c = a-b
    return(c)

def multiply(a, b):
    c = a*b
    return(c)

def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print('Division by zero')

print(add(5, 6))
print(subtract(100, 33))
print(multiply(12, 5))
print(divide(2, 0))