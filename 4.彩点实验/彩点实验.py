# 彩点实验
import time
from sprites import *
d = Sprite(shape='blank', visible=True)
d.screen.bgcolor('black')

while True:
    d.random_pos()
    d.randomcolor()
    time.sleep(0.3)
    d.dot(random.randint(10, 100))
