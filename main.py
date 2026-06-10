Web VPython 3.2
  
import random

box = sphere(size=vector(10, 10, 10), opacity=0.3, color=color.gray(0.5))
balls = []

for i in range(46) :
    
    balls.append(sphere(radius=0.4,pos = vec(0,0,0)))

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        for i in range(46) :
            balls[i].pos.x = balls[i].pos.x + random.uniform(-1,1)
            balls[i].pos.y = balls[i].pos.y + random.uniform(-1,1)
            
