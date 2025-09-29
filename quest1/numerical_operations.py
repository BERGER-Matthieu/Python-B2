def add(a:float, b:float):
    return a + b

def substract(a:float, b:float):
    return a - b

def multiply(a:float, b:float):
    return a * b

def square(a:float):
    return a*a

def power(a:float, b:float):
    res = a
    for i in range(b-1):
        res *= a

    return res

def modulo(a:float, b:float):
    if a == 0 or b == 0:
        return 0
    return a % b

def divide(a:float, b:float):
    if a == 0 or b == 0:
        return 0
    return a / b

def integer_division(a:float, b:float):
    if a == 0 or b == 0:
        return 0
    return a // b