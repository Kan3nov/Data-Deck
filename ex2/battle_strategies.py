from typing import Any

from ex0.creature_base import Creature

from .battle_strat_base import BattleStrategy


class InvalidCreature(Exception):
    def __init__(self, message: str = "Invalid Creature for this strategy"
                 ) -> None:
        super().__init__(message)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCreature("Invalid Creature '{creature.name}' for"
                                  + " this normal strategy")
        return creature.attack()

    def is_valid(self, creature: Any) -> bool:
        try:
            creature.attack()
            return True
        except AttributeError:
            return False
        except Exception as e:
            print("Error validating strategy : ", e)
            return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> str:
        if not self.is_valid(creature):
            raise InvalidCreature("Invalid Creature '{creature.name}' for"
                                  + " this aggressive strategy")
        return "\n".join([creature.transform(),
                          creature.attack(),
                          creature.revert()])

    def is_valid(self, creature: Any) -> bool:
        try:
            creature.transform()
            creature.attack()
            creature.revert()
            return True
        except AttributeError:
            return False
        except Exception as e:
            print("Error validating strategy : ", e)
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> str:
        if not self.is_valid(creature):
            raise InvalidCreature("Invalid Creature '{creature.name}' for"
                                  + " this defensive strategy")
        return "\n".join([creature.attack(),
                          creature.heal()])

    def is_valid(self, creature: Any) -> bool:
        try:
            creature.attack()
            creature.heal()
            return True
        except AttributeError:
            return False
        except Exception as e:
            print("Error validating strategy : ", e)
            return False
