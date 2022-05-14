from fires.distance_fire import DistanceFire
from recharges.distance_recharge import DistanceRecharge
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, name):
        super().__init__(name)

    def type(self) -> str:
        return "Assault rifle"

    def set_fire(self, fire: DistanceFire):
        if not isinstance(fire, DistanceFire):
            raise TypeError

        super(AssaultRifle, self).set_fire(fire)
        
    def set_recharge(self, recharge: DistanceRecharge):
        if not isinstance(recharge, DistanceRecharge):
            raise TypeError

        super(AssaultRifle, self).set_recharge(recharge)
