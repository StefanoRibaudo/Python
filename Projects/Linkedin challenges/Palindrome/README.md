## Palindrome challenge

### Desciption
The aim of this challenge is to write a function that returns True if the argument is a palindrome, False otherwise.
Requires math.

### Solution
I've solved this challenge with and without the RE module. In both cases we clear the string of spaces and other non-alphabetical characters and then check if the first half is equal to the reversed second half. Both solutions are branchless.

### Usage
is_palindrome(string) returns True if string is palindrome, False otherwise. Only alphabetical characters are taken into account.