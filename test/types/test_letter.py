from chords.types.letter import letter_from_str, letter_from_int, A, B, C, D, E, F, G


def test_letter_to_str():
    assert A.to_str() == "A"
    assert B.to_str() == "B"
    assert C.to_str() == "C"
    assert D.to_str() == "D"
    assert E.to_str() == "E"
    assert F.to_str() == "F"
    assert G.to_str() == "G"


def test_letter_to_int():
    assert A.to_int() == 0
    assert B.to_int() == 2
    assert C.to_int() == 3
    assert D.to_int() == 5
    assert E.to_int() == 7
    assert F.to_int() == 8
    assert G.to_int() == 10


def test_from_str():
    assert letter_from_str("A") == A
    assert letter_from_str("B") == B
    assert letter_from_str("C") == C
    assert letter_from_str("D") == D
    assert letter_from_str("E") == E
    assert letter_from_str("F") == F
    assert letter_from_str("G") == G


def test_from_int():
    assert letter_from_int(0) == A
    assert letter_from_int(2) == B
    assert letter_from_int(3) == C
    assert letter_from_int(5) == D
    assert letter_from_int(7) == E
    assert letter_from_int(8) == F
    assert letter_from_int(10) == G