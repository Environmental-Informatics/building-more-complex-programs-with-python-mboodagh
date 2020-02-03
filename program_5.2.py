#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:05:34 2020

@author: mboodagh
"""
""" The goal of this program is to check whether 
the Fermant's principle holds for a set of values provided by the user"""

# Define a function to check Fermant's theorem and prints the results
def check_fermat ():
    # Ask for the inputs and turn them into integers
    a=float(input ('please enter the first number>1 ')) # The number must be >1 to be turned into a positive integer
    b=float(input ('please enter the second number>1 ')) # The number must be >1 to be turned into a positive integer
    c=float(input ('please enter the third number>1 ')) # The number must be >1 to be turned into a positive integer
    n=float(input ('please enter the power >3 = ')) # The number must be >3 to be turned into a an integer>2 
    # turning the inputs into integers
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    # Print the outcome
    if a**n+b**n != c**n:
        print ('N0, that doesnt work')
    else:
        print('Holy smokes, Fermat was wrong')
        
# run the function                
check_fermat ()    
