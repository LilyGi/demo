from sprites import *
# 新建屏幕
screen = Screen()
# 设置背景颜色
screen.bgcolor('dodger blue')
# 设置标题
screen.title('旋转的文字')

# 新建不可见的角色
t = Sprite(visible=False)
# 设置角色为白色
t.color('pink')
# a是一个全局变量，这里代表角度
a = 0
# 要旋转的文字
info = '小可爱要天天开心哦！'
# 定义字体样式
ft = ('黑体', 27, 'normal')
def rotate():
    # 申明a为全局变量
    global a
    # 清除以前所写的内容
    t.clear()

    t.write(info, align='center', font=ft, angle=a)
    a = a + 15
    screen.ontimer(rotate, 60)
rotate()

screen.mainloop()