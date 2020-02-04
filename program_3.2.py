# -*- coding: utf-8 -*-
"""username:mboodagh"""
""" The purpose of this program to print a word 4 times"""

# define a function that repeats a function 2 times
def do_twice(f,x):
    f(x)
    f(x)
    
# define a function that prints the input 2 times.    
def print_twice(bruce):
    print(bruce)
    print(bruce)

# print spam 4 times    
do_twice(print_twice,'spam')


     
        