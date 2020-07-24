# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:04:16 2020

@author: ribau
"""
def gen_pass(n_words):
    import random
    
    passphrase=[]
    f=open('diceware.txt','r')
    text=f.read().split()
    numbers=text[::2]
    words=text[1::2]
    f.close()
    for i in range(n_words):
        rand_6=''.join(map(str,random.choices(list(range(1,7)),k=5)))
        index=numbers.index(rand_6)
        passphrase.append(words[index])
    
    return ' '.join(passphrase)


