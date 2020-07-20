# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:15:25 2020

@author: ribau
"""
import math

def is_palindrome(string):

    string=string.lower()
    
    #Removing non-letters
    alpha_string=""
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(string)):
        alpha_string=alpha_string + string[i] * (string[i] in alphabet)
        
    #Solving
    nletters=len(alpha_string)
    up_half=math.ceil(nletters/2)
    lo_half=math.floor(nletters/2)
    return alpha_string[0:lo_half] == alpha_string[-1:up_half-1:-1]
















