from typing import Dict, List, Optional, Tuple, Union

SomeType = Dict[str, Union[int, str]]
SomeOtherType = Union[List[int], List[str]]


def function(*args: List[Optional[int]]) -> None:
    formatted_args: List[Union[str, int]] = [
        arg if arg is not None else "blank"
        for arg in args
    ]
    print(formatted_args)


class Foo:
    """Example class definition."""

    def func(self, arg: Optional[int]) -> Union[int, str]:
        """Example function definition."""
        return arg if arg is not None else "default"

    def func2(self, arg: Tuple[int]) -> List[int]:
        """Example function definition."""
        return list(arg)
