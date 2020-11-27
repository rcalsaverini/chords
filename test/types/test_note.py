from chords.types.note import Note, note_from_int, note_from_str
from chords.types.letter import A, B, F, G
from chords.types.accident import FLAT, SHARP, NATURAL
import pytest
from typing import List, Tuple


@pytest.fixture
def notes():
    return [
        (Note(A, NATURAL), "A", 0),
        (Note(G, FLAT), "G♭", 9),
        (Note(A, SHARP), "A♯", 1),
        (Note(B, FLAT), "B♭", 1),
    ]


def test_letter_to_str(notes: List[Tuple[Note, str, int]]):
    for note, symbol, _ in notes:
        assert note.to_str() == symbol


def test_letter_to_int(notes: List[Tuple[Note, str, int]]):
    for note, _, number in notes:
        assert note.to_int() == number


def test_from_str(notes: List[Tuple[Note, str, int]]):
    for note, symbol, _ in notes:
        assert note_from_str(symbol) == note

    assert note_from_str("B#") == Note(B, SHARP)
    assert note_from_str("Fb") == Note(F, FLAT)


def test_from_int(notes: List[Tuple[Note, str, int]]):
    for note, _, number in notes:
        assert note_from_int(number) == note.to_sharp()
