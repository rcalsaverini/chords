from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple


class Quality(Enum):
    DIMINISHED = -2
    MINOR = -1
    PERFECT = 0
    MAJOR = 1
    AUGMENTED = 2

    def to_int(self: "Quality") -> int:
        return self.value

    def invert(self: "Quality") -> "Quality":
        return {
            DIMINISHED: AUGMENTED,
            MINOR: MAJOR,
            PERFECT: PERFECT,
            MAJOR: MINOR,
            AUGMENTED: DIMINISHED,
        }[self]


class Number(Enum):
    UNISON = 0
    SECOND = 1
    THIRD = 3
    FOURTH = 5
    FIFTH = 7
    SIXTH = 8
    SEVENTH = 10
    OCTAVE = 12

    def to_int(self: "Number") -> int:
        return self.value


DIMINISHED = Quality.DIMINISHED
MINOR = Quality.MINOR
PERFECT = Quality.PERFECT
MAJOR = Quality.MAJOR
AUGMENTED = Quality.AUGMENTED

UNISON = Number.UNISON
SECOND = Number.SECOND
THIRD = Number.THIRD
FOURTH = Number.FOURTH
FIFTH = Number.FIFTH
SIXTH = Number.SIXTH
SEVENTH = Number.SEVENTH
OCTAVE = Number.OCTAVE


def is_valid_interval(quality: Quality, number: Number):
    if quality is PERFECT:
        return number in {UNISON, FOURTH, FIFTH, OCTAVE}
    elif quality in {MAJOR, MINOR}:
        return number in {SECOND, THIRD, SIXTH, SEVENTH}
    else:
        return True


@dataclass
class Interval:
    quality: Quality
    number: Number

    def __init__(self, quality: Quality, number: Number):
        if not is_valid_interval(quality, number):
            raise ValueError("Invalid combination {quality} {number}")
        super().__init__()
        self.quality = quality
        self.number = number

    def to_int(self: "Interval") -> int:
        if (self.quality, self.number) in INTERVAL_TO_SEMITONES:
            return INTERVAL_TO_SEMITONES[(self.quality, self.number)]
        else:
            raise ValueError(f"Unknown interval {self}.")

    @property
    def symbol(self) -> str:
        return interval_to_str(self)

    def __add__(self, other: "Interval") -> "Interval":
        return interval_from_int(self.to_int() + other.to_int())


PERFECT_UNISON = Interval(PERFECT, UNISON)
MINOR_SECOND = Interval(MINOR, SECOND)
MAJOR_SECOND = Interval(MAJOR, SECOND)
MINOR_THIRD = Interval(MINOR, THIRD)
MAJOR_THIRD = Interval(MAJOR, THIRD)
PERFECT_FOURTH = Interval(PERFECT, FOURTH)
TRITONE = Interval(DIMINISHED, FIFTH)
PERFECT_FIFTH = Interval(PERFECT, FIFTH)
MINOR_SIXTH = Interval(MINOR, SIXTH)
MAJOR_SIXTH = Interval(MAJOR, SIXTH)
MINOR_SEVENTH = Interval(MINOR, SEVENTH)
MAJOR_SEVENTH = Interval(MAJOR, SEVENTH)
PERFECT_OCTAVE = Interval(PERFECT, OCTAVE)

SYMBOL_TO_INTERVAL: Dict[str, Interval] = {
    "U": PERFECT_UNISON,
    "m2": MINOR_SECOND,
    "M2": MAJOR_SECOND,
    "m3": MINOR_THIRD,
    "M3": MAJOR_THIRD,
    "P4": PERFECT_FOURTH,
    "T": TRITONE,
    "P5": PERFECT_FIFTH,
    "m6": MINOR_SIXTH,
    "M6": MAJOR_SIXTH,
    "m7": MINOR_SEVENTH,
    "M7": MAJOR_SEVENTH,
    "O": PERFECT_OCTAVE,
}

SEMITONES_TO_INTERVAL: Dict[int, Interval] = {
    1: MINOR_SECOND,
    2: MAJOR_SECOND,
    3: MINOR_THIRD,
    4: MAJOR_THIRD,
    5: PERFECT_FOURTH,
    6: TRITONE,
    7: PERFECT_FIFTH,
    8: MINOR_SIXTH,
    9: MAJOR_SIXTH,
    10: MINOR_SEVENTH,
    11: MAJOR_SEVENTH,
    0: PERFECT_OCTAVE,
}

INTERVAL_TO_SYMBOL: Dict[Tuple[Quality, Number], str] = {
    (interval.quality, interval.number): symbol
    for (symbol, interval) in SYMBOL_TO_INTERVAL.items()
}

INTERVAL_TO_SEMITONES: Dict[Tuple[Quality, Number], int] = {
    (interval.quality, interval.number): semitones
    for (semitones, interval) in SEMITONES_TO_INTERVAL.items()
}

INTERVAL_TO_SEMITONES[PERFECT, UNISON] = 0
INTERVAL_TO_SEMITONES[PERFECT, OCTAVE] = 12


def interval_to_str(interval: Interval) -> str:
    if (interval.quality, interval.number) in INTERVAL_TO_SYMBOL:
        return INTERVAL_TO_SYMBOL[(interval.quality, interval.number)]
    else:
        raise ValueError(f"Unknown interval {interval}.")


def interval_from_str(string: str) -> Interval:
    if string in SYMBOL_TO_INTERVAL:
        return SYMBOL_TO_INTERVAL[string]
    else:
        raise ValueError(f"Unknown symbol for interval {string}.")


def interval_from_int(integer: int) -> "Interval":
    if integer == 0:
        return PERFECT_UNISON
    else:
        return SEMITONES_TO_INTERVAL[integer % 12]