## Download sequential files challenge

### Desciption
The aim of this challenge is to write a function that downloads a sequence of files. The files must differ from each other for a number in their name or path. The input URL must be a file in the sequence.

### Solution
For this challenge I've used the modules request and os. It uses a recursive function to access all possible paths in the domain.
It will only donwload files if their path or name differ for one or more numbers.\
Examples for different file names:\
dowload_sequential('http://www.example.com/image1.jpg',output_path) WILL download 'http://www.example.com/image5.jpg'. \
dowload_sequential('http://www.example.com/image1.jpg',output_path) WILL NOT download 'http://www.example.com/image12.jpg'. (File name is one character longer) \
dowload_sequential('http://www.example.com/cat.jpg',output_path) WILL NOT download 'http://www.example.com/dog.jpg'. (File names differ for alphabetical letters) \
Examples for different paths:\
dowload_sequential('http://www.example.com/folder1/image1.jpg',output_path) WILL download 'http://www.example.com/folder2/image5.jpg'. \
dowload_sequential('http://www.example.com/folderA/image1.jpg',output_path) WILL NOT download 'http://www.example.com/folderB/image5.jpg'. (The paths differ for alphabetical letters) \
dowload_sequential('http://www.example1.com/folder1/image1.jpg',output_path) WILL NOT download 'http://www.example2.com/folder2/image5.jpg'. (The domain is different) \

### Usage
dowload_sequential(url,output_path) where url is the a file in the sequence and output_path is the path where the files will be saved to. Try url='http://699340.youcanlearnit.net/image001.jpg' output_path='./Downloaded'