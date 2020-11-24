from chords.types.accident import (
    Accident,
    DOUBLE_FLAT,
    FLAT,
    NATURAL,
    SHARP,
    DOUBLE_SHARP,
)


def test_accident_symbols():
    assert DOUBLE_FLAT.symbol == "𝄫"
    assert FLAT.symbol == "♭"
    assert NATURAL.symbol == "♮"
    assert SHARP.symbol == "♯"
    assert DOUBLE_SHARP.symbol == "𝄪"


def test_accident_to_str():
    assert DOUBLE_FLAT.to_str() == "𝄫"
    assert FLAT.to_str() == "♭"
    assert NATURAL.to_str() == "♮"
    assert SHARP.to_str() == "♯"
    assert DOUBLE_SHARP.to_str() == "𝄪"


def test_accident_to_int():
    assert DOUBLE_FLAT.to_int() == -2
    assert FLAT.to_int() == -1
    assert NATURAL.to_int() == 0
    assert SHARP.to_int() == 1
    assert DOUBLE_SHARP.to_int() == 2


def test_from_str():
    assert Accident.from_str("𝄫") == DOUBLE_FLAT
    assert Accident.from_str("♭") == FLAT
    assert Accident.from_str("b") == FLAT
    assert Accident.from_str("♮") == NATURAL
    assert Accident.from_str("♯") == SHARP
    assert Accident.from_str("#") == SHARP
    assert Accident.from_str("𝄪") == DOUBLE_SHARP


def test_from_int():
    assert Accident.from_int(-2) == DOUBLE_FLAT
    assert Accident.from_int(-1) == FLAT
    assert Accident.from_int(0) == NATURAL
    assert Accident.from_int(1) == SHARP
    assert Accident.from_int(2) == DOUBLE_SHARP
