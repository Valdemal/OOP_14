from numbers import Number
from time import sleep
from typing import Type

from parameters_validation import validate_parameters, non_negative, parameter_validation
from parameters_validation.builtin_validations import _build_arg

from recharges.recharge import Recharge


@parameter_validation
def is_natural(number: Number, arg_name: str, arg_type: type = str):
    """
    Validation to reject negative numbers.

    >>> from parameters_validation import validate_parameters
    ...
    ... @validate_parameters
    ... def foo(bar: non_negative(float)):
    ...     print(bar)
    ...
    ... foo(0.0)   # valid: number is non-negative
    ... foo(-0.1)   # invalid: number is negative

    :param number: the parameter's value being validated
    :param arg_name: the argument name for this parameter (provided by the :meth:`parameter_validation` decorator)
    :param arg_type: the argument type for this parameter (provided by the :meth:`parameter_validation` decorator)
    :return: None
    :raises ValueError: invalid parameter, i.e. :param number: contains one or more whitespaces
    :raises RuntimeError: unable to validate parameter (possibly :param number: is of an unexpected type)
    """
    validation_error = None
    arg = _build_arg(arg_name, arg_type)
    try:
        if number <= 0:
            validation_error = ValueError(
                "Parameter `{arg}` cannot be negative".format(arg=arg))
    except Exception as e:
        validation_error = RuntimeError(
            "Unable to validate parameter `{arg}`: {error_name}{error}".format(arg=arg, error_name=e.__class__.__name__,
                                                                               error=e), e)
    if validation_error:
        raise validation_error


class DistanceRecharge(Recharge):
    @validate_parameters
    def __init__(self, reload_time_ms: is_natural(Type[int]), shop_size: is_natural(Type[int]),
                 initial_ammo_count: non_negative(Type[int])):

        if initial_ammo_count > shop_size:
            raise ValueError("Ammo count can't be more than shop size!")

        self.__reload_time_ms = reload_time_ms
        self.__shop_size = shop_size
        self.__current_ammo_count = initial_ammo_count

    @property
    def shop_size(self) -> int:
        return self.__shop_size

    @property
    def current_ammo_count(self) -> int:
        return self.__current_ammo_count

    def is_ready(self) -> bool:
        return self.__current_ammo_count > 0

    def reload(self):
        sleep(self.__reload_time_ms)
        self.__current_ammo_count = self.__shop_size

    def decrease_ammo(self):
        if self.__current_ammo_count > 0:
            self.__current_ammo_count -= 1

    def __str__(self):
        return f'reload time: {self.__reload_time_ms} ms\n' \
               f'\tshop size: {self.shop_size}\n' \
               f'\tammo count: {self.current_ammo_count}'
