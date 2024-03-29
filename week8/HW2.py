from vpython import *    #Web Vpython 3.2

A = 1.0
N = 100
omega = 2*pi/1.0   #振動角頻率
size = 0.1         #介質的大小
m = 0.1            #介質的質量
k = 400.0          #每一小段彈簧的彈力常數
d = 0.4            #介質之間的初始間隔
     
scene = canvas(title='Spring Wave', width=1200, height=300, center = vector((N-1)*d/2, 0, 0)) 

ball =[]
for i in range(N):
    ball.append(sphere(radius=size, color=color.yellow, pos=vec(i*d, 0, 0), v=vec(0,0,0)))# 將sphere(radius=size, color=color.yellow, pos=vec(i*d, 0, 0), v=vec(0,0,0))放入list中

spring = []
for i in range(N-1):
    spring.append(helix(radius = size/2.0, thickness = d/15.0, pos=vec(i*d, 0, 0), axis=vec(d,0,0)))#將helix(radius = size/2.0, thickness = d/15.0, pos=vec(i*d, 0, 0), axis=vec(d,0,0))放入list中

def SpringForce(r):    #彈力
    return  k*(mag(r)-0.5*d)*r/mag(r)
      
t, dt = 0, 0.001       #初始時間，時間差
while True:
    rate(1000)
    t += dt
    
    if t <= pi/omega:
        ball[0].pos = vector( 0 , A*sin(omega*t) , 0)    ##強迫第一個球沿y方向振動
    
    #在每次迴圈中調整彈簧位置與長度
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos-ball[i].pos

    #計算每一個球受相鄰兩條彈簧的彈力所造成的加速度
    for i in range(1,N):      
        if i != N-1: 
            ball[i].v += (SpringForce(spring[i].axis)-SpringForce(spring[i-1].axis))/m*dt#非最後且非第一個的球受相鄰兩條彈簧的彈力所造成的加速度

        ball[i].pos += ball[i].v*dt