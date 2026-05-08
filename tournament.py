from ex2 import HealingCreatureFactory, TransformCreatureFactory, \
                AggressiveStrategy, DefensiveStrategy, NormalStrategy
from ex2.battle_strat_base import BattleStrategy
from ex0.factory_base import CreatureFactory
from ex2.battle_strategies import InvalidCreature

from ex0 import FlameFactory, AquaFactory


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("[ ", end="")
    for fac, strat in opps:
        print(f"({fac.create_base().__class__.__name__}" +
              f"+{strat.__class__.__name__})",
              end=" ")
    print("]")

    print("*** Tournament ***")
    print(len(opps), "opponents involved")
    print()

    for i in range(len(opps)):
        for j in range(i + 1, len(opps)):
            print("* Battle *")
            print(opps[i][0].create_base().describe())
            print("vs.")
            print(opps[j][0].create_base().describe())
            print("now fight!")
            try:
                print(opps[i][1].act(opps[i][0].create_base()))
                print(opps[j][1].act(opps[j][0].create_base()))
                print()
            except InvalidCreature as e:
                print(f"Error occurred: {e}")
                break
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
                break


flame_fac = FlameFactory()
aqua_fac = AquaFactory()
heal_fac = HealingCreatureFactory()
trans_fac = TransformCreatureFactory()

norm_stat = NormalStrategy()
aggr_stat = AggressiveStrategy()
def_stat = DefensiveStrategy()

print("Tournament 0 (basic)")
battle([(flame_fac, norm_stat), (heal_fac, def_stat)])

print("Tournament 1 (error)")
battle([(flame_fac, aggr_stat), (heal_fac, def_stat)])

print("\nTournament 2 (multiple)")
battle([(aqua_fac, norm_stat), (heal_fac, def_stat),
        (trans_fac, aggr_stat)])
