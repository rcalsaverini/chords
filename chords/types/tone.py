from .note import Note
from .accident import Accident
from .letter import Letter
from dataclasses import dataclass
from re import compile

TONE_PATTERN = compile("^([A-G])(𝄫|♭|♮|♯|𝄪|b|#)?(\d+)$")


@dataclass
class Tone:
    note: Note
    octave: int

    def to_int(self: "Tone") -> int:
        return self.note.to_int() + self.octave * 12

    def to_str(self: "Tone") -> str:
        return f"{self.note.to_str()}{self.octave}"

    @classmethod
    def from_int(cls, integer: int) -> "Tone":
        return Tone(Note.from_int(integer % 12), integer // 12)

    @classmethod
    def from_str(cls, string: str) -> "Tone":
        matching = TONE_PATTERN.match(string)
        if matching is None:
            raise ValueError(f"String does not match pattern {TONE_PATTERN}")
        else:
            letter, accident, octave = matching.groups()
            note = Note(Letter.from_str(letter), Accident.from_str(accident))
            return Tone(note, int(octave))