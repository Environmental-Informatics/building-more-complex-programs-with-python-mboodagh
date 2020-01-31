#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:42:34 2020

@author: mboodagh
"""
import math
def mysqrt(a):
    x=1
    y=2.2
    # print the header
    print'a','  mysqrt(a)','       math.sqrt(a)','    diff'
    print'-','  ---------','       ------------','    ----'
    # ask the user for the inputs
    # calculate the approx value
    while abs(x-y)> 10**(-15):
          x=y
          y=(x+a/x)/2
    #calculate the real value
    a_m=math.sqrt(a)
    diff=abs(y-a_m)
    print a,' ',y,'  ',a_m,'  ',diff
    return y 
mysqrt(3)  
    
      
        
