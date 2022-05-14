from recharges.recharge import Recharge


class MeleeRecharge(Recharge):

    def __init__(self):
        pass

    def is_ready(self) -> bool:
        return True

    def decrease_ammo(self):
        pass

    def reload(self):
        pass
