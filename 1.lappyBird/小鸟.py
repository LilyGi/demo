'''
本程序运行后会有一只小鸟向前飞
安装模块 pip install sprites
'''
# 从精灵模块导入所有命令
from sprites import *
# 新建角色，造型序列为images
images = 'res/bird1.png','res/bird2.png','res/bird3.png'
# 新建角色
bird = Sprite(shape=images)
# 设置旋转模式为左右翻转
bird.rotatemode(1)
# 播放鸟煽动翅膀飞过
bird.play('鸟煽动翅膀飞过.wav')
# 当成立时（重复执行）
while True:
    # 前进9
    bird.fd(21)
    # 下一个造型
    bird.nextcostume()
    # 碰到边缘就反弹
    bird.bounce_on_edge()
    # 等待0.3秒
    bird.wait(0.3)