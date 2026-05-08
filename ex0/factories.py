from .factory_base import CreatureFactory
from .creatures import Flameling, Aquabob, Pyrodon, Torragon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabob:
        return Aquabob()

    def create_evolved(self) -> Torragon:
        return Torragon()
