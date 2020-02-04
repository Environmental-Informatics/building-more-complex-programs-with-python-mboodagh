#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:14:09 2020

@author: mboodagh
"""
""" The major purpose of this program is to print bars and pluses in the requested shape of problme 3.2"""

# Define a function that repeats the function 2 times
def do_twice(f):
    f()
    f()

# Define a function that repeats the function f 4 times
def do_four(f):
    do_twice(f)
    do_twice(f)

# Define a function that prints plus and negatives in the requested order corresponding to the 1st row 
def print_beam():
    print( '+ - - - -', end=' ')

# Define a function that prints bars and spaces in a requested order corresponding to rows 2 to 5
def print_post():
    print ('|        ', end=' ')

# define a function that prints + 4 times  
def print_beams():
    do_four(print_beam)
    print ('+')

# define a function to print  | 4 times 
def print_posts():
    do_four(print_post)
    print ('|')

# define a function that prints a combination of beams and 4 times printed posts  
def print_row():
    print_beams()
    do_four(print_posts)

# define a function that repeats the print_row 4 times and adds the ending line to it
def print_grid():
    do_four(print_row)
    print_beams()
    
# print the final shape 
print_grid()
    