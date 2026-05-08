from ex0.creature_base import Creature
from .cap_base import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling",
                 type: str = "Grass") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str = "Bloomelle",
                 type: str = "Grass/Fairy") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others" +\
               " for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling",
                 type: str = "Normal") -> None:
        super().__init__(name, type)
        self.state = "Base"

    def attack(self) -> str:
        if self.state == "Base":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        if self.state == "Evolved":
            return f"{self.name} is already in its evolved form!"
        self.state = "Evolved"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if self.state == "Base":
            return f"{self.name} is already in its base form!"
        self.state = "Base"
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str = "Morphagon",
                 type: str = "Normal/Dragon") -> None:
        super().__init__(name, type)
        self.state = "Base"

    def attack(self) -> str:
        if self.state == "Base":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self.state == "Evolved":
            return f"{self.name} is already in its evolved form!"
        self.state = "Evolved"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if self.state == "Base":
            return f"{self.name} is already in its base form!"
        self.state = "Base"
        return f"{self.name} stabilizes its form."
