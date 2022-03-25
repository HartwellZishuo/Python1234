import random
print("hellw world!")
#产生（0-100）的随机数
x=random.random()*100
y=random.random()*100
z=random.random()*100
#逗号，默认是空格，用sep设置分隔符号
print(x,y,z,sep=";")
#end:行末符，默认是回车
print(x,end=";")
print(y,end=";")
print(z)
print("x=%.2f"%x)
print("x=%.2f,y=%.2f"%(x,y))
print("x={:.3f},y={:.3f}".format(x,y))
print(f"x={x:.2f},y={y:.3f},z={z:.1f}")
print("测试结束".center(10,"+"))