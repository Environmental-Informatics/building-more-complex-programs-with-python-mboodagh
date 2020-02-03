#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:18:59 2020

@author: mboodagh
"""
""" This program draws flowers using the Think Python
 drawing package turulte
"""
#importing the required modules
import math
import turtle

#start a turtle object named bob
bob = turtle.Turtle()

# Define a fuction that draws a polyline 
# with four inputs(the turtle object, the number of line segments, the length of each line segment, the angle between each line segment) 
def polyline(t, n, length, angle):
    for i in range(n): 
        t.fd(length)
        t.lt(angle) 
        
# Define a function that draws an arc based on the polyline
# With two inputs(the turtle object, the radius, the angle between the line segments)   
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# Define a function that draws a petal based on the arc 
# With three inputs(the turtle object, the radius, the angle between the line segments)     
def petal(t,r,angle):    
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
        
# Define a function that draws a flower based on the petals
# With four inputs(the turtle object, the radius, the angle between the line segments, the number of petals)            
def flower(t,r,angle,n):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)

# Define a function that moves the object right or left 
# with two inputs (the turtle object, the displacment legth )        
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
# move the object 200 pixels to the left and draw it   
move(bob, -200)
flower(bob,60.0,60.0,7)

# move the object 200 pixels to the right relative to the first object and draw it 
move(bob, 200)
flower(bob, 40.0, 80.0,10)

# move the object 200 pixels to the right relative to the first object and draw it 
move(bob, 200)
flower(bob,200.0,20,20)

#end of the code