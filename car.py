class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"[Рік]: {self.year}")
        print(f"[Марка]: {self.make}")
        print(f"[Модель]: {self.model}")
