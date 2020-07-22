## Find all list items challenge

### Desciption
The aim of this challenge is to write a function that returns an index list pointing at all occurences of an item in a list. The item can be any object that supports the equality operator. The list in argument can have nested lists of objects.

### Solution
The solution involves a recursive function. This function calls itself with a sub-list in case of nested lists while preserving the solution.

### Usage
index_all(list_to_be_searched,item) returns a list of indexes. The elements of the nested lists indicate the subsequential subscripts that point to the item searched.\
Example: if index_all(list_to_be_searched,item) returns [[0,1,2],[1,2]] , then item can be found at list_to_be_searched[0][1][2] and list_to_be_searched[1][2].