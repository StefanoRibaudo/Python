## Zip all files with extension challenge

### Desciption
The aim of this challenge is to write a function that saves a zip file containing all the files with a given extension in a folder or subfolders. Folders structure must be the same.

### Solution
For this challenge I've used the modules zipfile, os and numpy. zipfile and os are to interact with zip files and to easily locate paths to the files. Numpy is used for advanced indexing.

### Usage
zip_all(path,extension) zips all files in given path and subpaths that present the given extension. The zip file is crated where the python working directory is.