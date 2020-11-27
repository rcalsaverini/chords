from chords.types.interval import interval_from_str, interval_from_int
from chords.types.interval import PERFECT_UNISON
from chords.types.interval import MINOR_SECOND
from chords.types.interval import MAJOR_SECOND
from chords.types.interval import MINOR_THIRD
from chords.types.interval import MAJOR_THIRD
from chords.types.interval import PERFECT_FOURTH
from chords.types.interval import TRITONE
from chords.types.interval import PERFECT_FIFTH
from chords.types.interval import MINOR_SIXTH
from chords.types.interval import MAJOR_SIXTH
from chords.types.interval import MINOR_SEVENTH
from chords.types.interval import MAJOR_SEVENTH
from chords.types.interval import PERFECT_OCTAVE


def test_interval_to_int():
    assert PERFECT_UNISON.to_int() == 0
    assert MINOR_SECOND.to_int() == 1
    assert MAJOR_SECOND.to_int() == 2
    assert MINOR_THIRD.to_int() == 3
    assert MAJOR_THIRD.to_int() == 4
    assert PERFECT_FOURTH.to_int() == 5
    assert TRITONE.to_int() == 6
    assert PERFECT_FIFTH.to_int() == 7
    assert MINOR_SIXTH.to_int() == 8
    assert MAJOR_SIXTH.to_int() == 9
    assert MINOR_SEVENTH.to_int() == 10
    assert MAJOR_SEVENTH.to_int() == 11
    assert PERFECT_OCTAVE.to_int() == 12


def test_interval_from_int():
    assert interval_from_int(0) == PERFECT_UNISON
    assert interval_from_int(1) == MINOR_SECOND
    assert interval_from_int(2) == MAJOR_SECOND
    assert interval_from_int(3) == MINOR_THIRD
    assert interval_from_int(4) == MAJOR_THIRD
    assert interval_from_int(5) == PERFECT_FOURTH
    assert interval_from_int(6) == TRITONE
    assert interval_from_int(7) == PERFECT_FIFTH
    assert interval_from_int(8) == MINOR_SIXTH
    assert interval_from_int(9) == MAJOR_SIXTH
    assert interval_from_int(10) == MINOR_SEVENTH
    assert interval_from_int(11) == MAJOR_SEVENTH
    assert interval_from_int(12) == PERFECT_OCTAVE
    assert interval_from_int(13) == MINOR_SECOND
    assert interval_from_int(14) == MAJOR_SECOND
    assert interval_from_int(15) == MINOR_THIRD
    assert interval_from_int(16) == MAJOR_THIRD
    assert interval_from_int(17) == PERFECT_FOURTH
    assert interval_from_int(18) == TRITONE
    assert interval_from_int(19) == PERFECT_FIFTH
    assert interval_from_int(20) == MINOR_SIXTH
    assert interval_from_int(21) == MAJOR_SIXTH
    assert interval_from_int(22) == MINOR_SEVENTH
    assert interval_from_int(23) == MAJOR_SEVENTH
    assert interval_from_int(24) == PERFECT_OCTAVE


def test_interval_from_str():
    assert interval_from_str("U") == PERFECT_UNISON
    assert interval_from_str("m2") == MINOR_SECOND
    assert interval_from_str("M2") == MAJOR_SECOND
    assert interval_from_str("m3") == MINOR_THIRD
    assert interval_from_str("M3") == MAJOR_THIRD
    assert interval_from_str("P4") == PERFECT_FOURTH
    assert interval_from_str("T") == TRITONE
    assert interval_from_str("P5") == PERFECT_FIFTH
    assert interval_from_str("m6") == MINOR_SIXTH
    assert interval_from_str("M6") == MAJOR_SIXTH
    assert interval_from_str("m7") == MINOR_SEVENTH
    assert interval_from_str("M7") == MAJOR_SEVENTH
    assert interval_from_str("O") == PERFECT_OCTAVE
