# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:00:58 2020

@author: ribau
"""
import numpy as np

def check(sudmat,ind_row,ind_col):
    sudsize=len(sudmat)
    invalid_move=False
    
    # Check row and col
    for i in range(sudsize): # Row
        if i != ind_row and sudmat[ind_row,ind_col] == sudmat[i,ind_col] and sudmat[i,ind_col] != 0:
            invalid_move=True
            return invalid_move
    for i in range(sudsize): # Col
        if i != ind_col and sudmat[ind_row,ind_col] == sudmat[ind_row,i] and sudmat[ind_row,i] != 0:
            invalid_move=True
            return invalid_move
    
    # Check square
    smallsize=int(np.sqrt(sudsize))
    square_ind=[-(-(ind_row+1)//smallsize),-(-(ind_col+1)//smallsize)]
    for i in range((square_ind[0]-1)*smallsize,(square_ind[0])*smallsize):
        for j in range((square_ind[1]-1)*smallsize,(square_ind[1])*smallsize):
            if i != ind_row and j != ind_col and sudmat[ind_row,ind_col] == sudmat[i,j] and sudmat[i,j] != 0:
                invalid_move=True
                return invalid_move
                
    return invalid_move

def unwrap(raw_ind,sudsize):
    ind_row=raw_ind//sudsize
    ind_col=raw_ind-ind_row*sudsize
    return ind_row,ind_col

# Initialization
initial=open('sudoku.txt','r').read().split()
sudsize=int(np.sqrt(len(initial)))

sudmat=np.zeros([sudsize,sudsize],dtype='int32')
for i in range(sudsize):
    for j in range(sudsize):
        sudmat[i,j]=initial[i*sudsize+j]
givens=np.vectorize(bool)(sudmat)

solved=False
current_raw_ind=0
current_index=unwrap(current_raw_ind,sudsize)
max_current=0
cicle_num=0

while not solved:
    cicle_num+=1
    if current_raw_ind>max_current:
        print('{:.2f}%'.format(current_raw_ind/sudsize**2*100))
        max_current=current_raw_ind
        
    if sudmat[current_index] == 0:
        sudmat[current_index]=1
    
    if not check(sudmat,current_index[0],current_index[1]):
        found_next_iterable=False
        while not found_next_iterable:
            # Checking if it is solved
            if current_raw_ind==(sudsize**2-1):
                solved=True
                break
            else:
                current_raw_ind+=1
                current_index=unwrap(current_raw_ind,sudsize)
                if not givens[current_index]:
                    found_next_iterable=True
                    break
    else:
        if sudmat[current_index] == sudsize:
            sudmat[current_index]=0
            found_next_iterable=False
            while not found_next_iterable:
                current_raw_ind-=1
                current_index=unwrap(current_raw_ind,sudsize)
                if not givens[current_index]:
                    if sudmat[current_index] == sudsize:
                        sudmat[current_index]=0
                    else:
                        found_next_iterable=True
                        sudmat[current_index]+=1
        else:
            sudmat[current_index]+=1
        continue
           
    
print('\n\n\n Solved in {} cicles!!!\n'.format(cicle_num))
print(sudmat)




    













