import pytest
import pytz
from datetime import datetime
from decimal import Decimal
from poker2.card import Card, Rank, Suit


from poker2.handhistory import HandHistoryHeaderExtra, PlayerAction, Seat, Street
from poker2.parsers import parse_pokernow, parse_pokernow_header
from poker2.enums import Action, Game, GameType, Limit
from poker2.examples import MICHAEL, BRIAN

POKERNOW_HAND1 = r'''
"-- ending hand #7 --",2023-01-14T21:51:55.296Z,167373311529604
"""brian @ Tf95qWPA1J"" collected 1160 from pot with Full House, Q's over 10's (combination: Q♥, Q♦, Q♠, 10♦, 10♣)",2023-01-14T21:51:55.296Z,167373311529603
"""brian @ Tf95qWPA1J"" shows a Q♥, 7♥.",2023-01-14T21:51:55.296Z,167373311529602
"""michael @ VEYRadLj9o"" collected 1160 from pot with Full House, Q's over 10's (combination: Q♣, Q♦, Q♠, 10♦, 10♣)",2023-01-14T21:51:55.296Z,167373311529601
"""michael @ VEYRadLj9o"" shows a Q♣, 8♥.",2023-01-14T21:51:55.296Z,167373311529600
"""michael @ VEYRadLj9o"" calls 1000",2023-01-14T21:51:54.490Z,167373311449000
"""brian @ Tf95qWPA1J"" raises to 1000",2023-01-14T21:51:43.559Z,167373310355900
"""michael @ VEYRadLj9o"" bets 400",2023-01-14T21:51:16.959Z,167373307695900
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:50:52.244Z,167373305224400
"River: Q♦, 10♦, 10♣, 2♥ [Q♠]",2023-01-14T21:50:48.194Z,167373304819400
"""brian @ Tf95qWPA1J"" calls 80",2023-01-14T21:50:47.346Z,167373304734600
"""michael @ VEYRadLj9o"" bets 80",2023-01-14T21:50:41.437Z,167373304143700
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:50:18.768Z,167373301876800
"Turn: Q♦, 10♦, 10♣ [2♥]",2023-01-14T21:50:16.567Z,167373301656700
"""brian @ Tf95qWPA1J"" calls 30",2023-01-14T21:50:15.724Z,167373301572400
"""michael @ VEYRadLj9o"" bets 30",2023-01-14T21:50:13.388Z,167373301338800
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:49:58.480Z,167373299848000
"Flop:  [Q♦, 10♦, 10♣]",2023-01-14T21:49:53.833Z,167373299383300
"""brian @ Tf95qWPA1J"" calls 50",2023-01-14T21:49:53.031Z,167373299303100
"""michael @ VEYRadLj9o"" raises to 50",2023-01-14T21:49:51.140Z,167373299114000
"""brian @ Tf95qWPA1J"" posts a big blind of 20",2023-01-14T21:49:44.596Z,167373298459605
"""michael @ VEYRadLj9o"" posts a small blind of 10",2023-01-14T21:49:44.596Z,167373298459604
"Your hand is Q♣, 8♥",2023-01-14T21:49:44.596Z,167373298459602
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2040) | #6 ""brian @ Tf95qWPA1J"" (1960)",2023-01-14T21:49:44.596Z,167373298459601
"-- starting hand #7 (id: tooolqqevl05)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:49:44.596Z,167373298459600
'''

POKERNOW_HAND2 = r'''
"-- ending hand #6 --",2023-01-14T21:49:41.625Z,167373298162502
"""brian @ Tf95qWPA1J"" collected 40 from pot",2023-01-14T21:49:41.625Z,167373298162501
"Uncalled bet of 30 returned to ""brian @ Tf95qWPA1J""",2023-01-14T21:49:41.625Z,167373298162500
"""michael @ VEYRadLj9o"" folds",2023-01-14T21:49:40.789Z,167373298078900
"""brian @ Tf95qWPA1J"" raises to 50",2023-01-14T21:49:19.883Z,167373295988300
"""michael @ VEYRadLj9o"" posts a big blind of 20",2023-01-14T21:49:17.676Z,167373295767605
"""brian @ Tf95qWPA1J"" posts a small blind of 10",2023-01-14T21:49:17.676Z,167373295767604
"Your hand is 8♦, J♦",2023-01-14T21:49:17.676Z,167373295767602
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2060) | #6 ""brian @ Tf95qWPA1J"" (1940)",2023-01-14T21:49:17.676Z,167373295767601
"-- starting hand #6 (id: imlmnm907ut5)  (No Limit Texas Hold'em) (dealer: ""brian @ Tf95qWPA1J"") --",2023-01-14T21:49:17.676Z,167373295767600
'''

UTC = pytz.timezone('UTC')

@pytest.fixture
def hand_header(request):
    """Parse hand history header only defined in hand_text
    and returns a PokerNowHandHistory instance.
    """
    playermap = {'michael': MICHAEL, 'brian': BRIAN}
    hh = parse_pokernow_header(request.instance.hand_text, playermap)
    return hh

@pytest.fixture
def hand(request):
    """Parse hand history defined in hand_text
    and returns a PokerNowHandHistory instance.
    """
    playermap = {'michael': MICHAEL, 'brian': BRIAN}
    hh = parse_pokernow(request.instance.hand_text, playermap)
    return hh


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