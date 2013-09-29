the_hog_game
============


Please see hog.py file.

In this project, I developed a simulator and multiple strategies for the dice game Hog. I implemented some higher-order functions, experiment with random number generators, and generate some ASCII art.

In Hog, two players alternate turns trying to reach 100 points first. On each turn, the current player chooses some number of dice to roll, up to 10. She scores the sum of the dice outcomes, unless any of the dice come up a 1 (Pig out), in which case she scores only 1 point for the turn.

To spice up the game, I created five special rules:

Hog Tied. If the sum of both players' scores ends in a seven (e.g., 17, 27, 57), then the current player can roll at most one die.
Hog Wild. If the sum of both players' scores is a multiple of seven (e.g., 14, 21, 35), then the current player rolls four-sided dice instead of the usual six-sided dice.
Free Bacon. If a player chooses to roll zero dice, she scores one more than the tens digit of her opponent's score. E.g., if the first player has 32 points, the second player can score four by rolling zero dice. If the opponent has fewer than 10 points (tens digit is zero), then the player scores one.
Touchdown. If a player's score for the turn is a multiple of 6, then the current player gains additional points equal to the turn score divided by 6. E.g., if the original turn score is 12, the player will earn 14 (12 + 2) points total for the turn, after the Touchdown rule.
Hogtimus Prime. If a player's score for the turn is a prime number, then the turn score is increased to the next largest prime number. Note: 1 is not prime. E.g., if the original turn score is 19, the player earns 23 points total for the turn. If the original turn score is 6, then the player earns 11 points total from the Touchdown and Hogtimus Prime rules.
