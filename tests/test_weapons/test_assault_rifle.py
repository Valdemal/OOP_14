from pytest import raises, fixture

from fires.distance_fire import DistanceFire
from fires.melee_fire import MeleeFire
from recharges.distance_recharge import DistanceRecharge
from recharges.melee_recharge import MeleeRecharge
from weapons.assault_rifle import AssaultRifle


@fixture
def assault_rifle() -> AssaultRifle:
    return AssaultRifle("M4A1")


def test_set_valid_fire(assault_rifle):
    distance_fire = DistanceFire(25)
    assault_rifle.set_fire(distance_fire)

    assert assault_rifle.fire is not None
    assert isinstance(assault_rifle.fire, DistanceFire)


def test_set_invalid_fire(assault_rifle):
    with raises(TypeError):
        melee_fire = MeleeFire(50)
        assault_rifle.set_fire(melee_fire)


def test_set_valid_recharge(assault_rifle):
    distance_recharge = DistanceRecharge(5, 20, 2)
    assault_rifle.set_recharge(distance_recharge)

    assert assault_rifle.recharge is not None
    assert isinstance(assault_rifle.recharge, DistanceRecharge)


def test_set_invalid_recharge(assault_rifle):
    with raises(TypeError):
        melee_recharge = MeleeRecharge()
        assault_rifle.set_recharge(melee_recharge)