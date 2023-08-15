#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:27:39 2022

@author: muntazirabidi
"""

        

class GD:
    '''
    Implements the gradient descent (GD) method.  
    '''
    def __init__(self, function, initial_value):
        '''
        function: function to optimize
        initial_value: initial value to evaluate the function at
        '''
        
        x0, y0 = initial_value[0], initial_value[1]
        pred_value = function.__call_(initial_value)
        df_dx, df_dy = function.derivative(initial_value)
    
    def update(self, learning_rate=0.001):
        '''
        learning_rate: gd learning rate (default = 0.001)
        Executes one GD step
        ''' 

        x0 = x0  -  learning_rate * df_dx
        y0 = y0  -  learning_rate * df_dy

        



    def value(self):
        
        '''Returns the current value found by GD'''
        pass
    
    def result(self):
        '''Returns the result at the current value'''
        pass
        
class Solution:
    def __init__(self, x = None, y=None):
       
        
    def optimize(self):
        # Update members of self any way you like. 
        # Running this method once should give your final solution.
        pass
        
        
    
    # Other methods you might need go here.

if __name__ == "__main__":
    # Run tests here
