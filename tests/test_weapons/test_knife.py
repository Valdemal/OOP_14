from pytest import fixture, raises

from fires.distance_fire import DistanceFire
from fires.melee_fire import MeleeFire
from recharges.distance_recharge import DistanceRecharge
from recharges.melee_recharge import MeleeRecharge
from weapons.knife import Knife


@fixture
def knife():
    return Knife("AK-74 bayonet")


def test_set_valid_fire(knife):
    melee_fire = MeleeFire(50)
    knife.set_fire(melee_fire)

    assert knife.fire is not None
    assert isinstance(knife.fire, MeleeFire)


def test_set_invalid_fire(knife):
    with raises(TypeError):
        distance_fire = DistanceFire(11)
        knife.set_fire(distance_fire)


def test_set_valid_recharge(knife):
    melee_recharge = MeleeRecharge()
    knife.set_recharge(melee_recharge)

    assert knife.recharge is not None
    assert isinstance(knife.recharge, MeleeRecharge)


def test_set_invalid_recharge(knife):
    with raises(TypeError):
        distance_recharge = DistanceRecharge(1, 2, 0)
        knife.set_recharge(distance_recharge)
