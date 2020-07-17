# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:00:58 2020

@author: ribau
"""
import numpy as np
import itertools

def unwrap(raw_ind,sudsize):
    ind_row=raw_ind//sudsize
    ind_col=raw_ind-ind_row*sudsize
    return ind_row,ind_col

def intersect_set(pool,negative_tries_mat,s_map,keys,current_index):
    
    result=set(pool[keys['r']]).intersection(pool[keys['c']]).intersection(pool[keys['s']]).intersection(negative_tries_mat[current_index])
    
    return list(result)



# Initialization
f=open('sudoku.txt','r')
initial=f.read().split()
f.close()
sudsize=int(np.sqrt(len(initial)))
negative_tries_mat=np.empty((sudsize,sudsize),dtype='object')
keys=dict()
solv_order_ind=list()

sudmat=np.zeros([sudsize,sudsize],dtype='int32')
for i in range(sudsize):
    for j in range(sudsize):
        sudmat[i,j]=initial[i*sudsize+j]
        negative_tries_mat[i,j]=list(range(1,sudsize+1))
givens=np.vectorize(bool)(sudmat)


# Get possible numbers per row,col and small square
pool=dict()
for i in range(sudsize): # Rows
    pool['r{}'.format(i)]=list(range(1,sudsize+1))
    for j in range(sudsize):
        if sudmat[i,j] != 0:
            pool['r{}'.format(i)].remove(sudmat[i,j])
            
for i in range(sudsize): # Cols
    pool['c{}'.format(i)]=list(range(1,sudsize+1))
    for j in range(sudsize):
        if sudmat[j,i] != 0:
            pool['c{}'.format(i)].remove(sudmat[j,i])

s_map=np.zeros([sudsize,sudsize,2],dtype='int32')
for i in range(int(np.sqrt(sudsize))): # Small squares
    for j in range(int(np.sqrt(sudsize))):
        pool['s{}{}'.format(i,j)]=list(range(1,sudsize+1))
        for ii in range(i*int(np.sqrt(sudsize)),(i+1)*int(np.sqrt(sudsize))):
            for jj in range(j*int(np.sqrt(sudsize)),(j+1)*int(np.sqrt(sudsize))):
                s_map[ii,jj,:]=[i,j]
                if sudmat[ii,jj] != 0:
                    pool['s{}{}'.format(i,j)].remove(sudmat[ii,jj])

# Computing end index
end_index=sudsize**2-1
for i, j in itertools.product(range(sudsize), range(sudsize)):
    if givens[-i-1,-j-1]:
        end_index-=1
    else:
        break

# Computing start index
start_index=0
for i, j in itertools.product(range(sudsize), range(sudsize)):
    if givens[i,j]:
        start_index+=1
    else:
        break

# Computing solving order
solv_order=np.empty((sudsize,),dtype='object')
for i in range(sudsize):
    solv_order[i]=list()
for current_raw_ind in range(sudsize**2):
    current_index=unwrap(current_raw_ind,sudsize)
    if not givens[current_index]:
        keys['r']='r{}'.format(current_index[0])
        keys['c']='c{}'.format(current_index[1])
        keys['s']='s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])

        n_moves=len(intersect_set(pool,negative_tries_mat,s_map,keys,current_index))
        solv_order[n_moves-1].append(current_raw_ind)
    else:
        solv_order[sudsize-1].append(current_raw_ind)
for i in range(sudsize):
    solv_order_ind.extend(list(solv_order[i]))
    
#solv_order_ind2=[79, 22, 30, 33, 34, 39, 41, 46, 50, 51, 70, 71, 75, 76, 4, 47, 53, 58, 66, 69, 21, 57, 64, 10, 27, 29, 74, 78, 25, 1, 16, 55, 59, 72, 42, 44, 24, 62, 18, 23, 56, 8, 14, 26, 2, 5, 15, 17, 6, 9, 11, 63, 36, 38, 65, 54]
#solv_order_ind2.extend(solv_order_ind[len(solv_order_ind2):-1])
#solv_order_ind=solv_order_ind2.copy()
#solv_order_ind=[21, 30, 34, 50, 76, 79, 22, 33, 39, 41, 46, 51, 75, 4, 10, 29, 44, 47, 53, 57, 58, 70, 71, 1, 8, 23, 27, 38, 42, 54, 55, 59, 64, 66, 69, 78, 2, 5, 9, 11, 14, 16, 17, 25, 26, 36, 56, 62, 63, 65, 72, 74, 6, 15, 18, 24, 0, 3, 7, 12, 13, 19, 20, 28, 31, 32, 35, 37, 40, 43, 45, 48, 49, 52, 60, 61, 67, 68, 73, 77, 80]
# Solving

solved=False
#current_raw_ind=start_index
current_raw_ind=0
current_index=unwrap(solv_order_ind[current_raw_ind],sudsize)
max_current=0
cycle_num=int(0)

keys['r']='r{}'.format(current_index[0])
keys['c']='c{}'.format(current_index[1])
keys['s']='s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])

while not solved:
    cycle_num+=1
    if current_raw_ind>max_current:
        print('{:.2f}%'.format(current_raw_ind/sudsize**2*100))
        max_current=current_raw_ind
    moves_set=intersect_set(pool,negative_tries_mat,s_map,keys,current_index)
    if sudmat[current_index] != 0:
        pool[keys['r']].append(sudmat[current_index])
        pool[keys['c']].append(sudmat[current_index])
        pool[keys['s']].append(sudmat[current_index])
        #moves_set.append(sudmat[current_index])
    if moves_set:
        sudmat[current_index]=moves_set[0]
        pool[keys['r']].remove(sudmat[current_index])
        pool[keys['c']].remove(sudmat[current_index])
        pool[keys['s']].remove(sudmat[current_index])
        negative_tries_mat[current_index].remove(sudmat[current_index])
        
        found_next_iterable=False
        while not found_next_iterable:
            if current_raw_ind == end_index:
                solved=True
                found_next_iterable=True
            else:
                current_raw_ind+=1
                current_index=unwrap(solv_order_ind[current_raw_ind],sudsize)
                if not givens[current_index]:
                    found_next_iterable=True
        keys['r']='r{}'.format(current_index[0])
        keys['c']='c{}'.format(current_index[1])
        keys['s']='s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])
                      
    else:
        sudmat[current_index]=0
        negative_tries_mat[current_index]=list(range(1,sudsize+1))
        found_next_iterable=False
        while not found_next_iterable:
            current_raw_ind-=1
            current_index=unwrap(solv_order_ind[current_raw_ind],sudsize)
            if not givens[current_index]:
                found_next_iterable=True
        keys['r']='r{}'.format(current_index[0])
        keys['c']='c{}'.format(current_index[1])
        keys['s']='s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])
           
    
print('\n\n\n Solved in {} cycles!!!\n'.format(cycle_num))
print(sudmat)




    

"""
sudmat[current_index]=list(intersect_set(pool,negative_tries_mat,s_map,current_index))[0]
pool['r{}'.format(current_index[0])].remove(sudmat[current_index])
pool['c{}'.format(current_index[1])].remove(sudmat[current_index])
pool['s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])].remove(sudmat[current_index])






pool['r{}'.format(current_index[0])].append(sudmat[current_index])
pool['c{}'.format(current_index[1])].append(sudmat[current_index])
pool['s{}{}'.format(s_map[current_index[0],current_index[1],:][0],s_map[current_index[0],current_index[1],:][1])].append(sudmat[current_index])
sudmat[current_index]=0
"""











