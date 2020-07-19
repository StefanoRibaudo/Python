## Factorization challenge

### Desciption
The aim of this challenge is to write a function that returns the factors of a number.
Requires numpy and os.

### Solution
My solution is based on the 'remainder' strategy and is optimized for sequential calls. The function writes a file 'saved_primes.npy' that contains all the primes numbers it previously found. This is to avoid trying to divide for non-prime numbers.

### Usage
Two functions are defined.\
find_factors(number) returns a list of prime factors of number and saves information on primes up to number in 'saved_primes.npy'.\
delete_save() deletes 'saved_primes.npy'.