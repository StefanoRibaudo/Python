# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:31:10 2020

@author: ribau
"""
def zip_with_extension(path,extension):
    import zipfile,os
    import numpy as np
    
    def extension_index(filenames):
        return np.array(list(map(lambda x: x.endswith(extension),filenames)))
    
    with zipfile.ZipFile('./zipped_files.zip','w') as zip_file:
    
        for dirpath, dirnames, filenames in os.walk('.'):
            filenames=np.array(filenames)
            
            for filename in filenames[extension_index(filenames)]:
                filepath=os.path.join(dirpath,filename).replace("\\","/")
                zip_file.write(filepath)





