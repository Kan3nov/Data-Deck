from .creature_base import Creature


class Flameling(Creature):
    def __init__(self, name: str = "Flameling", type: str = "Fire") -> None:
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon",
                 type: str = "Fire/Flying") -> None:
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} uses Flamethrower!"


class Aquabob(Creature):
    def __init__(self, name: str = "Aquabob",
                 type: str = "Water") -> None:
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon",
                 type: str = "Water") -> None:
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} uses Hydro Pump!"
