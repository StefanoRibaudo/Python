# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:10:53 2020

@author: ribau
"""

import time
import random

def waiting_game():
    playing = True
    while playing:
        rand_time=random.randrange(2,8)
        input('Target time is '+ str(rand_time)+ ' seconds. Press Enter to start, then Enter to stop.')
        start=time.time()
        input('Press Enter to stop.')
        finish=time.time()
        if rand_time>(finish-start):
            print('Your time is {:.2f} seconds. You were {:.2f} seconds too early!'.format(finish-start,rand_time-(finish-start)))
        else:
            print('Your time is {:.2f} seconds. You were {:.2f} seconds too late!'.format(finish-start,-rand_time+(finish-start)))
        if round(rand_time,2)==round(finish-start,2):
            print('OMG snipe that timer!!! You got exactly {:.2f} seconds!'.format(rand_time))
        ans=input('Wanna play again? (y or Enter to play) : ')
        if not (ans=='y' or ans=='Y' or ans==''):
            playing=False
        
        
