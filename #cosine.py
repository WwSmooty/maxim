#cosine.py
#!/usr/bin/env python3

#by calderon.gaona.mariaconcepcion@gmail.com
#GNU/GPL License
#Plotting cosine fuction
# y=f(x)
# x=[0,2pi]

import math # Es una Biblioteca
def f(x): 
    y=math.cos(0)
    return y


N=1000 #n de saltos
A=0 #inicio de rango
B=200 #fin de rango

dx=(B-A)/N #largo del salto
values=range(N+1) #n saltos+1
x=A
for jump in values:
    x= A+jump * dx
    y=f(x)
    print(x,y)
