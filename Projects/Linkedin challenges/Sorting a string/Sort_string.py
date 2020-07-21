# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:29:34 2020

@author: ribau
"""
def sort_string(string):
    
    str_list=string.split(' ')
    str_list.sort(key=lambda string: string.lower())
    
    return ' '.join(str_list)









