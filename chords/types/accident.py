from enum import Enum, unique
from functools import cached_property

STR_ACCIDENT = ["𝄫", "♭", "♮", "♯", "𝄪"]


@unique
class Accident(Enum):
    DOUBLE_FLAT = -2
    FLAT = -1
    NATURAL = 0
    SHARP = 1
    DOUBLE_SHARP = 2

    @cached_property
    def symbol(self) -> str:
        return STR_ACCIDENT[2 + self.value]

    def __repr__(self: "Accident"):
        return f"<Accident: {self.name}>"

    @classmethod
    def from_str(cls, accident: str) -> "Accident":
        if accident in STR_ACCIDENT:
            return Accident(STR_ACCIDENT.index(accident) - 2)
        elif accident == "b":
            return cls.FLAT
        elif accident == "#":
            return cls.SHARP
        else:
            raise ValueError(f"Invalid string. Expected: {STR_ACCIDENT},  b or #.")

    def to_str(self: "Accident") -> str:
        return self.symbol

    @classmethod
    def from_int(cls, integer: int) -> "Accident":
        return Accident(integer)

    def to_int(self) -> int:
        return self.value


DOUBLE_FLAT = Accident.DOUBLE_FLAT
FLAT = Accident.FLAT
NATURAL = Accident.NATURAL
SHARP = Accident.SHARP
DOUBLE_SHARP = Accident.DOUBLE_SHARP