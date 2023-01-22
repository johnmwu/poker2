from enum import Enum
from .card import Card

Shape = Enum('Shape', ['OFFSUIT','SUITED', 'PAIR'])


class Combo:
    """Hand combination."""
    def __init__(
        self, 
        first: Card, 
        second: Card
    ):
        if first > second:
            self.first = first
            self.second = second
        elif second > first:
            self.first = second
            self.second = first
        else:
            raise ValueError(f'Passed {first},{second}, cannot have a combo of equal cards')

    @property
    def is_suited_connector(self):
        return self.is_suited and self.is_connector

    @property
    def is_suited(self):
        return self.first.suit == self.second.suit

    @property
    def is_offsuit(self):
        return not self.is_suited and not self.is_pair

    @property
    def is_connector(self):
        return self.rank_difference == 1

    @property
    def is_one_gapper(self):
        return self.rank_difference == 2

    @property
    def is_two_gapper(self):
        return self.rank_difference == 3

    @property
    def rank_difference(self):
        """The difference between the first and second rank of the Combo."""
        # self.first >= self.second
        return self.first.rank - self.second.rank

    @property
    def is_pair(self):
        return self.first.rank == self.second.rank

    @property
    def is_broadway(self):
        return self.first.is_broadway and self.second.is_broadway

    @property
    def shape(self):
        if self.is_pair:
            return Shape.PAIR
        elif self.is_suited:
            return Shape.SUITED
        else:
            return Shape.OFFSUIT