from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food_per_day(self):
        pass

    def describe(self):
        return f"{self.name}: {self.sound()}"

class Lion(Animal):
    def sound(self):
        return "Р-р-р"

    def food_per_day(self):
        return self.weight * 0.05

class Parrot(Animal):
    def sound(self):
        return "Привет!"

    def food_per_day(self):
        return self.weight * 0.10

class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("В зоопарк можно добавлять только животных")
        self._animals.append(animal)
    def sounds(self):
        return [animal.describe() for animal in self._animals]

    def total_food(self):
        return sum(animal.food_per_day() for animal in self._animals)

    def __len__(self):
        return len(self._animals)
