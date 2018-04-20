"""
Ejemplos para trabajar con cadenas de texto
"""

TEXTO = 'hola mundo cruel'

print(TEXTO[0])
print(TEXTO[1])
print(TEXTO[2])
print(TEXTO[3])

print(TEXTO[5:8])
print(TEXTO[5:])
print(TEXTO[:3])

# concatenación
print(TEXTO + ' ' + TEXTO)

print(TEXTO.upper())
print(TEXTO.capitalize())
print(len(TEXTO))
print(TEXTO.split())
print(TEXTO.split('mun'))