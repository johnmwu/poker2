from .handhistory import Player
from uuid import UUID

MICHAEL = Player(name='michael', uuid=UUID(int=0))
BRIAN = Player(name='brian', uuid=UUID(int=1))
PLAYERMAP1 = {'michael': MICHAEL, 'brian': BRIAN, 'hero': MICHAEL}

POKERNOW_SESSION1 = r'''
entry,at,order
"""michael @ VEYRadLj9o"" posts a big blind of 20",2023-01-14T21:52:01.301Z,167373312130105
"""brian @ Tf95qWPA1J"" posts a small blind of 10",2023-01-14T21:52:01.301Z,167373312130104
"Your hand is 7♣, 7♦",2023-01-14T21:52:01.301Z,167373312130102
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2040) | #6 ""brian @ Tf95qWPA1J"" (1960)",2023-01-14T21:52:01.301Z,167373312130101
"-- starting hand #8 (id: t6grg9zkzrwn)  (No Limit Texas Hold'em) (dealer: ""brian @ Tf95qWPA1J"") --",2023-01-14T21:52:01.301Z,167373312130100
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
"-- ending hand #5 --",2023-01-14T21:49:14.767Z,167373295476702
"""michael @ VEYRadLj9o"" collected 100 from pot",2023-01-14T21:49:14.767Z,167373295476701
"Uncalled bet of 50 returned to ""michael @ VEYRadLj9o""",2023-01-14T21:49:14.767Z,167373295476700
"""brian @ Tf95qWPA1J"" folds",2023-01-14T21:49:13.884Z,167373295388400
"""michael @ VEYRadLj9o"" bets 50",2023-01-14T21:49:04.351Z,167373294435100
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:48:50.998Z,167373293099800
"Flop:  [4♣, 8♠, Q♥]",2023-01-14T21:48:48.937Z,167373292893700
"""brian @ Tf95qWPA1J"" calls 50",2023-01-14T21:48:48.090Z,167373292809000
"""michael @ VEYRadLj9o"" raises to 50",2023-01-14T21:48:46.725Z,167373292672500
"""brian @ Tf95qWPA1J"" posts a big blind of 20",2023-01-14T21:48:43.237Z,167373292323705
"""michael @ VEYRadLj9o"" posts a small blind of 10",2023-01-14T21:48:43.237Z,167373292323704
"Your hand is A♦, 2♦",2023-01-14T21:48:43.237Z,167373292323702
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2010) | #6 ""brian @ Tf95qWPA1J"" (1990)",2023-01-14T21:48:43.237Z,167373292323701
"-- starting hand #5 (id: hmoy1d3ra6jk)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:48:43.237Z,167373292323700
"-- ending hand #4 --",2023-01-14T21:48:40.332Z,167373292033202
"""michael @ VEYRadLj9o"" collected 20 from pot",2023-01-14T21:48:40.332Z,167373292033201
"Uncalled bet of 10 returned to ""michael @ VEYRadLj9o""",2023-01-14T21:48:40.332Z,167373292033200
"""brian @ Tf95qWPA1J"" folds",2023-01-14T21:48:39.519Z,167373291951900
"""michael @ VEYRadLj9o"" posts a big blind of 20",2023-01-14T21:48:33.727Z,167373291372705
"""brian @ Tf95qWPA1J"" posts a small blind of 10",2023-01-14T21:48:33.727Z,167373291372704
"Your hand is 5♣, 6♦",2023-01-14T21:48:33.727Z,167373291372702
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2000) | #6 ""brian @ Tf95qWPA1J"" (2000)",2023-01-14T21:48:33.727Z,167373291372701
"-- starting hand #4 (id: zvgml5dacb2r)  (No Limit Texas Hold'em) (dealer: ""brian @ Tf95qWPA1J"") --",2023-01-14T21:48:33.727Z,167373291372700
"-- ending hand #3 --",2023-01-14T21:48:30.723Z,167373291072302
"""michael @ VEYRadLj9o"" collected 40 from pot",2023-01-14T21:48:30.723Z,167373291072301
"Uncalled bet of 30 returned to ""michael @ VEYRadLj9o""",2023-01-14T21:48:30.723Z,167373291072300
"""brian @ Tf95qWPA1J"" folds",2023-01-14T21:48:29.857Z,167373290985700
"""michael @ VEYRadLj9o"" raises to 50",2023-01-14T21:48:27.781Z,167373290778100
"""brian @ Tf95qWPA1J"" posts a big blind of 20",2023-01-14T21:48:21.544Z,167373290154405
"""michael @ VEYRadLj9o"" posts a small blind of 10",2023-01-14T21:48:21.544Z,167373290154404
"Your hand is 8♥, 10♣",2023-01-14T21:48:21.544Z,167373290154402
"Player stacks: #1 ""michael @ VEYRadLj9o"" (1980) | #6 ""brian @ Tf95qWPA1J"" (2020)",2023-01-14T21:48:21.544Z,167373290154401
"-- starting hand #3 (id: 5tjfqd8relt4)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:48:21.544Z,167373290154400
"-- ending hand #2 --",2023-01-14T21:48:18.615Z,167373289861502
"""brian @ Tf95qWPA1J"" collected 140 from pot",2023-01-14T21:48:18.615Z,167373289861501
"Uncalled bet of 60 returned to ""brian @ Tf95qWPA1J""",2023-01-14T21:48:18.615Z,167373289861500
"""michael @ VEYRadLj9o"" folds",2023-01-14T21:48:17.809Z,167373289780900
"""brian @ Tf95qWPA1J"" bets 60",2023-01-14T21:48:13.156Z,167373289315600
"""michael @ VEYRadLj9o"" checks",2023-01-14T21:48:09.044Z,167373288904400
"Turn: 2♥, 7♥, 7♣ [2♣]",2023-01-14T21:48:06.597Z,167373288659700
"""michael @ VEYRadLj9o"" calls 20",2023-01-14T21:48:05.732Z,167373288573200
"""brian @ Tf95qWPA1J"" bets 20",2023-01-14T21:48:00.690Z,167373288069000
"""michael @ VEYRadLj9o"" checks",2023-01-14T21:47:53.267Z,167373287326700
"Flop:  [2♥, 7♥, 7♣]",2023-01-14T21:47:48.993Z,167373286899300
"""michael @ VEYRadLj9o"" calls 50",2023-01-14T21:47:48.139Z,167373286813900
"""brian @ Tf95qWPA1J"" raises to 50",2023-01-14T21:47:45.231Z,167373286523100
"""michael @ VEYRadLj9o"" posts a big blind of 20",2023-01-14T21:47:36.487Z,167373285648705
"""brian @ Tf95qWPA1J"" posts a small blind of 10",2023-01-14T21:47:36.487Z,167373285648704
"Your hand is Q♦, 9♦",2023-01-14T21:47:36.487Z,167373285648702
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2050) | #6 ""brian @ Tf95qWPA1J"" (1950)",2023-01-14T21:47:36.487Z,167373285648701
"-- starting hand #2 (id: c0xs7qm03sip)  (No Limit Texas Hold'em) (dealer: ""brian @ Tf95qWPA1J"") --",2023-01-14T21:47:36.487Z,167373285648700
"-- ending hand #1 --",2023-01-14T21:47:33.581Z,167373285358102
"""michael @ VEYRadLj9o"" collected 100 from pot",2023-01-14T21:47:33.581Z,167373285358101
"Uncalled bet of 50 returned to ""michael @ VEYRadLj9o""",2023-01-14T21:47:33.581Z,167373285358100
"""brian @ Tf95qWPA1J"" folds",2023-01-14T21:47:32.753Z,167373285275300
"""michael @ VEYRadLj9o"" bets 50",2023-01-14T21:47:31.548Z,167373285154800
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:47:25.545Z,167373284554500
"Flop:  [2♠, 7♠, 6♠]",2023-01-14T21:47:18.015Z,167373283801500
"""brian @ Tf95qWPA1J"" calls 50",2023-01-14T21:47:17.205Z,167373283720500
"""michael @ VEYRadLj9o"" raises to 50",2023-01-14T21:47:14.793Z,167373283479300
"""brian @ Tf95qWPA1J"" posts a big blind of 20",2023-01-14T21:47:08.939Z,167373282893907
"""michael @ VEYRadLj9o"" posts a small blind of 10",2023-01-14T21:47:08.939Z,167373282893906
"Your hand is 7♥, 6♥",2023-01-14T21:47:08.939Z,167373282893904
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2000) | #6 ""brian @ Tf95qWPA1J"" (2000)",2023-01-14T21:47:08.939Z,167373282893903
"The player ""brian @ Tf95qWPA1J"" joined the game with a stack of 2000.",2023-01-14T21:47:08.939Z,167373282893902
"The player ""michael @ VEYRadLj9o"" joined the game with a stack of 2000.",2023-01-14T21:47:08.939Z,167373282893901
"-- starting hand #1 (id: ufhrgt2tkrb6)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:47:08.939Z,167373282893900
"The admin approved the player ""brian @ Tf95qWPA1J"" participation with a stack of 2000.",2023-01-14T21:47:05.329Z,167373282532900
"The player ""brian @ Tf95qWPA1J"" requested a seat.",2023-01-14T21:46:59.180Z,167373281918000
"The admin approved the player ""michael @ VEYRadLj9o"" participation with a stack of 2000.",2023-01-14T21:46:09.345Z,167373276934501
"The player ""michael @ VEYRadLj9o"" requested a seat.",2023-01-14T21:46:09.345Z,167373276934500
'''

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

POKERNOW_HAND3 = r'''
"-- ending hand #1 --",2023-01-14T21:47:33.581Z,167373285358102
"""michael @ VEYRadLj9o"" collected 100 from pot",2023-01-14T21:47:33.581Z,167373285358101
"Uncalled bet of 50 returned to ""michael @ VEYRadLj9o""",2023-01-14T21:47:33.581Z,167373285358100
"""brian @ Tf95qWPA1J"" folds",2023-01-14T21:47:32.753Z,167373285275300
"""michael @ VEYRadLj9o"" bets 50",2023-01-14T21:47:31.548Z,167373285154800
"""brian @ Tf95qWPA1J"" checks",2023-01-14T21:47:25.545Z,167373284554500
"Flop:  [2♠, 7♠, 6♠]",2023-01-14T21:47:18.015Z,167373283801500
"""brian @ Tf95qWPA1J"" calls 50",2023-01-14T21:47:17.205Z,167373283720500
"""michael @ VEYRadLj9o"" raises to 50",2023-01-14T21:47:14.793Z,167373283479300
"""brian @ Tf95qWPA1J"" posts a big blind of 20",2023-01-14T21:47:08.939Z,167373282893907
"""michael @ VEYRadLj9o"" posts a small blind of 10",2023-01-14T21:47:08.939Z,167373282893906
"Your hand is 7♥, 6♥",2023-01-14T21:47:08.939Z,167373282893904
"Player stacks: #1 ""michael @ VEYRadLj9o"" (2000) | #6 ""brian @ Tf95qWPA1J"" (2000)",2023-01-14T21:47:08.939Z,167373282893903
"The player ""brian @ Tf95qWPA1J"" joined the game with a stack of 2000.",2023-01-14T21:47:08.939Z,167373282893902
"The player ""michael @ VEYRadLj9o"" joined the game with a stack of 2000.",2023-01-14T21:47:08.939Z,167373282893901
"-- starting hand #1 (id: ufhrgt2tkrb6)  (No Limit Texas Hold'em) (dealer: ""michael @ VEYRadLj9o"") --",2023-01-14T21:47:08.939Z,167373282893900
'''
