# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:15:25 2020

@author: ribau
"""
import math

def is_palindrome(string):

    string=string.lower()
    #Remove non-letters
    import re
    
    regex = re.compile('[^a-z]')
    alpha_string=regex.sub('', string)
    
    #Solving
    nletters=len(alpha_string)
    up_half=math.ceil(nletters/2)
    lo_half=math.floor(nletters/2)
    return alpha_string[0:lo_half] == alpha_string[-1:up_half-1:-1]
















