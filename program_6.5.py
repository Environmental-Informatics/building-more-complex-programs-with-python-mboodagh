#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:15:31 2020

@author: mboodagh
"""

def gcd(a,b):
    if a<b:  # check if a>b 
        x=a
        a=b
        b=x
    
    r=a % b   # calculate the remainder 
    if r==0:
        return b
    else:
        a=b
        b=r
        return gcd(a,b)
    
print(gcd(27,32))
    
    
     