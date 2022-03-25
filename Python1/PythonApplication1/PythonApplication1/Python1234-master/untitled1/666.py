#调用自定义函数，在tkinter上画图
import turtle
import tkinter as tk
#调用自定义函数：Pythonone文件夹,turtleDraw文件，ttd别名
import PythonOne.turtleDraw as ttd
root = tk.Tk()#创建窗口
root.title("在tkinter上画图：04组--李培")
#宽度;900,高度：520，x坐标：700，y坐标：200
root.geometry("900x520+700+200")
#添加控件：pack（）布局方式
tk.Label(root,text="单击按钮，在画布上画图",bg="lightgray",fg="blue",
         font=('微软雅黑',16,'bold'),width=54,height=2).pack()
#1.创建画布
canva = tk.Canvas(root,width=820,height=400)
#2.为画布布局：将其排列在tkinter窗口上
canva.pack()#按顺序布局
#3.创建turtle的画布，使其与canva关联
theScreen = turtle.TurtleScreen(canva)
#4.在创建的画布上定义绘图笔
pen = turtle.RawTurtle(theScreen)
def drawCanvaZB():
    ttd.drawZB(pen,300,200)
def drawImg():
    ttd.drawFlower(pen,-300,-100)
    ttd.drawStar(pen,260,-80)
def exitTk():
    root.destroy()
#创建按钮:用command定义函数，单击按钮执行，注意，如果函数加括号，则自动执行
btn1 = tk.Button(root,text="单击画坐标",font=('微软雅黑',12),
               bg="lightblue",fg="red",padx=10,pady=5,command=drawCanvaZB)
btn1.place(x=38,y=470)
#如果函数需要传参数，必然加括号，则需要用lambda定义为匿名函数，则不自动执行
btn2 = tk.Button(root,text="单击写文字",font=('微软雅黑',12),
               bg="lightblue",fg="red",padx=10,pady=5,
               command=(lambda:ttd.writeFont(pen,-400,100)))
btn2.place(x=200,y=470)
btn3 = tk.Button(root,text="单击绘小图",font=('微软雅黑',12),
               bg="lightblue",fg="red",padx=10,pady=5,
               command=drawImg)
btn3.place(x=350,y=470)
btnQ = tk.Button(root,text="退出",font=('微软雅黑',12),
               bg="lightblue",fg="red",padx=10,pady=5,command=exitTk)
btnQ.place(x=500,y=470)
# 启动消息循环，保证界面窗口呈现
root.mainloop()
