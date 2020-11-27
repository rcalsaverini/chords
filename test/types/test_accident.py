from chords.types.accident import (
    accident_from_int,
    accident_from_str,
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
    assert accident_from_str("𝄫") == DOUBLE_FLAT
    assert accident_from_str("♭") == FLAT
    assert accident_from_str("b") == FLAT
    assert accident_from_str("♮") == NATURAL
    assert accident_from_str("♯") == SHARP
    assert accident_from_str("#") == SHARP
    assert accident_from_str("𝄪") == DOUBLE_SHARP


def test_from_int():
    assert accident_from_int(-2) == DOUBLE_FLAT
    assert accident_from_int(-1) == FLAT
    assert accident_from_int(0) == NATURAL
    assert accident_from_int(1) == SHARP
    assert accident_from_int(2) == DOUBLE_SHARP
