## Sort a string challenge

### Desciption
The aim of this challenge is to write a function that returns a sorted string of words arranged in alphabetical order. The outsput string has to retain lower and uppercases as per argument but has not to discretize upon lower or uppercase. Example: sort_string('baNana ORAnGE apple') returns 'apple baNana ORAnGE'. 

### Solution
The key to solving this challenge is to use .sort() with an adequate key function, the rest is trivial.

### Usage
sort_string(string) returns the sorted string of words. The argument can include non alphabetical characters and these will be sorted before alphabetical letters.