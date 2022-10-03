from __future__ import annotations


def function(*args: list[int | None]) -> None:
    formatted_args: list[str | int] = [
        arg if arg is not None else "blank" for arg in args
    ]
    print(formatted_args)


class Foo:
    """Example class definition."""

    def func(self, arg: int | None) -> int | str:
        """Example function definition."""
        return arg if arg is not None else "default"

    def func2(self, arg: tuple[int]) -> list[int]:
        """Example function definition."""
        return list(arg)
