from target import Target
from pytest import raises, fixture


def test_valid_creation():
    target = Target(100)
    assert target is not None
    assert isinstance(target, Target)


def test_invalid_creation():
    with raises(ValueError):
        Target(-1)


@fixture
def target():
    return Target(100)


def test_valid_set_hp(target):
    hp = 25
    target.set_hp(25)
    assert target.hp == hp


def test_invalid_set_hp(target):
    with raises(ValueError):
        target.set_hp(-2)


def test_non_killable_reduce_hp(target):
    damage = target.hp / 2
    hp = target.hp
    target.reduce_hp(damage)

    assert target.hp == hp - damage


def test_killable_reduce_hp(target):
    damage = target.hp + 1
    target.reduce_hp(damage)

    assert target.hp == 0
