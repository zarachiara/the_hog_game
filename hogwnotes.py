"""The Game of Hog"""

from dice import four_sided_dice, six_sided_dice, make_test_dice
from ucb import main, trace, log_current_line, interact

goal = 100          # The goal of Hog is to score 100 points.
commentary = True  # Whether to display commentary for every roll.


# Taking turns


def roll_dice(num_rolls, dice=six_sided_dice, who='Boss Hogg'):
    """Calculate WHO's turn score after rolling DICE for NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A function of no args and returns an integer outcome.
    who:        Name of the current player, for commentary.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    summing = 0 
    counting = 0 
    rolled_one = False
    while num_rolls > counting: 
        result = dice() 
        if commentary:
            announce(result, who)
        if result == 1: 
            rolled_one = True 
        else: 
            summing = result + summing 
        counting += 1 
    if rolled_one: 
        return 1 
    return summing 

# Write your own prime functions here!
"***YOUR CODE HERE***"
def is_prime(x): 
    k = 2 
    if x == 1: 
        return False
    while k < x: 
        if x % k == 0: 
            return False 
        k += 1 
    return True # from June 27, 2013 Discussion 

def next_prime(x): # finds the next prime 
   x = x + 1 
   while not is_prime(num): 
      x = x + 1
   return x

# End prime functions here

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Boss Hogg'):
    """Simulate a turn in which WHO chooses to roll NUM_ROLLS, perhaps 0.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args and returns an integer outcome.
    who:             Name of the current player, for commentary.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    if commentary:
        print(who, 'is going to roll', num_rolls, 'dice')
    "*** YOUR CODE HERE ***"
    turnScore = 0
    if num_rolls > 0: 
        turnScore = roll_dice(num_rolls, dice)
    else:
        turnScore = free_bacon(turnScore, opponent_score)
    turnScore = touchdown(turnScore)
    turnScore = hogitmus_prime(turnScore)
    return turnScore
    

def free_bacon(turnScore, opponent_score): 
# actually number of rolls
    if turnScore == 0: # free bacon rule
        turnScore = ((opponent_score % 100 // 10) + 1)
    return turnScore

def touchdown(turnScore):
    if turnScore % 6 == 0 != turnScore != 0: 
        turnScore = turnScore + (turnScore / 6)
    return turnScore

def hogitmus_prime(turnScore):
    if is_prime(turnScore):
        turnScore = next_prime(turnScore)
    return turnScore 

def hog_tied(turnScore,opponent_score):
    if (turnScore + opponent_score) % 10 == 7: 
        return True 
    else:
        False

def hog_wild(turnScore, opponent_score):
    if (turnScore + opponent_score) % 7 == 0 and (turnScore + opponent_score) != 0: 
        return True
    else:
        False

def all_applied(turnScore, opponent_score): 
    freebacon_score = free_bacon(turnScore, opponent_score)
    touchdown_score = touchdown(freebacon_score) 
    hogitmusprime_score = hogitmus_prime(touchdown_score)
    return hogitmusprime_score

def take_turn_test():
    """Test the roll_dice and take_turn functions using test dice."""
    print('-- Testing roll_dice --')
    dice = make_test_dice(4, 6, 1)
    assert roll_dice(2, dice) == 10, 'First two rolls total 10'

    dice = make_test_dice(4, 6, 1)
    assert roll_dice(3, dice) == 1, 'Third roll is a 1'

    dice = make_test_dice(1, 2, 3)
    assert roll_dice(3, dice) == 1, 'First roll is a 1'

    print('-- Testing take_turn --')
    dice = make_test_dice(4, 6, 1)
    assert take_turn(2, 0, dice) == 10, 'First two rolls total 10'

    dice = make_test_dice(4, 6, 1)
    assert take_turn(3, 20, dice) == 1, 'Third roll is a 1'

    print('---- Testing Free Bacon rule ----')
    assert take_turn(0, 34) == 4, 'Opponent score 10s digit is 3'
    assert take_turn(0, 71) == 8, 'Opponent score 10s digit is 7'
    assert take_turn(0,  7) == 1, 'Opponont score 10s digit is 0'

    print('---- Testing Touchdown rule ----')
    dice = make_test_dice(6)
    assert take_turn(2, 0, dice) == 14, 'Original score was 12'
    assert take_turn(3, 0, dice) == 21, 'Original score was 18'

    print('---- Testing Hogtimus Prime rule ----')
    dice = make_test_dice(5, 6, 5, 2)
    assert take_turn(0, 42, dice) == 7, 'Opponent score 10s digit is 4'
    assert take_turn(2, 0, dice) == 13, 'Original score was 11'
    assert take_turn(0, 52, dice) == 11, 'Opponent score 10s digit is 5'
    assert take_turn(2, 0, dice) == 11, 'Original score was 7'

    print('Tests for roll_dice and take_turn passed.')

    '*** You may add more tests here if you wish ***'


# Commentator

def announce(outcome, who):
    """Print a description of WHO rolling OUTCOME."""
    print(who, 'rolled a', outcome)
    print(draw_number(outcome))

def draw_number(n, dot='*'):
    """Return a text representation of rolling the number N.
    If a number has multiple possible representations (such as 2 and 3), any
    valid representation is acceptable.

    >>> print(draw_number(3))
     -------
    |     * |
    |   *   |
    | *     |
     -------

    >>> print(draw_number(5))
     -------
    | *   * |
    |   *   |
    | *   * |
     -------

    >>> print(draw_number(6, '$'))
     -------
    | $   $ |
    | $   $ |
    | $   $ |
     -------
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return draw_dice(True, False, False, False, dot)
    if n == 2: 
        return draw_dice(False, True, False, False, dot)
    if n == 3:
        return draw_dice(True, True, False, False, dot) 
    if n == 4:
        return draw_dice(False, True, True, False, dot)
    if n == 5:
        return draw_dice(True, True, True, False, dot)
    if n == 6:
        return draw_dice(False, True, True, True, dot)



def draw_dice(c, f, b, s, dot):
    """Return an ASCII art representation of a die roll.

    c, f, b, & s are boolean arguments. This function returns a multi-line
    string of the following form, where the letters in the diagram are either
    filled if the corresponding argument is true, or empty if it is false.

     -------
    | b   f |
    | s c s |
    | f   b |
     -------

    The sides with 2 and 3 dots have 2 possible depictions due to rotation.
    Either representation is acceptable.

    This function uses Python syntax not yet covered in the course.

    c, f, b, s -- booleans; whether to place dots in corresponding positions.
    dot        -- A length-one string to use for a dot.
    """
    assert len(dot) == 1, 'Dot must be a single symbol'
    border = ' -------'
    def draw(b):
        return dot if b else ' '
    c, f, b, s = map(draw, [c, f, b, s])
    top = ' '.join(['|', b, ' ', f, '|'])
    middle = ' '.join(['|', s, c, s, '|'])
    bottom = ' '.join(['|', f, ' ', b, '|'])
    return '\n'.join([border, top, middle, bottom, border])


# Game simulator

def num_allowed_dice(score, opponent_score):
    """Return the maximum number of dice allowed this turn. The maximum
    number of dice allowed is 10 unless the sum of SCORE and
    OPPONENT_SCORE has a 7 as its ones digit.

    >>> num_allowed_dice(1, 0)
    10
    >>> num_allowed_dice(5, 7)
    10
    >>> num_allowed_dice(7, 10)
    1
    >>> num_allowed_dice(13, 24)
    1
    """
    "*** YOUR CODE HERE ***"
    if hog_tied(score,opponent_score):
        return 1 
    else:
        return 10

def select_dice(score, opponent_score):
    """Select 6-sided dice unless the sum of scores is a multiple of 7.

    >>> select_dice(4, 24) == four_sided_dice
    True
    >>> select_dice(16, 64) == six_sided_dice
    True
    """
    "*** YOUR CODE HERE ***"
    if hog_wild(score, opponent_score):
        return four_sided_dice
    else:
        return six_sided_dice


def other(who):
    """Return the other player, for players numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def name(who):
    """Return the name of player WHO, for player numbered 0 or 1."""
    if who == 0:
        return 'Player 0'
    elif who == 1:
        return 'Player 1'
    else:
        return 'An unknown player'

def play(strategy0, strategy1):
    """Simulate a game and return 0 if the first player wins and 1 otherwise.

    A strategy function takes two scores for the current and opposing players.
    It returns the number of dice that the current player will roll this turn.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.

    strategy0:  The strategy function for player 0, who plays first.
    strategy1:  The strategy function for player 1, who plays second.
    """
    who = 0 # Which player is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    strategy = [strategy0, strategy1]
    score = [0, 0]

    while score[who] < goal:
        num_selected = strategy[who](score[who], score[other(who)])
        num_allowed = num_allowed_dice(score[who], score[other(who)])
        num_of_rolls = min(num_selected, num_allowed)
        dice = select_dice(score[who], score[other(who)])
        score[who] += take_turn(num_of_rolls, score[other(who)], dice, name(who))
        if score[who] >= goal :
            break
        else:
            who = other(who)

    return who

# Basic Strategy

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two game scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice to roll.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


# Experiments (Phase 2)

def make_average(fn, num_samples=100):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> avg_dice = make_average(dice, 100)
    >>> avg_dice()
    3.75
    >>> avg_score = make_average(roll_dice, 100)
    >>> avg_score(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"
    def avg_fn(*args):
        outcome = 0  
        count = 0
        while count < num_samples:
            outcome = outcome + fn(*args)
            count += 1
        average = outcome/ num_samples
        return average
    return avg_fn

def compare_strategies(strategy, baseline=always_roll(5)):
    """Return the average win rate (out of 1) of STRATEGY against BASELINE."""
    as_first = 1 - make_average(play)(strategy, baseline)
    as_second = make_average(play)(baseline, strategy)
    return (as_first + as_second) / 2  # Average the two results

def eval_strategy_range(make_strategy, lower_bound, upper_bound):
    """Return the best integer argument value for MAKE_STRATEGY to use against
    the always-roll-5 baseline, between LOWER_BOUND and UPPER_BOUND (inclusive).

    make_strategy -- A one-argument function that returns a strategy.
    lower_bound -- lower bound of the evaluation range.
    upper_bound -- upper bound of the evaluation range.
    """
    best_value, best_win_rate = 0, 0
    value = lower_bound
    while value <= upper_bound:
        strategy = make_strategy(value)
        win_rate = compare_strategies(strategy)
        print('Win rate against the baseline using', value, 'value:', win_rate)
        if win_rate > best_win_rate:
            best_win_rate, best_value = win_rate, value
        value += 1
    return best_value

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # Change to False when done testing always_roll
        result = eval_strategy_range(always_roll, 1, 10)
        print('Best always_roll strategy:', result)

    if True: # Change to True when ready to test make_comeback_strategy
        result = eval_strategy_range(make_comeback_strategy, 5, 15)
        print('Best comeback strategy:', result)

    if True: # Change to True when ready to test make_mean_strategy
        result = eval_strategy_range(make_mean_strategy, 1, 10)
        print('Best mean strategy:', result)

    "*** You may add additional experiments here if you wish ***"


# Strategies

def make_comeback_strategy(margin, num_rolls=5):
    """Return a strategy that rolls one extra time when losing by MARGIN."""
    "*** YOUR CODE HERE ***"
    def comeback(score, opponent_score):
        if scoreplayer2 - scoreplayer1 >= margin:
            return num_rolls + 1
        else:
            return num_rolls 
    return comeback

def make_mean_strategy(min_points, num_rolls=5):
    """Return a strategy that attempts to give the opponent problems."""
    "*** YOUR CODE HERE ***"
    def mean_strategy(score, opponent_score):
        freebacon_score = free_bacon(score, opponent_score)
        touchdown_score = touchdown(freebacon_score) 
        hogitmusprime_score = hogitmus_prime(touchdown_score)
        if hogitmusprime_score < min_points: 
            return num_rolls
        if hog_tied(hogitmusprime_score, opponent_score) or hog_wild(hogitmusprime_score, opponent_score): 
            return 0 
        else: 
            return num_rolls
    return mean_strategy

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    The strategy greatly emphasizes different cases of when we must take advantage of the free bacon roll 0 rule to enhance points. 

    The most important strategy to consider is when all cases and score are greater than 100, we will return 0.  This is to ensure that we obtain free bacon points.  

    The next case is when number allowed dice is one, we will return 0 if the opponent score is greater than 30 and 1 otherwise to increase our chance of free bacon where we would receive a score of 4 or greater. 
        
    If both opponent score and our score is less than goal, we return 0 if bacon and score are 100. However, if our score is midway to 100, around 49, we will return 0 if hog wild and bacon is greater than 3 is present

    The strategy also takes into consideration hog tied and bacon.  If bacon is 3, we will return 0 once again since the probability of scores ending in a seven is 0.1 and when the score is 49, we can get 5 points. We take a risk and return 10 otherwise if it is not hog tied if our score is 49.   

    When dice is 4 sided and opponent score is greater than 19, we will return 0. Otherwise, we will return 1. 

    Finally, if the diffrence between both scores is 5, we will return our comeback strategy as the last call to maximize points. 

    """
    "*** YOUR CODE HERE ***"
    bacon = free_bacon(score, opponent_score)
    diff = opponent_score - score
    point_away = 100 - score
    num_rolls = 5
    every_case = all_applied(score, opponent_score)
    if every_case + score >= 100: 
        return 0 
    if num_allowed_dice(score, opponent_score) == 1:
        if opponent_score > 30:
            return 0
        else:
            return 1
    if score < goal and opponent_score < goal:
        bacon = int(opponent_score/10)+1
        if bacon + score >= 100:
            return 0
        elif score == 49:
            if (opponent_score + score)%10 == 7:
                if bacon > 3:
                    return 0
                else:
                    return 1
            else:
                return 10
    if select_dice(score, opponent_score) == four_sided_dice:
        if opponent_score > 19:
            return 0
        else:
            return 1
    if diff > 5:
        return make_comeback_strategy(5)(score, opponent_score)
    else:
        return num_rolls
    

def final_strategy_test():
    """Compares final strategy to the baseline strategy."""
    print('-- Testing final_strategy --')
    print('Win rate:', compare_strategies(final_strategy))



# Interaction.  You don't need to read this section of the program.

def interactive_strategy(score, opponent_score):
    """Prints total game scores and returns an interactive tactic.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    print('Current score:', score, 'to', opponent_score)
    while True:
        response = input('How many dice will you roll? ')
        try:
            result = int(response)
        except ValueError:
            print('Please enter a positive number')
            continue
        if result < 0:
            print('Please enter a non-negative number')
        else:
            return result

def play_interactively():
    """Play one interactive game."""
    global commentary
    commentary = True
    print("Shall we play a game?")
    winner = play(interactive_strategy, always_roll(5))
    if winner == 0:
        print("You win!")
    else:
        print("The computer won.")

def play_basic():
    """Play one game in which two basic strategies compete."""
    global commentary
    commentary = True
    winner = play(always_roll(5), always_roll(6))
    if winner == 0:
        print("Player 0, who always wants to roll 5, won.")
    else:
        print("Player 1, who always wants to roll 6, won.")

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--take_turn_test', '-t', action='store_true')
    parser.add_argument('--play_interactively', '-p', action='store_true')
    parser.add_argument('--play_basic', '-b', action='store_true')
    parser.add_argument('--run_experiments', '-r', action='store_true')
    parser.add_argument('--final_strategy_test', '-f', action='store_true')
    args = parser.parse_args()
    for name, execute in args.__dict__.items():
        if execute:
            globals()[name]()



