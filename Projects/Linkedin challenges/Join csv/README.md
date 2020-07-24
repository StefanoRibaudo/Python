## Merge csv files challenge

### Desciption
The aim of this challenge is to write a function that saves a csv file that is constructed from two csv files in input.

### Solution
Pandas has everything you need to solve this challenge already build-in. The method .append does exactly what is required.

### Usage
merge_csv(input_csv_paths_list,output_csv_path) saves the merged csv to 'output_csv_path'. The argument 'input_csv_paths_list' must be a list of strings with the input files paths.