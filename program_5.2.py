#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:05:34 2020

@author: mboodagh
"""
# A fubction to check Fermant's theorem
def check_fermat ():
    a=input ('please enter the first number>1 ') # must turn to a positive integer
    b=input ('please enter the second number>1 ') # must turn to a positive integer
    c=input ('please enter the third number>1 ') # must turn to a positive integer
    n=input ('please enter the power >3 = ') # must turn to an integer >2
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    if a**n+b**n != c**n:
        print ('N0, that doesnt work')
    else:
        print('Holy smokes, Fermat was wrong')
                
check_fermat ()     