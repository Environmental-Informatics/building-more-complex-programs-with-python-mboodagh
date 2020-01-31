#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:18:59 2020

@author: mboodagh
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:02:34 2020
@author: mboodagh
"""

import math
import turtle
bob = turtle.Turtle()
#cricle function
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
 #polyline function   
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
 #arc function based on the polyline   
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
#polygon function based on the polyline  
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
 # making a petal   
def petal(t,r,angle):    
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
 # making n number of petals       
def flower(t,r,angle,n):
    for i in range(n):
        petal(t,r,angle)
        t.lt(360/n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
    
move(bob, -200)
flower(bob,60.0,60.0,7)

move(bob, 200)
flower(bob, 40.0, 80.0,10)

move(bob, 200)
flower(bob,200.0,20,20)