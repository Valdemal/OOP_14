import copy

from tests.conftest import SomeWeapon
from weapons.weapon import Weapon
from pytest import raises


def test_valid_creation(weapon):
    assert weapon is not None
    assert isinstance(weapon, Weapon)


def test_invalid_creation():
    with raises(ValueError):
        SomeWeapon("")


def test_cast_to_str(weapon):
    s = str(weapon)
    assert s is not None
    assert s != ""


def test_shoot(weapon, target):
    target2 = copy.deepcopy(target)
    weapon.fire.use(target2)
    weapon.shoot(target)
    assert target.hp == target2.hp