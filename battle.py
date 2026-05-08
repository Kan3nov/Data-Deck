from ex0 import FlameFactory, AquaFactory
from ex0.factory_base import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    try:
        base_creature = factory.create_base()
        print(base_creature.describe())
        print(base_creature.attack())
        evolv_creature = factory.create_evolved()
        print(evolv_creature.describe())
        print(evolv_creature.attack())
    except Exception as e:
        print("Error testing factory : ", e)


def battle(fac1: CreatureFactory, fac2: CreatureFactory) -> None:
    c1 = fac1.create_base()
    c2 = fac2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


print("Testing factory")
flame_fac = FlameFactory()
aqua_fac = AquaFactory()
test_factory(flame_fac)
print("\nTesting factory")
test_factory(aqua_fac)
print("\nTesting battle")
battle(flame_fac, aqua_fac)
