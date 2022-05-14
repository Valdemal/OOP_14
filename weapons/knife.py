from fires.melee_fire import MeleeFire
from recharges.melee_recharge import MeleeRecharge
from weapons.weapon import Weapon


class Knife(Weapon):

    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.set_recharge(MeleeRecharge())

    def reload(self):
        pass

    def set_recharge(self, recharge: MeleeRecharge):
        if not isinstance(recharge, MeleeRecharge):
            raise TypeError

        super().set_recharge(recharge)

    def set_fire(self, fire: MeleeFire):
        if not isinstance(fire, MeleeFire):
            raise TypeError

        super(Knife, self).set_fire(fire)

    def type(self) -> str:
        return "Knife"
