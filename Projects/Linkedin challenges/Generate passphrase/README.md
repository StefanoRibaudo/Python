## Generate passphrase challenge

### Desciption
The aim of this challenge is to write a function that returns a string of words separated by spaces. The number of words is specified as argument while the words are randomly selected from a pool.

### Solution
The pool of words was downloaded from diceware.com . The function generates 5 random number between 1 and 6 and uses these rolls to select a word from the pool. The words are returned with a .join method.

### Usage
gen_pass(N) returns a string of N randomly selected words.