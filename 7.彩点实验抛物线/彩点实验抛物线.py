# 彩点实验抛物线
from sprites import *
d = Sprite(shape='black', visible=False)
d.screen.bgcolor('black')

while True:
    d.randompos()
    if d.ycor() > 0.5*d.xcor()*d.xcor() / 100:
        d.randomcolor()
        d.dot(12)