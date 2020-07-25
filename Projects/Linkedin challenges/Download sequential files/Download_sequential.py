# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:37:20 2020

@author: ribau
"""
#url='http://699340.youcanlearnit.net/image001.jpg'
#output_path='./Downloaded'

def dowload_sequential(url,output_path):
    import requests
    import os
    
    def detect_filename(url):
        str_parts=url.split('/')
        return str_parts[-1]
    
    def reconstruct_url(dissected_url):
        rec_url=[]
        for i in range(len(dissected_url)):
            rec_url.append(''.join(dissected_url[i]))
        return '/'.join(rec_url)
    
    def dissect_url(url):
        str_parts=url.split('/')
        dissected_url=[]
        for part_index in range(len(str_parts)):
            dissected_part=[]
            for letter_index in range(len(str_parts[part_index])):
                dissected_part.append(str_parts[part_index][letter_index])
            dissected_url.append(dissected_part)
        return dissected_url
    
    def download_and_save(url):
        r = requests.get(url)
        if r.ok:
            with open(output_path+'/'+detect_filename(url), 'wb') as f:
                f.write(r.content)
                print('Download of '+url+' successful')
        r.close()
                
    def cycle_url(current_index,num_index,dissected_copy):
        ind_part=num_index[current_index][0]
        ind_lett=num_index[current_index][1]
        for _ in range(0,10):
    
            if int(dissected_copy[ind_part][ind_lett])+1<=9:
                dissected_copy[ind_part][ind_lett]=str(int(dissected_copy[ind_part][ind_lett])+1)
            else:
                dissected_copy[ind_part][ind_lett]=str(0)
            if current_index>0:
                dissected_copy=cycle_url(current_index-1,num_index,dissected_copy)
            else:
                download_and_save(reconstruct_url(dissected_copy))
        return dissected_copy
    
    
    
    
    if not url.startswith('http://'):
        raise ValueError('Url must start with http://')
    
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    
    num_index=[]
    dissected_url=dissect_url(url)
    for part_index in range(len(dissected_url)):
        for letter_index in range(len(dissected_url[part_index])):
            if dissected_url[part_index][letter_index].isdecimal() and part_index>2:
                num_index.append([part_index,letter_index])
    
    
    
    cycle_url(len(num_index)-1,num_index,dissect_url(url))







