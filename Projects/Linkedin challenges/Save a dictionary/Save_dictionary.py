# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:17:10 2020

@author: ribau
"""
def save_dict(dictionary,path,dict_name):
    import numpy as np
    if dict_name.endswith('.npy'):
        np.save(path+'/'+dict_name,dictionary)
    else:
        np.save(path+'/'+dict_name+'.npy',dictionary)

def load_dict(path,dict_name):
    import numpy as np
    if dict_name.endswith('.npy'):
        return np.load(path+'/'+dict_name,allow_pickle='TRUE').item()
    else:
        return np.load(path+'/'+dict_name+'.npy',allow_pickle='TRUE').item()
    

