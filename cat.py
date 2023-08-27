from datetime import date
# from [file] import [Class]
from food import Food


class Cat:
    def __init__(self,
                 n: str,
                 a: int,
                 color: str):
        self.name = n
        self.__age = a
        self.color = color
        self.energy = 100

    @property
    def age(self):
        if self.__age < 1:
            return 'Es un minino'
        elif 1 < self.__age < 4:
            return 'Es joven'
        elif 4 < self.__age < 10:
            return 'Es adulto'

        return 'Es anciano'

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise Exception('Edad inválida')
        else:
            self.__age = value

    def meow(self):
        print(self.name)
        print('Meoooooooooooooow')

    def run(self):
        if self.energy > 0:
            self.energy -= 10
            print(f"{self.name}: Estoy corriendo...")
        else:
            print(f"{self.name}: No puedo... estoy cansadito")

    def eat(self, food: Food):
        today = date.today()
        if food.exp_date > today:
            self.energy += food.energy
        else:
            days = (today - food.exp_date).days
            consumed_energy = days * food.energy

            self.energy = max(self.energy - consumed_energy, 0)

    def __str__(self):
        result = 'Información del gato: \n'
        result += 'Nombre: ' + self.name + '\n'
        result += 'Edad: ' + str(self.__age) + '\n'
        result += 'Energía: ' + str(self.energy)

        return result
