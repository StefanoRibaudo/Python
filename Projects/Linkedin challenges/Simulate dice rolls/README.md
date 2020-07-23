## Send an email challenge

### Desciption
The aim of this challenge is to write a function that determines the probabilty of all possible outcomes when rolling dice. (When multiple dice are present, the total outcome is the sum of each dice)

### Solution
I've used a Monte Carlo method to simulate 1 Million rolles of the specified dice. The probability is computed against the total number of simulations.

### Usage
sim_dice(dice_list) accepts a list of numbers as arguments. The list should include how many sides each dice has. The probabilities are printed in console.\
Example: sim_dice([6,6]) prints:\
2   2.80 %\
3   5.54 %\
4   8.32 %\
5   11.07 %\
6   13.90 %\
7   16.64 %\
8   13.96 %\
9   11.12 %\
10   8.32 %\
11   5.56 %\
12   2.78 %