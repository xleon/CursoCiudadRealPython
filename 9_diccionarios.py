"""
Ejemplos para trabajar con diccionarios
"""
ALUMNO = {
    'nombre': 'Diego',
    'edad': 37,
    'clase': 'python'
}

print(ALUMNO)
print(ALUMNO['nombre'])
print(ALUMNO['edad'])

ALUMNO['edad'] = 35
print(ALUMNO)

ALUMNO['sexo'] = 'masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)
