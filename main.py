Web VPython 3.2

import random

box = sphere(size=vector(10, 10, 10), opacity=0.3, color=color.gray(0.5))

balls = []

for i in range(1, 46):

    while True:
        pos_vec = vector.random() 
        if mag(pos_vec) <= 1: 
            break
            
    if i <= 10: c = color.yellow
    elif i <= 20: c = color.blue
    elif i <= 30: c = color.red
    elif i <= 40: c = color.black
    else: c = color.green
    
    s = sphere(radius=0.3, color=c)
    t = text(text=str(i), pos=vector(-0.15, -0.1, 0.3), height=0.2, color=color.white)
    
    b = compound([s, t])
    b.pos = pos_vec
    
    balls.append(b)
