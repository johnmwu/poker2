import re
import logging
from datetime import datetime
import pytz
from typing import List
from decimal import Decimal
from typing import Dict
from pprint import pprint

from poker2.card import Card, Rank, Suit
from poker2.enums import Action, GameType, Game, Limit
from poker2.hand import Combo
from poker2.handhistory import HandHistory, HandHistoryHeaderExtra, Player, PlayerAction, PokerSession, Seat, Street

module_logger = logging.getLogger(__name__)
UTC = pytz.timezone('UTC')



_start_hand_re = re.compile(r'''\"-- starting hand \#(?P<handnum>\d+) \(id: (?P<handid>[a-z0-9]+)\)  \((?P<gametype>.*?)\) \(dealer: \"\"(?P<buttonplayer>\w*?) @ (?P<buttonseatname>\w*?)\"\"\) --\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_stack_size_re = re.compile(r'''\"Player stacks:(?P<players>(( \|)? \#(\d+) \"\"(?P<playername>.*?)\"\" \((?P<stacksize>\d+)\))+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_post_sb_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" posts a small blind of (?P<sbamt>\d+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_post_bb_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" posts a big blind of (?P<bbamt>\d+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_flop_re = re.compile(r'''\"Flop:  \[(?P<card1>\w+.), (?P<card2>\w+.), (?P<card3>\w+.)\]\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_turn_re = re.compile(r'''\"Turn:\s+(?P<card1>\w+.), (?P<card2>\w+.), (?P<card3>\w+.) \[(?P<card4>\w+.)\]\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_river_re = re.compile(r'''\"River:\s+(?P<card1>\w+.), (?P<card2>\w+.), (?P<card3>\w+.), (?P<card4>\w+.) \[(?P<card5>\w+.)\]\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_shows_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" shows a (?P<card1>\w+.), (?P<card2>\w+.)\.\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_collects_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" collected (?P<collectamt>\d+) from pot with (?P<handdescr>.*?)\(combination: (?P<card1>\w+.), (?P<card2>\w+.), (?P<card3>\w+.), (?P<card4>\w+.), (?P<card5>\w+.)\)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_returned_re = re.compile(r'''\"Uncalled bet of (?P<uncalledamt>\d+) returned to \"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\"\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_raise_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" raises to (?P<raiseamt>\d+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_call_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" calls (?P<callamt>\d+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_check_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" checks\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_bet_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" bets (?P<betamt>\d+)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_joins_re = re.compile(r'''\"The player \"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" joined the game with a stack of (?P<stacksize>\d+)\.\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_ending_hand_re = re.compile(r'''\"-- ending hand \#(?P<handno>\d+) --\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_folds_re = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" folds\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_returned_re = re.compile(r'''\"Uncalled bet of (?P<returnamt>\d+) returned to \"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\"\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_collects_re2 = re.compile(r'''\"\"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" collected (?P<collectamt>\d+) from pot\",(?P<handutc>.*?),(?P<handseqno>.*$)''')
_your_cards_re = re.compile(r'''\"Your hand is (?P<card1>\w+.), (?P<card2>\w+.)\",(?P<handutc>.*?),(?P<handseqno>.*$)''')

# not corresponding to a line
_player_re = re.compile(r'''(?P<players>( \|)? \#(?P<seatno>\d+) \"\"(?P<playername>\w*?) @ (?P<playerseatname>\w*?)\"\" \((?P<stacksize>\d+)\))''') 

def parse_pokernow_logfile(text: str, playermap: Dict[str, Player]) -> PokerSession:
    session_hands: List[HandHistory] = []

    text = text.strip()
    lines = list(reversed(text.split('\n')))

    it = enumerate(lines)
    starting_hand_index = None
    starting_hand_no = None
    for index, line in it:
        if starting_hand_index is None:
            match = _start_hand_re.match(line)
            if match is not None:
                starting_hand_index = index
                _d = match.groupdict()
                starting_hand_no = int(_d['handnum'])
                continue
        else:
            match = _ending_hand_re.match(line)
            if match is not None:
                ending_hand_index = index
                _d = match.groupdict()
                ending_hand_no = int(_d['handno'])
                if ending_hand_no != starting_hand_no:
                    raise ValueError(f'Started parsing handno {starting_hand_no}, ending handno {ending_hand_no}')

                hand_lines = lines[starting_hand_index:ending_hand_index+1]
                handhistory = parse_pokernow_hand(hand_lines, playermap)
                session_hands.append(handhistory)

                starting_hand_index = None
                ending_hand_index = None

    # might be in the middle of a hand when downloading the log
    if starting_hand_index is not None:
        module_logger.info(f'Unfinished hand {starting_hand_no}')

    return PokerSession(
        hands=session_hands
    )


def parse_pokernow_hand(lines: List[str], playermap: Dict[str, Player]) -> HandHistory:
    logger = module_logger

    # text = text.strip()
    # lines = list(reversed(text.split('\n')))

    result = parse_pokernow_header(lines, playermap)

    # get indices of before_hand street
    start_before_hand_index = 1
    actions = []
    for line in lines[start_before_hand_index:]:
        match = _stack_size_re.match(line)
        if match is not None:
            break

        action = _parse_action_line(line, playermap)
        actions.append(action)

    result.before_hand = Street(
        actions=actions,
        cards=[]
    )
    

    # get indices of each of the "normal streets"
    it = enumerate(lines)
    for index, line in it:
        match = _post_sb_re.match(line)
        if match is not None:
            preflop_index = index
            break
    else:
        raise ValueError('Failed to find post_sb line')

    for index, line in it:
        match = _flop_re.match(line)
        if match is not None:
            flop_index = index
            break
    else:
        flop_index = None
        logger.info(f'Failed for find flop line for lines {lines}')

    for index, line in it:
        match = _turn_re.match(line)
        if match is not None:
            turn_index = index
            break
    else:
        turn_index = None
        logger.info(f'Failed for find turn line for lines {lines}')

    for index, line in it:
        match = _river_re.match(line)
        if match is not None:
            river_index = index
            break
    else:
        river_index = None
        logger.info(f'Failed for find river line for lines {lines}')

    for index, line in it:
        match1 = _shows_re.match(line)
        if any([match is not None for match in (match1,)]):
            showdown_index = index
            break
    else:
        showdown_index = None
        logger.info(f'Failed for find showdown line for lines {lines}')


    # preflop
    if flop_index is not None:
        preflop_lines = lines[preflop_index:flop_index]
    else:
        preflop_lines = lines[preflop_index:-1]
    
    preflop_actions = [_parse_action_line(line, playermap) for line in preflop_lines]
    preflop_cards = []
    preflop = Street(
        actions=preflop_actions,
        cards=preflop_cards
    )
    result.preflop = preflop

    # flop
    if flop_index is None:
        result.flop = None
    else:
        if turn_index is None:
            flop_lines = lines[flop_index:-1]
        else:
            flop_lines = lines[flop_index:turn_index]

        flop_cards_line = flop_lines[0]
        flop_actions_lines = flop_lines[1:]
        
        # flop cards
        flop_match = _flop_re.match(flop_cards_line)
        if flop_match is None:
            raise ValueError(f'Failed to match flop line {flop_cards_line}')
        _d = flop_match.groupdict()
        flop_cards = [_parse_card(card) for card in (_d['card1'], _d['card2'], _d['card3'])]

        # flop actions
        flop_actions = [_parse_action_line(line, playermap) for line in flop_actions_lines]

        result.flop = Street(flop_actions, flop_cards)

    # turn
    if turn_index is None:
        result.turn = None
    else:
        if river_index is None:
            turn_lines = lines[turn_index:-1]
        else:
            turn_lines = lines[turn_index:river_index]

        turn_cards_line = turn_lines[0]
        turn_actions_lines = turn_lines[1:]
        
        # turn cards
        turn_match = _turn_re.match(turn_cards_line)
        if turn_match is None:
            raise ValueError(f'Failed to match turn line {turn_cards_line}')
        _d = turn_match.groupdict()
        turn_cards = [_parse_card(card) for card in (_d['card4'],)]

        # turn actions
        turn_actions = [_parse_action_line(line, playermap) for line in turn_actions_lines]

        result.turn = Street(turn_actions, turn_cards)

    # river
    if river_index is None:
        result.river = None
    else:
        if showdown_index is None:
            river_lines = lines[river_index:-1]
        else:
            river_lines = lines[river_index:showdown_index]

        river_cards_line = river_lines[0]
        river_actions_lines = river_lines[1:]
        
        # river cards
        river_match = _river_re.match(river_cards_line)
        if river_match is None:
            raise ValueError(f'Failed to match river line {river_cards_line}')
        _d = river_match.groupdict()
        river_cards = [_parse_card(card) for card in (_d['card5'],)]

        # river actions
        river_actions = [_parse_action_line(line, playermap) for line in river_actions_lines]

        result.river = Street(river_actions, river_cards)

    # showdown
    if showdown_index is None:
        result.showdown = None
    else:
        showdown_lines = lines[showdown_index:-1]

        showdown_actions_lines = showdown_lines
        showdown_actions = [_parse_action_line(line, playermap) for line in showdown_actions_lines]
        result.showdown = Street(showdown_actions, [])

    # populate all seats with proper showdown cards
    for line in lines:
        match = _shows_re.match(line)
        if match is not None:
            _d = match.groupdict()
            player = playermap[_d['playername']]
            seat = next(seat for seat in result.seats if seat.player==player)
            card1 = _parse_card(_d['card1'])
            card2 = _parse_card(_d['card2'])
            seat.combo = Combo(card1, card2)

    # populate hero seat with proper cards
    for line in lines:
        match = _your_cards_re.match(line)
        if match is not None:
            _d = match.groupdict()
            player = playermap['hero']
            seat = next(seat for seat in result.seats if seat.player==player)
            card1 = _parse_card(_d['card1'])
            card2 = _parse_card(_d['card2'])
            seat.combo = Combo(card1, card2)    
            break       

    return result


def parse_pokernow_header(lines: List[str], playermap: Dict[str, Player]) -> HandHistory:
    logger = module_logger

    # text = text.strip()
    # lines = list(reversed(text.split('\n')))


    # begin parsing
    max_players = 9  # TODO is this true?
    game_type = GameType.CASH

    # start hand line
    # example: "-- starting hand #7 (id: tooolqqevl05)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:49:44.596Z,167373298459600
    match_start_hand = _start_hand_re.match(lines[0])
    if match_start_hand is not None:
        start_hand_d = match_start_hand.groupdict()
    else:
        raise ValueError(f'Failed to match start hand line {lines[0]}')

    ident = start_hand_d['handid']
    handutcstr = start_hand_d['handutc']
    handutcfmt = "%Y-%m-%dT%H:%M:%S.%fZ"
    date = UTC.localize(datetime.strptime(handutcstr, handutcfmt))

    game = _parse_pokernow_gametype(start_hand_d['gametype'])
    limit = _parse_pokernow_limit(start_hand_d['gametype'])
    buttonplayername = start_hand_d['buttonplayer']

    # PLAYER STACK SIZE LINE
    for line in lines:
        match_stack_size = _stack_size_re.match(line)
        if match_stack_size is not None:
            stack_size_d = match_stack_size.groupdict()
            playersstr = stack_size_d['players']
            break
    else:
        raise ValueError('Failed to find stack size line')

    # set `seats`
    seats: List[Seat] = []
    for playermatch in re.finditer(_player_re, playersstr): 
        _d = playermatch.groupdict()
        seatno = int(_d['seatno'])
        player = playermap.get(_d['playername'], Player(name=_d['playername'], uuid=None))
        seat = Seat(
            seatno=seatno,
            stack=Decimal(_d['stacksize']),
            combo=None,
            player=player  
        )
        seats.append(seat)
    # `seats` should be sorted according to seatno
    if not all(seats[i].seatno <= seats[i+1].seatno for i in range(len(seats)-1)):
        raise ValueError(f'Parsed seats out of order: {lines[1]}')

    _l = list(filter(lambda seat: seat.player.name == buttonplayername, seats))
    if len(_l) != 1:
        raise Exception() # TODO
    button = _l[0]

    # SB, BB
    for line in lines:
        match = _post_sb_re.match(line)
        if match:
            _d = match.groupdict()
            sb = Decimal(int(_d['sbamt']))
            break
    else:
        raise ValueError('Failed to locate small blind line')

    for line in lines:
        match = _post_bb_re.match(line)
        if match:
            _d = match.groupdict()
            bb = Decimal(int(_d['bbamt']))
            break
    else:
        raise ValueError('Failed to locate big blind line')

    return HandHistory(
        date=date,
        ident=ident,
        game=game,
        game_type=game_type,
        limit=limit,
        max_players=max_players,
        seats=seats,
        sb=sb,
        bb=bb,
        button=button,
        header_extra=HandHistoryHeaderExtra(),
    )


def _parse_card(cardstr: str) -> Card:
    rankstr = cardstr[:-1]
    suitstr = cardstr[-1]

    rankmap = {
        '2': Rank.TWO,
        '3': Rank.THREE,
        '4': Rank.FOUR,
        '5': Rank.FIVE,
        '6': Rank.SIX,
        '7': Rank.SEVEN,
        '8': Rank.EIGHT,
        '9': Rank.NINE,
        '10': Rank.TEN,
        'J': Rank.JACK,
        'Q': Rank.QUEEN,
        'K': Rank.KING,
        'A': Rank.ACE,
    }
    suitmap = {
        '♣': Suit.CLUBS,
        '♦': Suit.DIAMONDS,
        '♥': Suit.HEARTS,
        '♠': Suit.SPADES,
    }
    return Card(rank=rankmap[rankstr], suit=suitmap[suitstr])


def _parse_action_line(line: str, playermap: Dict[str, Player]) -> PlayerAction:
    match_joins = _joins_re.match(line)
    if match_joins is not None:
        _d = match_joins.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.JOIN,
            amount=Decimal(_d['stacksize'])
        )

    match_returned = _returned_re.match(line)
    if match_returned is not None:
        _d = match_returned.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.RETURNED,
            amount=Decimal(_d['returnamt'])
        )

    match_folds = _folds_re.match(line)
    if match_folds is not None:
        _d = match_folds.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.FOLD,
            amount=None,
        )

    match_sb = _post_sb_re.match(line)
    if match_sb is not None:
        _d = match_sb.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.POSTBLIND,
            amount=Decimal(_d['sbamt'])
        )
    
    match_bb = _post_bb_re.match(line)
    if match_bb is not None:
        _d = match_bb.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.POSTBLIND,
            amount=Decimal(_d['bbamt'])
        )

    match_raise = _raise_re.match(line)
    if match_raise is not None:
        _d = match_raise.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.RAISE,
            amount=Decimal(_d['raiseamt'])
        )

    match_call = _call_re.match(line)
    if match_call is not None:
        _d = match_call.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.CALL,
            amount=Decimal(_d['callamt'])
        )
   
    match_check = _check_re.match(line)
    if match_check is not None:
        _d = match_check.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.CHECK,
            amount=None,
        )

    match_bet = _bet_re.match(line)
    if match_bet is not None:
        _d = match_bet.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.BET,
            amount=Decimal(_d['betamt']),
        )
   
    match_shows = _shows_re.match(line)
    if match_shows is not None:
        _d = match_shows.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.SHOW,
            amount=None,
        )
   
    match_collects = _collects_re.match(line)
    match_collects2 = _collects_re2.match(line)
    if match_collects is not None or match_collects2 is not None:
        match = match_collects if match_collects is not None else match_collects2
        _d = match.groupdict()
        playername = _d['playername']
        player = playermap[playername]
        return PlayerAction(
            player=player,
            action=Action.COLLECT,
            amount=Decimal(_d['collectamt']),
        )
   
    raise ValueError(f'Failed to parse line {line}')

def _parse_pokernow_gametype(gametypestr: str):
    if gametypestr == "No Limit Texas Hold'em":
        return Game.HOLDEM

    raise ValueError(f'Game string {gametypestr} not recognized')

def _parse_pokernow_limit(gametypestr: str):
    if gametypestr == "No Limit Texas Hold'em":
        return Limit.NL