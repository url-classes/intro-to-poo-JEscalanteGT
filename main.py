from datetime import date
from cat import Cat
from food import Food
from math import sqrt


def main():
    # 1 - Identidad
    cat1 = Cat('Gardfield', 5, 'Anaranjado')
    cat2 = Cat('Luna', 2, 'Café')
    cat3 = Cat('Misho', 1, 'Negro')

    print(id(cat1))
    print(id(cat2))
    print(id(cat3))

    # 2 - Estado
    print('Nombre:', cat1.name)
    print('Edad:', cat1.age)

    cat1.name = 'Señor Gato'
    cat1.age = 1

    print('Muchas líneas de código...')

    print('Nombre:', cat1.name)
    print('Edad:', cat1.age)

    # 3 - Comportamiento
    print('Energía al iniciar:', cat1.energy)
    cat1.run()
    print('Energía al finalizar:', cat1.energy)

    n = int(input('Ingrese un número: '))
    resultado = sqrt(n)
    print('El resultado es:', resultado)


main()
