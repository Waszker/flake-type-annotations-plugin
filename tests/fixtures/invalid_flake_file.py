from typing import List, Optional, Tuple, Union


class Foo:
    """Example class definition."""

    def func(self, arg: Optional[int]) -> Union[int, str]:
        """Example function definition."""
        return arg if arg is not None else "default"

    def func2(self, arg: Tuple[int]) -> List[int]:
        """Example function definition."""
        return list(arg)
