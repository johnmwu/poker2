import itertools
from functools import total_ordering
from enum import Enum, IntEnum
from dataclasses import dataclass
# from ._common import PokerEnum, _ReprMixin


__all__ = ["Suit", "Rank", "Card"]

class Suit(IntEnum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

BROADWAY_RANKS = [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]

@total_ordering
class Card:
    _instances = {}

    def __new__(cls, rank, suit):
        """
        Prevents the same card from being instantiated twice
        """
        key = (rank, suit)
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance.rank = rank
            instance.suit = suit
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, rank: Rank, suit: Suit):
        # rank and suit were initialized by __new__
        self.rank = self.rank
        self.suit = self.suit

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.rank == other.rank and self.suit == other.suit
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented

        # with same ranks, suit counts
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    @property
    def is_broadway(self):
        return self.rank in BROADWAY_RANKS
        

c2 = Card(Rank.ACE, Suit.DIAMONDS)

# Suit = Enum('Suit', ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES'])
