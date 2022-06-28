from sprites import *
# 新建虫子精灵
bug = Sprite()
# 绘画延时为10毫秒
bug.screen.delay(99)
# 画笔尺寸
bug.pensize(12)
# 画笔颜色
# 宝蓝
bug.color('dodger blue')
# 落笔
bug.pendown()
# 重复4次
for _ in range(4):
    # 前进100
    bug.fd(100)
    # 右转90
    bug.rt(90)
# 抬笔
bug.penup()