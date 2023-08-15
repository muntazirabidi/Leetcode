#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:12:36 2022

@author: muntazirabidi
"""

'''
The Himmelblau function is given by the following equation
f(x,y)=(x^2+y-11)^2 + (x+y^2-7)^2
In this exercise, we will program a gradient descent (GD) algorithm to find minima of the Himmelblau function.  
Please follow the signatures of the methods given.
1. Create a Himmelblau class that accepts a numpy vector of size 2 and returns a scalar value that is the Himmelblau function.
2. For optimization, we will also need to create a function that returns its first order derivatives. 
For our purposes, you can calculate the derivatives of the Himmelblau class explicitly. 
3. Create an GD class that accepts the Himmelblau class for optimization.
4. Use both classes to write a program to find a minimum of the Himmelblau function, together with the argmin. 
In addition, you are given that the search space can be limited to ?-5 <= x,y <= 5. 
Your routine should work for any reasonable initial point in this range.
'''

class Himmelblau:
    '''
    Implements the Himmelblau function.  
    Gives result evaluate at a point and as well as first order derivitives
    '''
    def __call__(self, value):
        '''
        value: numpy array to evaluate result of the function at
        Returns the result evaluated at value
        '''
        self.x, self.y = value[0], value[1]

        return (self.x**2 +self.y - 11)**2 + (self.x+ self.y**2 - 7)**2
    
    def derivative(self, value):
        '''
        value: numpy array to evaluate derivative at
        Returns the first derivitive evaluated at value (numpy array)
        '''
        self.x, self.y = value[0], value[1]
        
        df_dx = 4*self.x*(self.x**2 + self.y -11) +2 *(self.x + self.y**2 -7)
        df_dy = 2*(self.x**2 + self.y -11) + 4*self.y*(self.x+self.y**2 - 7)

        # df_dx * deltax + df_dy * deltay
        return [df_dx, df_dy]


class GD:
    '''
    Implements the gradient descent (GD) method.  
    '''
    def __init__(self, function, initial_value):
        '''
        function: function to optimize
        initial_value: initial value to evaluate the function at
        '''
        self.x, self.y = initial_value[0], initial_value[1]
        print(self.x, self.y)
        
        self.df_dx, self.df_dy =  function.derivative(initial_value)
    
    def update(self, learning_rate=0.001):
        '''
        learning_rate: gd learning rate (default = 0.001)
        Executes one GD step
        ''' 
        
        df_dx,df_dy = function.derivative([self.x,self.y])
    

        self.x = self.x  -  learning_rate * self.df_dx
        self.y = self.y  -  learning_rate * self.df_dy
        
        #print(self.x,self.y)
        
    def value(self):
        '''Returns the current value found by GD'''
        return [self.x, self.y]
    
    def result(self):
        '''Returns the result at the current value'''
        return function([self.x,self.y])



class Solution:
    
    def __init__(self, x = None, y=None):
        self.x = x
        self.y = y
        
        self.max_iteration = 10000
        
        self.iters = 0
        
        self.precision= 0.001
        
        function = Himmelblau()
        
        self.gradient = GD(function, [self.x,self.y])
        
        
       
        
    def optimize(self):
        
        # Update members of self any way you like. 
        # Running this method once should give your final solution.
        
        while previous_step_size > self.precision and self.iters < self.max_iteration:
            
            
        




function = Himmelblau()

#print(function([1,2]))

#print(function.derivative([1,2]))

gradient_descent = GD(function, [1,2])

print(gradient_descent.update())
print(gradient_descent.value())
print(gradient_descent.result())


sol = Solution(1,2)
print(sol.optimize())