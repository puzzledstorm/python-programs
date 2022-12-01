"""
In Python, there are two common approaches to factories, as follows:

We define a function that creates objects of the required classes.

We define a class that has methods for creating objects. This is the Factory
design pattern, as described in books on object-oriented design patterns. In
languages such as Java, a factory class hierarchy is required because the
language doesn't support standalone functions.

In Python, a class isn't required to create an object factory, but this can be a good
idea when there are related factories or factories that are complex. One of the
strengths of Python is that we're not forced to use a class hierarchy when a
simple function might do just as well
"""


# from https://github.com/PacktPublishing/Mastering-Object-Oriented-Python-Second-Edition/blob/master/Chapter_2/ch02_ex2.py
# ---------------------------------------------

from typing import Tuple, Any, Union, cast

class Card:
    insure = False

    def __init__(self, rank: str, suit: Any) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def __eq__(self, other: Any) -> bool:
        return (
            self.suit == cast("Card", other).suit
            and self.rank == cast("Card", other).rank
            and self.hard == cast("Card", other).hard
            and self.soft == cast("Card", other).soft
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(suit={self.suit!r}, rank={self.rank!r})"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)


class AceCard(Card):
    insure = True

    def _points(self) -> Tuple[int, int]:
        return 1, 11


class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10

from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"

# -------------------------------------------
from typing import cast, Iterable, Iterator

# 1.factory function
def card(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")

deck = [
    card(rank, suit) for rank in range(1, 14) for suit in cast(Iterable[Suit], Suit)
]
deck_l = [
    card(rank, suit) for rank in range(1, 14) for suit in iter(Suit)
]

deck_l = [
    card(rank, suit) for rank in range(1, 14) for suit in list(Suit)
]


deck_l = [
    card(rank, suit) for rank in range(1, 14) for suit in Suit
] # mypy没有报错signal errors啊

# print(deck)
# print(deck_l)


# It's important to avoid a vague else clause.

# 使用不明确的else示例
def card2(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    else:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
deck2 = [card2(rank, suit) for rank in range(13) for suit in Suit]


# Factory design patterns:
# An if-elif sequence
# A mapping
