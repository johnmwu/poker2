from enum import Enum

Game = Enum('Game', ['HOLDEM', 'OMAHA'])
GameType = Enum('GameType', ['TOURNAMENT', 'CASH', 'SNG'])
Limit = Enum('Limit', ['NL', 'PL', 'FL'])

class Action(Enum):
    BET = 0
    RAISE = 1
    CHECK = 2
    FOLD = 3
    CALL = 4
    POSTBLIND = 5
    SHOW = 6
    COLLECT = 7
