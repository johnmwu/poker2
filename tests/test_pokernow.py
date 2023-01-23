import pytest
import pytz
from datetime import datetime
from decimal import Decimal
from poker2.card import Card, Rank, Suit
from poker2.hand import Combo


from poker2.handhistory import HandHistoryHeaderExtra, PlayerAction, Seat, Street
from poker2.pokernow_parser import parse_pokernow_hand, parse_pokernow_header, parse_pokernow_logfile
from poker2.enums import Action, Game, GameType, Limit
from poker2.examples import MICHAEL, BRIAN, POKERNOW_HAND1, POKERNOW_HAND2, POKERNOW_HAND3, POKERNOW_SESSION1, PLAYERMAP1


UTC = pytz.timezone('UTC')

@pytest.fixture
def hand_header(request):
    """Parse hand history header only defined in hand_text
    and returns a PokerNowHandHistory instance.
    """
    lines = list(reversed(request.instance.hand_text.strip().split('\n')))
    hh = parse_pokernow_header(lines, PLAYERMAP1)
    return hh

@pytest.fixture
def hand(request):
    """Parse hand history defined in hand_text
    and returns a PokerNowHandHistory instance.
    """
    lines = list(reversed(request.instance.hand_text.strip().split('\n')))
    hh = parse_pokernow_hand(lines, PLAYERMAP1)
    return hh

@pytest.fixture
def poker_session(request):
    """Parse all hand histories in a given pokernow logfile
    """
    ps = parse_pokernow_logfile(request.instance.logfile_text, PLAYERMAP1)
    return ps


class TestSession1:
    logfile_text = POKERNOW_SESSION1

    @pytest.mark.parametrize(
        ('attribute', 'expected_value'),
        [
            ("ident", "ufhrgt2tkrb6"),
        ]
    )
    def test_first_hand(self, poker_session, attribute, expected_value):
        assert getattr(poker_session.hands[0], attribute) == expected_value


class TestHand2:
    hand_text = POKERNOW_HAND3
    @pytest.mark.parametrize(
        ("attribute", "expected_value"),
        [
            ("date", UTC.localize(datetime(2023, 1, 14, 21, 47, 8, 939000))),
            ("ident", "ufhrgt2tkrb6"),
            ("game", Game.HOLDEM),
            ("game_type", GameType.CASH),
            ("limit", Limit.NL),
            ("max_players", 9),
            ("seats", 
                [
                    Seat(
                        seatno=1,
                        stack=Decimal(2000),
                        combo=Combo(
                            first=Card(Rank.SEVEN, Suit.HEARTS),
                            second=Card(Rank.SIX, Suit.HEARTS)
                        ),
                        player=MICHAEL
                    ),
                    Seat(
                        seatno=6,
                        stack=Decimal(2000),
                        combo=None,
                        player=BRIAN
                    )
                ]
            ),
            ("sb", Decimal(10)),
            ("bb", Decimal(20)),
            (
                "button", 
                Seat(
                    seatno=1,
                    stack=Decimal(2000),
                    combo=Combo(
                            first=Card(Rank.SEVEN, Suit.HEARTS),
                            second=Card(Rank.SIX, Suit.HEARTS)
                    ),
                    player=MICHAEL
                )
            ),
            (
                'before_hand',
                Street(
                    [
                        PlayerAction(MICHAEL, Action.JOIN, Decimal(2000)),
                        PlayerAction(BRIAN, Action.JOIN, Decimal(2000)),
                    ],
                    []
                )
            ),
            (
                'preflop',
                Street(
                    [
                        PlayerAction(MICHAEL, Action.POSTBLIND, Decimal(10)),
                        PlayerAction(BRIAN, Action.POSTBLIND, Decimal(20)),
                        PlayerAction(MICHAEL, Action.RAISE, Decimal(50)),
                        PlayerAction(BRIAN, Action.CALL, Decimal(50)),
                    ],
                    []
                )
            ),
            (
                'flop',
                Street(
                    [
                        PlayerAction(BRIAN, Action.CHECK, None),
                        PlayerAction(MICHAEL, Action.BET, Decimal(50)),
                        PlayerAction(BRIAN, Action.FOLD, None),
                        PlayerAction(MICHAEL, Action.RETURNED, Decimal(50)),
                        PlayerAction(MICHAEL, Action.COLLECT, Decimal(100))
                    ],
                    [
                        Card(Rank.TWO, Suit.SPADES), 
                        Card(Rank.SEVEN, Suit.SPADES),
                        Card(Rank.SIX, Suit.SPADES)
                    ]
                )
            ),
            (
                'turn',
                None
            ),
            (
                'river',
                None
            ),
            (
                'showdown',
                None
            )
        ],
    )
    def test_values_after_parsed(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value




class TestHeader1:
    hand_text = POKERNOW_HAND1

    @pytest.mark.parametrize(
        ("attribute", "expected_value"),
        [
            ("date", UTC.localize(datetime(2023, 1, 14, 21, 49, 44, 596000))),
            ("ident", "tooolqqevl05"),
            ("game", Game.HOLDEM),
            ("game_type", GameType.CASH),
            ("limit", Limit.NL),
            ("max_players", 9),
            ("seats", 
                [
                    Seat(
                        seatno=1,
                        stack=Decimal(2040),
                        combo=None,
                        player=MICHAEL
                    ),
                    Seat(
                        seatno=6,
                        stack=Decimal(1960),
                        combo=None,
                        player=BRIAN
                    )
                ]
            ),
            ("sb", Decimal(10)),
            ("bb", Decimal(20)),
            (
                "button", 
                Seat(
                    seatno=1,
                    stack=Decimal(2040),
                    combo=None,
                    player=MICHAEL
                )
            ),
        ],
    )
    def test_values_after_header_parsed(self, hand_header, attribute, expected_value):
        assert getattr(hand_header, attribute) == expected_value


class TestHand1:
    hand_text = POKERNOW_HAND1

    @pytest.mark.parametrize(
        ("attribute", "expected_value"),
        [
            ("date", UTC.localize(datetime(2023, 1, 14, 21, 49, 44, 596000))),
            ("ident", "tooolqqevl05"),
            ("game", Game.HOLDEM),
            ("game_type", GameType.CASH),
            ("limit", Limit.NL),
            ("max_players", 9),
            ("seats", 
                [
                    Seat(
                        seatno=1,
                        stack=Decimal(2040),
                        combo=Combo(
                            first=Card(Rank.QUEEN, Suit.CLUBS),
                            second=Card(Rank.EIGHT, Suit.HEARTS)
                        ),
                        player=MICHAEL
                    ),
                    Seat(
                        seatno=6,
                        stack=Decimal(1960),
                        combo=Combo(
                            first=Card(Rank.QUEEN, Suit.HEARTS),
                            second=Card(Rank.SEVEN, Suit.HEARTS)
                        ),
                         player=BRIAN
                    )
                ]
            ),
            ("sb", Decimal(10)),
            ("bb", Decimal(20)),
            (
                "button", 
                Seat(
                    seatno=1,
                    stack=Decimal(2040),
                    combo=Combo(
                        first=Card(Rank.QUEEN, Suit.CLUBS),
                        second=Card(Rank.EIGHT, Suit.HEARTS)
                    ),
                    player=MICHAEL
                )
            ),
            (
                'preflop',
                Street(
                    [
                        PlayerAction(MICHAEL, Action.POSTBLIND, Decimal(10)),
                        PlayerAction(BRIAN, Action.POSTBLIND, Decimal(20)),
                        PlayerAction(MICHAEL, Action.RAISE, Decimal(50)),
                        PlayerAction(BRIAN, Action.CALL, Decimal(50)),
                    ],
                    []
                )
            ),
            (
                'flop',
                Street(
                    [
                        PlayerAction(BRIAN, Action.CHECK, None),
                        PlayerAction(MICHAEL, Action.BET, Decimal(30)),
                        PlayerAction(BRIAN, Action.CALL, Decimal(30)),
                    ],
                    [
                        Card(Rank.QUEEN, Suit.DIAMONDS), 
                        Card(Rank.TEN, Suit.DIAMONDS),
                        Card(Rank.TEN, Suit.CLUBS)
                    ]
                )
            ),
            (
                'turn',
                Street(
                    [
                        PlayerAction(BRIAN, Action.CHECK, None),
                        PlayerAction(MICHAEL, Action.BET, Decimal(80)),
                        PlayerAction(BRIAN, Action.CALL, Decimal(80)),
                    ],
                    [
                        Card(Rank.TWO, Suit.HEARTS)
                    ]
                )
            ),
            (
                'river',
                Street(
                    [
                        PlayerAction(BRIAN, Action.CHECK, None),
                        PlayerAction(MICHAEL, Action.BET, Decimal(400)),
                        PlayerAction(BRIAN, Action.RAISE, Decimal(1000)),
                        PlayerAction(MICHAEL, Action.CALL, Decimal(1000)),
                    ],
                    [
                        Card(Rank.QUEEN, Suit.SPADES)
                    ]
                ),
            ),
            (
                'showdown',
                Street(
                    [
                        PlayerAction(MICHAEL, Action.SHOW, None),
                        PlayerAction(MICHAEL, Action.COLLECT, Decimal(1160)),
                        PlayerAction(BRIAN, Action.SHOW, None),
                        PlayerAction(BRIAN, Action.COLLECT, Decimal(1160)),
                    ],
                    []
                )
            )
        ],
    )
    def test_values_after_parsed(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value

