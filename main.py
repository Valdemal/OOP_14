from fire import Fire
from target import Target
from weapon import Weapon


class DistanceFire(Fire):
    def __init__(self, damage: float):
        super().__init__(damage)


class AssaultRifle(Weapon):
    def __init__(self, name):
        super().__init__(name)

    def type(self) -> str:
        return "Assault rifle"


if __name__ == '__main__':
    ak = AssaultRifle("AK-47")
    ak.set_fire(DistanceFire(35))

    print(ak)
    print()
    target = Target(30)
    print("Target hp before shoot:", target.hp)
    ak.shoot(target)
    print("Target hp after shoot:", target.hp)
