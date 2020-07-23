# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:06:08 2020

@author: ribau
"""
def count_words(txt_file):
    f = open(txt_file, "r")
    
    text=f.read()
    text=text.lower()
    separated_text=text.split()
    
    words_dict={}
    for word in separated_text:
        if word in words_dict:
            words_dict[word]+=1
        else:
            words_dict[word]=1
    
    print('This file has '+str(len(words_dict))+' unique words.')
    
    words_list=list(words_dict.keys())
    words_count_list=list(words_dict.values())
    words_list.sort(key=lambda key: words_dict[key],reverse=True)
    words_count_list.sort(reverse=True)
    first_20_words_count=words_count_list[0:20]
    first_20_words=words_list[0:20]
    
    print('Top 20 words:')
    for i in range(20):
        print(first_20_words[i]+'    '+str(first_20_words_count[i]))