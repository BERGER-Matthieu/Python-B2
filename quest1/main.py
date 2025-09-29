import hello_world as hw
import numerical_operations as no
import concat_string as cs
import punishment as p
import shopping as s

#hello_world.py
print(hw.say_hello_world())
print()

#numerical_operations.py
print(no.add(1, 2))
print(no.substract(1, 2))
print(no.multiply(6, 7))
print(no.square(2))
print(no.power(2, 4))
print()

#concat_string.py
print(cs.concat("pipi", "caca"))
print()

#punishment.py
print(p.do_punishment('Je ne jetterai plus de cacahuètes', 'sur le professeur.', 3))
print()

#numerical_operations.py
print(no.modulo(5, 2))
print(no.divide(5, 2))
print(no.integer_division(5, 2))
print()

#shopping.py
print(s.remember_the_milk(['tomatoes', 'pastas', 'salt']))
print(s.remember_the_milk([]))
print()
