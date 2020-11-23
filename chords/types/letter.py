from enum import Enum, unique

STR_LETTERS = "A_BC_D_EF_G_"

@unique
class Letter(Enum):
    A = 0
    B = 2
    C = 3
    D = 5
    E = 7
    F = 8
    G = 10

    def __repr__(self: "Letter"):
        return f"<Letter: {self.name}>"

    @classmethod
    def from_letter(cls, letter: str) -> "Letter":
        return Letter(STR_LETTERS.index(letter))


A = Letter.A
B = Letter.B
C = Letter.C
D = Letter.D
E = Letter.E
F = Letter.F
G = Letter.G

