# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:48:30 2020

@author: ribau
"""
def find_factors(number):
    import numpy as np
    
    def check_if_prime(number,prime_list):  #If number is prime returns True, False otherwise. Requires list of previous primes found
        for prime in prime_list:
            if number % prime == 0:
                return False
        return True
    
    def factorize(number,prime_list): #Returns factorization of number.
        factorials=[]
        for prime in prime_list:
            while number % prime == 0 and number != 1:
                number=int(number/prime)
                factorials.append(prime)
        return factorials
                
    
    def primes_until(number): #Searches and returns the prime number until the argument, starting from the last search. Saves the result of the search in saved_primes.npy. The key of the saved dict is the argument of last search.
        try: #Checking if file exists
            prime_dict=np.load('saved_primes.npy',allow_pickle='TRUE').item()
        except: #Initializing file
            prime_dict={str(0) : []}
            np.save('saved_primes.npy',prime_dict)
        
        checked_until=int(list(prime_dict.keys())[0]) #Extract last search argument from dict
        prime_list=prime_dict[str(checked_until)] #Extract saved prime numbers
        
        #if number>checked_until:
        for n_to_check in range(checked_until+1,number+1): #Adding primes until number
            if check_if_prime(n_to_check,prime_list) and n_to_check != 1:
                prime_list.append(n_to_check)
                
        prime_dict={str(number) : prime_list} #Constructing and saving dictionary of primes
        np.save('saved_primes.npy',prime_dict)
        
        return prime_list
    
    prime_list=primes_until(number)
    factors=factorize(number,prime_list)
    return factors


def delete_save():
    import os
    try:
        os.remove('saved_primes.npy')
        print('Saved primes removed!')
    except:
        print('No saves found.')




