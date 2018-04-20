"""
Operadores de comparación
"""

a = 21
b = 10
c = 0

if a == b:
    print('a == b')
else:
    print('a no es igual a b')

if a != b:
    print('a no es igual a b')
else:
    print('a es igual a b')

print(a < b)
print(a > b)

ES_MAYOR = a > b
print(type(ES_MAYOR))

print(a <= b)
print(a >= b)
print(a is b)

D = 5
F = 5
print(D is F)
print(D is not F)