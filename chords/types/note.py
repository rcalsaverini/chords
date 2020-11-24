from .letter import Letter
from .accident import Accident, NATURAL
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

    @classmethod
    def from_str(cls, note: str) -> "Note":
        if len(note) == 1:
            return Note(Letter.from_str(note), NATURAL)
        elif len(note) == 2:
            letter = note[0]
            accident = note[1]
            return Note(Letter.from_str(letter), Accident.from_str(accident))
        else:
            raise ValueError("Note symbols are expected to have 2 characters.")

    def to_str(self: "Note") -> str:
        return self.symbol

    @classmethod
    def from_int(cls, integer: int) -> "Note":
        """
        Get Note from integer. Fall back to sharps only.
        """
        letter = "AABCCDDEFFGG"[integer % 12]
        accident = "♮♯♮♮♯♮♯♮♮♯♮♯"[integer % 12]
        return Note(Letter.from_str(letter), Accident.from_str(accident))

    def to_int(self) -> int:
        return self.letter.to_int() + self.accident.to_int()

    def to_sharp(self: "Note") -> "Note":
        return Note.from_int(self.to_int())
