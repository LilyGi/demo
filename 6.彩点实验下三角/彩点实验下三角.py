# 彩点实验下三角
from sprites import *
d = Sprite(shape='black', visible=False)
d.screen.bgcolor('black')

while True:
    d.randompos()
    if d.xcor() > d.ycor():
        d.randomcolor()
        d.dot(9)