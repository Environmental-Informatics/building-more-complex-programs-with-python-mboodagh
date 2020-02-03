#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:15:31 2020

@author: mboodagh
"""

""" The purpose of this program is to find 
the greatest common divisor of two numbers"""

# Define a function that returns the greatest common divisor of two inputs
def gcd(a,b):
    # check if a>b, and replace them if necessary
    if a<b:   
        x=a
        a=b
        b=x
    
    r=a % b   # calculate the remainder 
    # replace the smallest number with the remainder and continue until the remainder is zero
    if r==0:
        return b
    else:
        a=b
        b=r
        return gcd(a,b)
    
# print the greatest common divisor
print(gcd(64,32))
    
    
     