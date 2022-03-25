
import random
a=c=0
k=random.randint(1,2)
if(k==1):
    a=random.randint(80,100)
else:
    a=random.random()*20+80
    print("甲的成绩:",a)
# a=input("请输入甲同学的成绩:")
# print("甲的成绩:",a)
# c=input("请输入丙同学的成绩：“）
if(isinstance(a,int)):
    print("甲的成绩:(整型）:%d"%a)
while True:
    try:
        c=float(input("请输入丙同学的成绩:"))
    except:
        c=random.random()*20+80
    if(a>c):
        break
    else:
        print(f"甲的成绩{a:.2f},丙的成绩{c:.2f}")
        print("丙的成绩，要小于甲的成绩，请重新输入！")
        continue
print("丙的成绩:",c)
b=random.random()*(a-c)+c
print("乙的成绩：{:.2f}".format(b))
print(f"总成绩：{a+b+c:.2f}")
