from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from functools import cached_property
from typing import List
from uuid import UUID, uuid4

from poker2.card import Card
from .enums import Game, GameType, Limit, Action
from .hand import Combo

@dataclass
class HandHistory:
    date: datetime 

    # header values
    ident: str 
    game: Game 
    game_type: GameType 
    limit: Limit 
    max_players: int 
    seats: List['Seat'] 
    sb: Decimal 
    bb: Decimal 
    button: 'Seat' 
    header_extra: 'HandHistoryHeaderExtra' 

    # streets
    preflop: Optional['Street'] = field(default=None)
    flop: Optional['Street'] = field(default=None)
    turn: Optional['Street'] = field(default=None)
    river: Optional['Street'] = field(default=None)
    showdown: Optional['Street'] = field(default=None)

    @property
    def sbplayer(self):
        is_headsup = len(self.seats)==2
        if is_headsup:
            return self.button
        else:
            return self.seats[self.button_index+1 % self.nplayers]

    @property
    def button_index(self):
        return self.seats.index(self.button)

    @property
    def nplayers(self):
        return len(self.seats)


@dataclass
class Street:
    actions: List['PlayerAction']
    cards: List[Card]


@dataclass
class PlayerAction:
    player: 'Player'
    action: Action
    amount: Optional[Decimal]


@dataclass
class Seat:
    seatno: int
    stack: Decimal
    combo: Optional[Combo]  # None if the combo is not revealed by the end of the hand
    player: 'Player'


class HandHistoryHeaderExtra:
    def __init__(self):
        pass


#  TODO make player class unique up to uuid's, better uuid system
class Player:
    """
    Po
    """
    _instances = {}

    def __new__(cls: type['Self'], name: str, uuid=None) -> 'Self':
        if uuid is None:
            uuid = uuid4()
        key = uuid
        if key not in cls._instances:
            instance = super().__new__(cls)
            instance.uuid = uuid
            instance.name = name
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, name: str, uuid: Optional[UUID]) -> None:
        self.name = self.name
        self.uuid = self.uuid

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.uuid == other.uuid
    
