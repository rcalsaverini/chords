from chords.types.note import Note, note_from_int, note_from_str
from chords.types.letter import A, B, C, D, E, F, G
from chords.types.accident import FLAT, SHARP, NATURAL
from chords.types.interval import (
    MAJOR_SEVENTH,
    MINOR_SECOND,
    PERFECT_FIFTH,
    PERFECT_FOURTH,
    PERFECT_OCTAVE,
    PERFECT_UNISON,
    TRITONE,
)
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


def test___sub__():
    assert Note(A, NATURAL) - Note(A, FLAT) == MINOR_SECOND
    assert Note(A, NATURAL) - Note(A, SHARP) == MAJOR_SEVENTH
    assert Note(G, NATURAL) - Note(C, NATURAL) == PERFECT_FIFTH
    assert Note(B, NATURAL) - Note(F, NATURAL) == TRITONE
    assert Note(D, FLAT) - Note(C, SHARP) == PERFECT_UNISON
    assert Note(E, SHARP) - Note(F, NATURAL) == PERFECT_UNISON
    assert Note(F, NATURAL) - Note(E, SHARP) == PERFECT_UNISON


def test___add__():
    assert Note(A, NATURAL) + MINOR_SECOND == Note(A, SHARP)
    assert Note(A, NATURAL) + MAJOR_SEVENTH == Note(A, FLAT)
    assert Note(G, NATURAL) + PERFECT_FOURTH == Note(C, NATURAL)
    assert Note(B, NATURAL) + TRITONE == Note(F, NATURAL)
    assert Note(D, FLAT) + PERFECT_OCTAVE == Note(D, FLAT)


def test___eq__():
    assert Note(A, SHARP) == Note(B, FLAT)
    assert Note(B, SHARP) == Note(C, NATURAL)
    assert Note(C, SHARP) == Note(D, FLAT)
    assert Note(D, SHARP) == Note(E, FLAT)
    assert Note(E, SHARP) == Note(F, NATURAL)
    assert Note(F, SHARP) == Note(G, FLAT)
    assert Note(G, SHARP) == Note(A, FLAT)
