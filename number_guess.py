#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:14:07 2022

@author: muntazirabidi
"""

import random

secret_number = random.randint(0,100)
trial_number  = 0
done = False

while not(done):
    trial_number += 1
    number_in = (int)(input('Enter your guess (between 0 and 100): '))
    if number_in == secret_number:
        print('Congratulations!')
        print('You got it in {} 23'.format(trial_number))
        done = True
    elif number_in < secret_number:
        print('Try higher...')
    else:
        print('Try lower...')