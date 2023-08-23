from datetime import date


class Cat:
    def __init__(self, n, a, color):
        self.name = n
        self.age = a
        self.color = color
        self.energy = 100

    def meow(self):
        print(self.name)
        print('Meoooooooooooooow')

    def run(self):
        if self.energy > 0:
            self.energy -= 10
            print(f"{self.name}: Estoy corriendo...")
        else:
            print(f"{self.name}: No puedo... estoy cansadito")

    def eat(self, food):
        if food.exp_date > date.today():
            self.energy += food.energy
        else:
            self.energy -= food.energy

    def __str__(self):
        result = 'Información del gato: \n'
        result += 'Nombre: ' + self.name + '\n'
        result += 'Energía: ' + str(self.energy)

        return result


class Food:
    def __init__(self, name, energy, exp_date):
        self.name = name
        self.energy = energy
        self.exp_date = exp_date


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


main()
