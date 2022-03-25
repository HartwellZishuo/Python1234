import turtle as  t
import time
import random
#定义函数，画坐标
def drawZB():
    t.penup()
    #移动笔,画原点
    t.color("red")#设置颜色
    t.goto(0,-5)
    t.pendown()
    t.begin_fill()#开始填充
    t.circle(5)
    t.end_fill()#结束填充
    t.color("black")
    #画向右的x轴，回到原点
    t.penup()
    t.goto(0,0)
    t.pendown()
    #向右移动300
    t.goto(300,0)
    #画箭头
    t.stamp()
    #画向上的y轴
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.goto(0,200)
    #画箭头
    t.stamp()
    #画向左的x轴，回到原点
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    #向左移动300
    t.goto(-300,0)
    #画箭头
    t.stamp()
    #画向下的y轴
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.goto(0,-200)
    #画箭头
    t.stamp()
#写文字
def writeFont():
    t.penup()
    t.goto(-300,200)
    #t.pendown() #不落笔，就不划线
    #写的文字是“当”，字体：华文彩云，字号：30，加粗
    #循环，i是从1到6
    t.hideturtle() #隐藏海龟
    for i in range(6):
        #seth是相对于x右轴的角度
        t.seth(0)
        t.write("当",font=("华文彩云",20+5*i,"bold"))
        t.forward(35+5*i)
        time.sleep(0.1)
    t.forward(25)
    t.write("！", font=("华文彩云",40, "bold"))
    t.forward(40)
    #定义列表，相对于数组
    words=['送','给','0','4','组','胡','洪','波']
   # words=['送','给',0,4,'组','胡','洪','波']
    #遍历列表
    for word in words:
        t.write(word, font=("微软雅黑",30,"bold"))
        #判断Word是数字字符
        try:
            k=int(word)
            t.forward(20)
        except:
            t.forward(40)
        time.sleep(0.1)
        #if(isinstance(word,int)):
        #t.forward(20)
        #else
        #t.forward(45)

#画同心圆
def drawCircle():
    #先画大圆，后画小圆
    #range(15,0,-3):从15开始，到3结束，每次减小3
    #设置使用rgb模式的颜色
    t.colormode(255)
    for i in range(12,0,-2):
        #生成颜色
        r=random.randint(100,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        #设置颜色为三原色组成r，g，b
        t.color([r,g,b])
        t.penup()
        t.goto(0,-i*i)
        t.pendown()
        t.begin_fill()
        t.circle(i*i)
        t.end_fill()
        time.sleep(0.2)
def drawRec():
    t.colormode(255)
    for i in range(12, 0, -3):
         #生成颜色
        r = random.randint(100, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        # 设置颜色为三原色组成r，g，b
        t.color([r, g, b])
        t.penup()
        he=300
        shu=-250
        t.goto(he,shu)
        t.pendown()
        t.begin_fill()
        t.goto(he+50, shu)
        t.goto(he+50, shu+50)
        t.goto(he, shu+50)
        t.goto(he, shu)
        t.end_fill()
        time.sleep(0.2)
        t.color([r, g, b])
        t.goto(he, shu+50)
        t.goto(he+50, shu)
        t.goto(he, shu)
        t.end_fill()
        time.sleep(0.2)
def drawRec2():
    t.colormode(255)
    for i in range(12, 0, -3):
         #生成颜色
        r = random.randint(100, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        # 设置颜色为三原色组成r，g，b
        t.color([r, g, b])
        t.penup()
        he=250
        shu=-200
        t.goto(he,shu)
        t.pendown()
        t.begin_fill()
        t.goto(he+50, shu)
        t.goto(he+50, shu+50)
        t.goto(he, shu+50)
        t.goto(he, shu)
        t.end_fill()
        time.sleep(0.2)
        t.color([r, g, b])
        t.goto(he, shu+50)
        t.goto(he+50, shu)
        t.goto(he, shu)
        t.end_fill()
        time.sleep(0.2)
#画矩形
def drawRect():
    t.penup()
    t.goto(300,-200)
    t.pendown()
    t.seth(0)
    t.color('yellow','red')
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.fillcolor("pink")
    t.left(0)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.end_fill()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.end_fill()