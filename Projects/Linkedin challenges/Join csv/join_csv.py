# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:36:04 2020

@author: ribau
"""
def merge_csv(input_csv_paths_list,output_csv_path):
    import pandas as pd
    
    csv1=pd.read_csv(input_csv_paths[0])
    csv2=pd.read_csv(input_csv_paths[1])
    
    joined=csv1.append(csv2)
    joined.to_csv(output_csv_path)






