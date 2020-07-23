# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:37:45 2020

@author: ribau
"""
def sim_dice(dice_list):
    import random
    n_simulations=10**6
    results=[]
    
    for i in range(n_simulations):
        simulation=0
        for j in range(len(dice_list)):
            simulation=simulation+random.randrange(1,dice_list[j]+1)
        
        results.append(simulation)
    
    for i in range(len(dice_list),sum(dice_list)+1):
        print(str(i)+'   {:.2f} %'.format(results.count(i)/n_simulations*100))
    
    
    
    










