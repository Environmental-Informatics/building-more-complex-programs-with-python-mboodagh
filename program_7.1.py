#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:42:34 2020

@author: mboodagh
"""

""" The purpose of this program is to define a function to calculate the mean sqaure root of a number 
and compare it with the Python's built-in function and calculate the error"""

# Import the required modules
import math
 
# define a function that calculates the mean square root  of numbers from 1 to the given input and returns the estimate value of the square root of the given number 
def mysqrt(a):

    # print the header
    print ('a','  mysqrt(a)','       math.sqrt(a)','    diff')
    print ('-','  -------------','   ------------','    ----')
    
    # calculate the approx values based on the arbitrary initial guess
    for u in range(1,a+1):
        x=1.5 # initial guess
        y=2.2 # initial guess
        while abs(x-y)> 10**(-15): # do the iteration until the error equals its min value
          x=y
          y=(x+u/x)/2
    
    # calculate the real value and the difference
        u_m=math.sqrt(u)
        diff=abs(y-u_m)
        print (u,' ','%.11f'%y,'  ','%.11f'%u_m,'  ',diff)
    
    return y  # return the approx value of the square root

# end of the function's definition

# calulate for the numbers 1-9
mysqrt(9)  
    
      
        
