# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:21:58 2020

@author: ribau
"""
def index_all(list_to_be_searched,item):
    def rec_search(sublist,item,is_master,current_index,solution):
        if sublist==item:
            return current_index.copy(),solution
        
        if isinstance(sublist,list):
            current_index.append(None)
            for i in range(len(sublist)):
                current_index[-1]=i
                result,solution=rec_search(sublist[i],item,False,current_index.copy(),solution)
                if result:
                    solution.append(result)
                    if is_master:
                        return solution
                    else:
                        return False,solution
        if is_master:
            return solution
        else:
            return False,solution
    
    index=rec_search(list_to_be_searched,item,True,[],[])
    return index
    



"""
#For testing purposes

list_to_be_searched=[[[1,2,3],2,[1,3]],[1,2,3],[[[1,2,3],2,[1,3]],[1,2,3]]]
item=[1,2,3]
test=index_all(list_to_be_searched,item)

    
for i in range(len(test)):
    if isinstance(test[i],list):
        list_copy=list_to_be_searched
        for j in range(len(test[i])):
            list_copy=list_copy[test[i][j]]
        print('Searching for '+str(item)+', found at '+str(test[i])+'. Values match = '+str(item==list_copy))
    else:
        print(print('Searching for '+str(item)+', found at '+str(test[i])+'. Values match = '+str(item==list_to_be_searched[test[i]])))
"""





