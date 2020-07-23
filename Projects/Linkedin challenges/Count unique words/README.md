## Count unique words challenge

### Desciption
The aim of this challenge is to write a function that prints information about how many unique words appear in a text and the 20 most popular words.

### Solution
The solution involves using the .sort() method with an adequate key function. Trivial parts include reading the file and extracting the data from the text.

### Usage
count_words(text) prints the information requested. Mind that punctuation is counted as letters (when close to a word) or as a word (if surrounded by spaces). This was intentionally left as per challenge specification.