from chords.types.letter import A, B, C, D, E, F, G

def test_letter_names():
    assert A.name == "A"
    assert B.name == "B"
    assert C.name == "C"
    assert D.name == "D"
    assert E.name == "E"
    assert F.name == "F"
    assert G.name == "G"

def test_letter_to_number():
    assert A.value == 0
    assert B.value == 2
    assert C.value == 3
    assert D.value == 5
    assert E.value == 7
    assert F.value == 8
    assert G.value == 10


