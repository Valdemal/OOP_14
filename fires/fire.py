from abc import ABC

from parameters_validation import non_negative, validate_parameters

from target import Target


class Fire(ABC):
    @validate_parameters
    def __init__(self, damage: non_negative(float)):
        self.__damage = damage

    @property
    def damage(self) -> float:
        return self.__damage

    def use(self, target: Target):
        target.reduce_hp(self.damage)

    def __str__(self):
        return f'damage: {self.damage} points'
