from sprites import *
d = Sprite(shape='black', visible=False)
d.screen.bgcolor('black')
# 半径
radius = 201

while True:
    d.randomcolor()
    d.randomheading()
    d.fd(random.randint(1, radius))

    d.dot(12)
    d.home()