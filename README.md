# Game of Greed

**Author**: Grace Choi, Sam Clark, Matthew Holder, Audrena Vacirca
**Version**: 1.0.2

## Overview
Roll some dice, get some scores, keep track of the scores.
Methods:
calculate_score() - calculates score
roll_dice() - rolls random dice
shelf() - shelves score
bank() - banks score
clear_shelf() - clears shelf

## Tests
#### Testing - Roll Dice
When rolling 1 to 6 dice ensure…
- A sequence of correct length is returned
- Each item in sequence is an integer with value between 1 and 6

#### Testing - Calculate Score
zilch - non scoring roll should return 0
ones - rolls with various number of 1s should return correct score
twos - rolls with various number of 2s should return correct score
threes - rolls with various number of 3s should return correct score
fours - rolls with various number of 4s should return correct score
fives - rolls with various number of 5s should return correct score
sixes - rolls with various number of 6s should return correct score
straight - 1,2,3,4,5,6 should return correct score
three_pairs - 3 pairs should return correct score
two_trios - 2 sets of 3 should return correct score
leftover_ones - 1s not used in set of 3 (or greater) should return correct score
leftover_fives - 5s not used in set of 3 (or greater) should return correct score

#### Testing - Banker
*shelf*  
should properly track unbanked points  
*bank*  
should properly add unbanked points to total and return the deposited amount  
*clear_shelf*  
should remove any unbanked points, resetting to zero.  
should not affect previously banked points  

## Change Log
12-29-2020 6:30pm - Started lab, divided 1 method per group member. Completed 4 methods.
12-30-2020 6:30pm - Finished all methods. 
