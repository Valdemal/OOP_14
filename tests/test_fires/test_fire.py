from pytest import raises

from fires.fire import Fire
from tests.conftest import SomeFire


def test_valid_creation():
    f = SomeFire(100)
    assert f is not None
    assert isinstance(f, Fire)


def test_invalid_creation():
    with raises(ValueError):
        SomeFire(-100)


def test_use(fire, target):
    post_hp = target.hp - fire.damage if fire.damage < target.hp else 0
    fire.use(target)
    assert target.hp == post_hp


def test_cast_to_str(fire):
    s = str(fire)

    assert s is not None
    assert s != ""