"""
Trabajando con clases y POO (programación orientada a objetos)
"""

class Thing:
    pass

cosa = Thing()

class Fruit:
    def __init__(self):
        print('objeto fruta iniciado')

fruit = Fruit()

# argumentos del constructor
class Person:
    """ Esta es la documentación de la clase Person """
    COUNTER = 0

    def __init__(self, name):
        self.name = name
        self.knowledge = []
        Person.COUNTER += 1

    def __str__(self):
        return 'Me llamo {} y se: {}'.format(self.name, self.knowledge)

    def learn(self, what):
        self.knowledge.append(what)

p1 = Person('Diego')
p2 = Person('Mary')
p3 = Person('David')

p1.learn("python")
p2.learn("javascript")
p3.learn("c#")
p3.learn('C++')

print(p1)
print(p2)
print(p3)
print(Person.COUNTER)
print(p1.name)





