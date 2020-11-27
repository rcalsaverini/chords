from .note import Note, note_from_int
from .accident import accident_from_str
from .letter import letter_from_str
from dataclasses import dataclass
from re import compile

TONE_PATTERN = compile("^([A-G])(𝄫|♭|♮|♯|𝄪|b|#)?(\\d+)$")


@dataclass
class Tone:
    note: Note
    octave: int

    def to_int(self: "Tone") -> int:
        return self.note.to_int() + self.octave * 12

    def to_str(self: "Tone") -> str:
        return f"{self.note.to_str()}{self.octave}"


def tone_from_int(integer: int) -> Tone:
    return Tone(note_from_int(integer % 12), integer // 12)


def tone_from_str(string: str) -> Tone:
    matching = TONE_PATTERN.match(string)
    if matching is None:
        raise ValueError(f"String does not match pattern {TONE_PATTERN}")
    else:
        letter, accident, octave = matching.groups()
        note = Note(
            letter_from_str(letter),
            accident_from_str(accident if accident is not None else "♮"),
        )
        return Tone(note, int(octave))