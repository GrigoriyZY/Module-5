# Задача "История строительства":

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.args = args
        cls.kwargs = kwargs
        instance = super().__new__(cls)
        House.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории.')

    # Методы сравнения количества этажей.

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    # Методы добавления количества этажей

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        elif isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value.number_of_floors
        return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        return self + value


h1 = House('ЖК Эльбрус', 10)
print(h1)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(h2)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(h3)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
