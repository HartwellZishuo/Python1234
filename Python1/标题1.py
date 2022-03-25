import tkinter as tk
import turtle as t
import tkinter.ttk as ttk
#导入自定义函数
#import PythonOne.turtleDraw as ttd
import random

class Win:
    #构造函数，实例化时会自动执行
    def __init__(self,r):
        self.root=r
        #设置窗口大小和位置
        self.root.geometry("900x520+500+300")
        #设置窗口的标题
        self.root.title("在tkinter上画图：02组--黄子硕")
        #self.root.iconbitmap("img/edit.ico")
        #定义类变量
        self.fen=tk.StringVar()#字符型数据
        self.fen.set('80')#设置默认值是80
        self.grade=tk.StringVar()
        self.grade.set("等级：未知")

        self.creat_page()
    def creat_page(self):
        tk.Label(self.root,text="单击测试成绩等级",bg="lightgray",
                 fg="blue",font=('微软雅黑',16),width=60,height=2).pack()
        self.canva=tk.Canvas(self.root,width=780,height=260)
        self.canva.pack()
        self.screen = t.TurtleScreen(self.canva)
        self.pen = t.RawTurtle(self.screen)
        self.pen.color("pink")

        #创建输入框，按钮
        tk.Label(self.root,text="请输入分数：",font=("宋体",16)).place(x=60,y=360)
        #textvariable=self.fen:将输入框与类的变量相关联
        self.score=tk.Entry(self.root,width=30,font=("宋体",16),textvariable=self.fen)
        self.score.place(x=200,y=360)

        #按钮
        self.bnt1=ttk.Button(self.root,text="单击判断结果",width=26,
                             command=self.checkFen)
        self.bnt1.place(x=60,y=420)

        self.bnt2 = ttk.Button(self.root, text="随机结果判断", width=26,
                               command=self.randSorce)
        self.bnt2.place(x=260, y=420)

        self.bnt3 = ttk.Button(self.root, text="退出", width=26,
                               command=self.exitTk)
        self.bnt3.place(x=460, y=420)

        #等级
        tk.Label(self.root,text="等级：未知",font=("宋体",16),textvariable=self.grade).place(x=60,y=480)

    def checkFen(self):
        #复位
        self.pen.reset()
        self.pen.color("pink")
        #获取文本框的值，将字符型转换成浮点型
        nowScore=float(self.score.get())
        if(nowScore>=85):
            scoreGrade="等级：优秀"
        elif (nowScore >=70):
            scoreGrade = "等级：良好"
        elif (nowScore >=60):
            scoreGrade = "等级：及格"
        else:
            scoreGrade = "等级：不及格"
        self.grade.set(scoreGrade)
        #调用写字函数
        self.writeName()
        self.drawResult()
    def writeName(self):
        #ttd.writeFont(self.pen,-395,30)
        self.pen.penup()
        self.pen.color("red")
        self.pen.goto(-100,-20)
        self.pen.write(self.grade.get(),font=("华文彩云",30,'bold'))
    def drawResult(self):
        self.pen.penup()
        #获得文本框的值，并判断
        if(float(self.score.get())>=60):
            self.pen.goto(100,-20)
            self.pen.pendown()
            self.pen.seth(-45)
            self.pen.forward(90)
            self.pen.seth(60)
            self.pen.forward(200)
        else:
            self.pen.goto(300,10)
            self.pen.seth(225)
            self.pen.pendown()
            self.pen.forward(150)
            self.pen.penup()
            self.pen.goto(200,10)
            self.pen.seth(-45)
            self.pen.pendown()
            self.pen.forward(150)
        self.pen.hideturtle()
    def randSorce(self):
        randFen=random.randint(40,100)
        #self.fen.set(randFen)
        #1.删除输入框内容
        self.score.delete(0,tk.END)
        #2.为文本框插入内容
        self.score.insert('insert',randFen)
        self.checkFen()
    def exitTk(self):
        self.root.destroy()
#本程序是入口
if __name__ == "__main__":

    root=tk.Tk()
    #类的实例化
    Win(root)

    root.mainloop()
