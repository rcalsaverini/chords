from chords.types.note import Note
from chords.types.tone import Tone, tone_from_str, tone_from_int
from chords.types.letter import A, B, G
from chords.types.accident import FLAT, SHARP, NATURAL


def test_letter_to_str():
    assert Tone(Note(A, FLAT), 3).to_str() == "A♭3"
    assert Tone(Note(G, SHARP), 3).to_str() == "G♯3"
    assert Tone(Note(A, FLAT), 3).to_str() == "A♭3"
    assert Tone(Note(A, FLAT), 3).to_str() == "A♭3"


def test_letter_to_int():
    assert Tone(Note(A, SHARP), 3).to_int() == 37
    assert Tone(Note(G, FLAT), 2).to_int() == 33
    assert Tone(Note(B, FLAT), 10).to_int() == 121


def test_from_str():
    assert tone_from_str("G#10") == Tone(Note(G, SHARP), 10)
    assert tone_from_str("Ab0") == Tone(Note(A, FLAT), 0)


def test_from_int():
    assert tone_from_int(0) == Tone(Note(A, NATURAL), 0)
    assert tone_from_int(-1) == Tone(Note(G, SHARP), -1)
    assert tone_from_int(120) == Tone(Note(A, NATURAL), 10)