from fires.distance_fire import DistanceFire
from fires.melee_fire import MeleeFire
from recharges.distance_recharge import DistanceRecharge
from target import Target
from weapons.assault_rifle import AssaultRifle
from weapons.knife import Knife


if __name__ == '__main__':

    ak = AssaultRifle("AK-47")
    ak.set_fire(DistanceFire(35))
    ak.set_recharge(DistanceRecharge(5, 30, 30))

    print(ak)
    print()
    target = Target(100)
    print("Target hp before shoot:", target.hp)
    ak.shoot(target)
    print("Target hp after shoot:", target.hp)
    print(ak)

    bayonet = Knife("AK-47 bayonet")
    bayonet.set_fire(MeleeFire(50))

    print(bayonet)
    print("Target hp before shoot:", target.hp)
    bayonet.shoot(target)

