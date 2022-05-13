from pytest import fixture

from fire import Fire
from target import Target
from weapon import Weapon


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

    def type(self) -> str:
        return "Some type"


@fixture
def weapon():
    return SomeWeapon("AK-47")


@fixture
def target():
    return Target(100)
