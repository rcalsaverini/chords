from .letter import Letter, letter_from_str
from .accident import Accident, accident_from_str, NATURAL
from dataclasses import dataclass


@dataclass
class Note:
    letter: Letter
    accident: Accident

    @property
    def symbol(self) -> str:
        return (
            f"{self.letter.symbol}"
            if self.accident == NATURAL
            else f"{self.letter.symbol}{self.accident.symbol}"
        )

    def __repr__(self: "Note"):
        return f"<Note: {self.symbol}>"

    def to_str(self: "Note") -> str:
        return self.symbol

    def to_int(self) -> int:
        return self.letter.to_int() + self.accident.to_int()

    def to_sharp(self: "Note") -> "Note":
        return note_from_int(self.to_int())


def note_from_str(note: str) -> Note:
    if len(note) == 1:
        return Note(letter_from_str(note), NATURAL)
    elif len(note) == 2:
        letter = note[0]
        accident = note[1]
        return Note(letter_from_str(letter), accident_from_str(accident))
    else:
        raise ValueError("Note symbols are expected to have 2 characters.")


def note_from_int(integer: int) -> Note:
    """
    Get Note from integer. Fall back to sharps only.
    """
    letter = "AABCCDDEFFGG"[integer % 12]
    accident = "♮♯♮♮♯♮♯♮♮♯♮♯"[integer % 12]
    return Note(letter_from_str(letter), accident_from_str(accident))
