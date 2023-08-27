from datetime import date
from cat import Cat
from food import Food


def main():
    cat1 = Cat('Gardfield', 5, 'Anaranjado')
    cat2 = Cat('Luna', 1, 'Gris')

    tuna = Food('Atún', 10, date(2023, 9, 22))

    cat1.run()
    cat1.run()

    cat2.run()

    print(cat1)
    cat1.eat(tuna)
    print(cat1)

    print('Edad en main:', cat1.age)
    cat1.age = -20
    print('Nueva edad:', cat1.age)


main()
