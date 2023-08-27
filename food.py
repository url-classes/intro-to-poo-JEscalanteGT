from datetime import date


class Food:
    def __init__(self,
                 name: str,
                 energy: int,
                 exp_date: date
                 ):
        self.name = name
        self.energy = energy
        self.exp_date = exp_date
