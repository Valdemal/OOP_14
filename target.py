from typing import Type

from parameters_validation import validate_parameters, non_negative


class Target:

    @validate_parameters
    def __init__(self, hp: non_negative(Type[float])):
        self.__hp = hp

    @property
    def hp(self) -> float:
        return self.__hp

    @validate_parameters
    def set_hp(self, hp: non_negative(Type[float])):
        self.__hp = hp

    @validate_parameters
    def reduce_hp(self, damage: non_negative(Type[float])):
        if damage > self.hp:
            self.set_hp(0)
        else:
            self.__hp -= damage
