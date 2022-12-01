from enum import Enum

class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


print(Suit.__dict__)

Suit.Heart.value = 'H'