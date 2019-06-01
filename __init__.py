import math# import sin
import matplotlib.pyplot as plt

def proizv(f,point,accurancy):
    point_old=point
    fp=f(point)
    point+=1
    arr=[]
    for i in range(100):
        arr.append([f(point)-fp,point-point_old])
        point=(point+point_old)/2
    new_arr=[]
    for df,dx in arr:
        if not df==0 and not dx==0:
            new_arr.append(df/dx)
    print(arr)
    i=1
    while i<99 and abs(new_arr[i]-new_arr[i-1])>accurancy:
        i+=1
    print(new_arr)

    return new_arr[i]

accur=0.00001
f = lambda x:math.log(x,math.e)
pr=lambda x: proizv(f,x,accur)

x_from=0.1
x_to=10
x_step=0.1

x_arr=[]
while x_from<x_to:
    x_arr.append(x_from)
    x_from+=x_step
f_y_arr=[]
for i in x_arr:
    f_y_arr.append(f(i))
f_ypr_arr=[]
for i in x_arr:
    f_ypr_arr.append(pr(i))

plt.plot(x_arr,f_y_arr)
plt.plot(x_arr,f_ypr_arr)
plt.show()

print(pr(3.5))
