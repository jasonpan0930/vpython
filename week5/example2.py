from vpython import *  #引用套件Vpython

G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24    #地球質量
m = 1000    #衛星質量
Re = 6.4*10**6  #地球半徑
r = 5*Re  #衛星軌道半徑
t = 0   
dt = 1
v0 = sqrt(G*M/r)   #衛星繞行速率   

def F_g(x):                                 #定義萬有引力公式
    return -G*M*m/(mag(x)**3)*x

scene = canvas(width=600, height=600, center=vec(1.6*Re,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(r,0,0), v = vec (0,0.7*v0,0), a = vec(0,0,0),radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星


while True:  #執行無窮迴圈
    rate(5000)
    
    mater.a = F_g(mater.pos-earth.pos)/m
    mater.v += mater.a*dt   
    mater.pos += mater.v*dt  
    
    if mater.v.x > 0 and mater.v.x + mater.a.x*dt < 0:
        print ('simulated period = ',t, ', theoretical period = ', 2*pi*sqrt(r**3/G/M))
        t = 0

    t += dt