#画坐标
def drawZB(t,x,y):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.speed(5)
    t.pensize(2)
    t.pencolor("blue")
    #向右
    t.goto(x,0)
    #绘制海龟标记
    t.stamp()
    #向上
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.goto(0,y)
    t.stamp()
    #向左
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.goto(-1*x,0)
    t.stamp()
    # 向下
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.goto(0,-1*y)
    t.stamp()
    #画原点
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    #设置填充色
    t.fillcolor("red")
    #开始填充
    t.begin_fill()
    #画半径为10的圆
    t.circle(10)
    #结束填充
    t.end_fill()
    # t.circle(20)

#写文字
def writeFont(t,x,y):
    t.penup()
    t.goto(x,y)
    # t.pendown()
    #设置角度为0，绝对值，针对x轴右方向的角度
    #right和left,是相对值，针对原来的方向
    t.seth(0)
    for i in range(6):
        t.write("当",font=("华文彩云",20+i*5,"bold"))
        t.forward(30+i*5)

    #获取当前坐标x、y  (-85.00,260.00)  x=p[0]  y=p[1]
    p=t.pos()
    print(p)
    t.sety(p[1]-20)  #海龟向下移动20
    t.write("! ", font=("华文彩云", 80, "bold"))
    t.forward(60)
    t.sety(p[1])  # 海龟回到原来的高度
    #送给,定义一个列表，相当于数组
    words = ['送', '给','0', '2','  组', ' ：', '黄', '子','硕']
    for word in words:
        print(word,": %.2f"%(t.pos()[0]))
        t.write(word,font=("微软雅黑",40,"bold"))
        #将当前word转换成整型，如果不是数字，则出现异常，字符前进60
        #不出现异常，说明word是数字，则前进30
        try:
            k=int(word)
            t.forward(30)
        except:
            t.forward(60)

#画太阳花
def drawFlower(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red", "yellow")  # 同时设置画笔颜色，填充颜色
    t.speed(10)
    t.begin_fill()
    for i in range(50):
        t.forward(150)  # 移动200
        t.left(170)  # 改变方向
    t.end_fill()

#画五角星
def drawStar(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","yellow")  # 颜色填充函数
    t.begin_fill()
    k=0
    while True:
        t.forward(150)
        t.right(144)
        k +=1
        if(k>5):
            break
    t.end_fill()