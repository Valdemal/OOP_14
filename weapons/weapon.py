from abc import ABC, abstractmethod
from typing import Type
from parameters_validation import validate_parameters, non_empty

from fires.fire import Fire
from recharges.recharge import Recharge
from target import Target


class Weapon(ABC):

    @validate_parameters
    def __init__(self, name: non_empty(Type[str])):
        self.__name = name
        self.__fire = None
        self.__recharge = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def fire(self) -> Fire:
        return self.__fire

    @property
    def recharge(self) -> Recharge:
        return self.__recharge

    @abstractmethod
    def type(self) -> str:
        pass

    def set_name(self, name: non_empty(Type[str])):
        self.__name = name

    def set_fire(self, fire: Fire):
        self.__fire = fire

    def set_recharge(self, recharge: Recharge):
        self.__recharge = recharge

    def shoot(self, target: Target):
        if self.recharge.is_ready():
            self.fire.use(target)
            self.recharge.decrease_ammo()

    def reload(self):
        self.recharge.reload()

    def __str__(self) -> str:
        res = f'{self.__name} characteristics:\n'
        res += f'\ttype: {self.type()}\n'
        res += f'\t{self.fire}\n'

        recharge_str = str(self.recharge)
        if recharge_str != '':
            res += '\t' + recharge_str

        return res
