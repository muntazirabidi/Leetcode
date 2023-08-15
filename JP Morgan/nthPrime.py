#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:35:13 2022

@author: muntazirabidi
"""

primes = []
 
# Function to generate N prime numbers using 
# Sieve of Eratosthenes
def primes_func():
     
    n = 10000005
     
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
     
    p = 2
    while (p * p <= n):
           
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
               
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
                 
        p += 1
       
    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
            

    
        
 

# Driver code
if __name__=='__main__':
     
    # Function call
    primes_func()   
     
    print("5th prime number is", primes[4]);
    print("16th prime number is", primes[15]);
    print("1049th prime number is", primes[1048]);

