from recharges.distance_recharge import DistanceRecharge
from pytest import raises, mark

valid_params_cases = [(1, 1, 1), (5, 20, 0), (5, 20, 2)]


@mark.parametrize('reload_time, shop_size, ammo_count', valid_params_cases)
def test_valid_creation(reload_time, shop_size, ammo_count):
    recharge = DistanceRecharge(reload_time, shop_size, ammo_count)

    assert recharge is not None
    assert isinstance(recharge, DistanceRecharge)


invalid_params_cases = [
    (0, 0, 1), (1, 0, 1), (0, 0, -1), (0, -1, 0), (0, -1, -1), (-1, 0, 0),
    (-1, 0, -1), (-1, -1, 0), (-1, -1, -1), (0, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 0)
]


@mark.parametrize('reload_time, shop_size, ammo_count', invalid_params_cases)
def test_invalid_creation(reload_time, shop_size, ammo_count):
    with raises(ValueError):
        DistanceRecharge(reload_time, shop_size, ammo_count)


def test_is_ready():
    recharge = DistanceRecharge(1, 20, 15)
    assert recharge.is_ready()


def test_is_not_ready():
    recharge = DistanceRecharge(1, 20, 0)
    assert not recharge.is_ready()


def test_decrease_ammo():
    init_ammo_count = 12
    recharge = DistanceRecharge(1, 20, 12)
    recharge.decrease_ammo()
    assert recharge.current_ammo_count == init_ammo_count - 1


def test_reload():
    recharge = DistanceRecharge(1, 20, 15)
    recharge.reload()
    assert recharge.current_ammo_count == recharge.shop_size
