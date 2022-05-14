from abc import ABC, abstractmethod
from time import sleep
from parameters_validation import validate_parameters, non_negative


class Recharge(ABC):
    @abstractmethod
    def is_ready(self) -> bool:
        pass

    @abstractmethod
    def decrease_ammo(self):
        pass

    @abstractmethod
    def reload(self):
        pass

    def __str__(self):
        return ""
