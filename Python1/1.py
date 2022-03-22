
import turtle as t
import time
import random
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
    #画向左的箭头
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
    t.stamp()
def writeFont():
    t.penup()
    t.goto(-300,200)
    #不落笔不划线
    #t.pendown()
    #循环，i是从1到6
    t.hideturtle()
    for i in range(6):
     #seth是相对于x右轴的角度
       t.seth(0)
       t.write("当",font=("华文彩云",20+3*i,"bold"))
       t.forward(25+5*i)
       time.sleep(0.1)
    t.forward(10)
    t.write("!",font=("微雅软黑",40,"bold"))
    t.forward(20)
    #定义列表，相当于数组
    words=['送','给','02','组','黄','子','硕']
    for word in words:
        t.write(word,font=("微雅软黑",30,"bold"))
        t.forward(50)
        time.sleep(0.1)

#画同心圆
def drawCircle():
  #先画大圆后画小圆
  #设置使用rgb模式的颜色
  t.colormode(255)
  for i in range(12,0,-2):
    r=random.randint(100,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    t.color([r,g,b])
    t.penup()
    t.goto(0,-i*i)
    t.pendown()
    t.begin_fill()
    t.circle(i*i)
    t.end_fill()
    time.sleep(0.2)


#画小方块
def drawF():
  t.penup()
  he=300
  shu=-250
  t.goto(he,shu)
  t.pendown()
  t.begin_fill()
  t.color('blue','blue')
  t.goto(he+50,shu)
  t.goto(he+50,shu+50)
  t.goto(he,shu+50)
  t.goto(he,shu)
  t.end_fill()
  t.begin_fill()
  t.color('black','black')
  t.goto(he,shu+50)
  t.goto(he+50,shu)
  t.goto(he,shu)
  t.end_fill()
  time.sleep(0.2)

#画小方块
def drawF1():
  t.penup()
  he=250
  shu=-200
  t.goto(he,shu)
  t.pendown()
  t.begin_fill()
  t.color('red','red')
  t.goto(he+50,shu)
  t.goto(he+50,shu+50)
  t.goto(he,shu+50)
  t.goto(he,shu)
  t.end_fill()
  t.begin_fill()
  t.color('black','black')
  t.goto(he,shu+50)
  t.goto(he+50,shu)
  t.goto(he,shu)
  t.end_fill()
  time.sleep(0.2)

#定义主函数
def main():
   # 设置窗口大小和位置，大小800*600，左上角坐标：x方向100，y方向50
   t.setup(800, 600, 500, 50)
   t.screensize(780, 580, "lightblue")
   # 设置标题栏文字
   t.title("画大白，02组：黄子硕")
   drawZB()
   writeFont()
   drawCircle()
   drawZB()
   drawF()
   drawF1()
   t.mainloop()



#如果本程序是主入口，则执行以下代码
if __name__=="__main__":
    main()
