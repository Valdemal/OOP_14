from pytest import fixture

from fires.fire import Fire
from recharges.distance_recharge import DistanceRecharge
from target import Target
from weapons.weapon import Weapon


class SomeFire(Fire):
    def __init__(self, damage):
        super().__init__(damage)


@fixture
def fire():
    return SomeFire(100)


class SomeWeapon(Weapon):
    def __init__(self, name):
        super().__init__(name)
        self.set_fire(SomeFire(50))
        self.set_recharge(DistanceRecharge(5, 30, 30))

    def type(self) -> str:
        return "Some type"


@fixture
def weapon():
    return SomeWeapon("AK-47")


@fixture
def target():
    return Target(100)
