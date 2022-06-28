'''
最简弹球，本程序主要演示碰到边缘就反弹这个命令
'''
from sprites import *
# 1代表弹球
ball =Sprite(1)

while True:
    # 前进0.1
    ball.fd(0.1)
    # 碰到边缘就反弹
    ball.bounce_on_edge()