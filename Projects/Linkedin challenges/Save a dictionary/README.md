## Save dictioanry challenge

### Desciption
The aim of this challenge is to write a function to save a dictionary and one to load it.

### Solution
I've already solved this problem in my factorization challenge. Using numpy.save and numpy.load one can easily save variables in .npy format.

### Usage
save_dict(dictionary,path,dict_name) saves dictionary in path as dict_name. load_dict(path,dict_name) outputs the saved dictionary in "path/dict_name".