# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:52:44 2020

@author: ribau
"""
def alarm(timer_in_seconds,wav_name,message):
    import winsound
    import time
    timer=time.time()+timer_in_seconds
    while time.time()<timer:
        pass
    winsound.PlaySound(wav_name, winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    
    print(message)
    input('Press Enter...')
    winsound.PlaySound(None, winsound.SND_PURGE)
    return None