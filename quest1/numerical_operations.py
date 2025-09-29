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

print(power(2, 5))
print(square(3))
