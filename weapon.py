from abc import ABC, abstractmethod
from typing import Type
from parameters_validation import validate_parameters, non_empty

from fire import Fire
from target import Target


class Weapon(ABC):

    @validate_parameters
    def __init__(self, name: non_empty(Type[str])):
        self.__name = name
        self.__fire = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def fire(self) -> Fire:
        return self.__fire

    @abstractmethod
    def type(self) -> str:
        pass

    def set_fire(self, fire: Fire):
        self.__fire = fire

    def shoot(self, target: Target):
        self.fire.use(target)

    def __str__(self) -> str:
        return f'{self.__name} characteristics:\n' \
               f'\ttype: {self.type()}\n' \
               f'\t{self.fire}'
