import numpy as np
import matplotlib.pyplot as plt
from math import sin


X=np.linspace(-np.pi,np.pi,500)
Signal=(16383*np.sin(X))
A=[16382]*500
B=[0]*500
D=[8192]*500
C=A+D+B+D

"""A=[16382 , 16382 , 16382 , 16382 ,
16382 , 16382 , 16382 , 16382 , 16382 , 16382 ,
16382 , 16382 , 16382 , 16382 , 16382 , 16382 ,
16382 , 16382 , 16382 , 16382 , 16382 , 16382 ,
16382 , 16382 , 16382 , 16382 , 16382 , 8192,
8192 ,8192 , 2 , 2 , 2 , 2 , 2 , 2 , 2,
 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 ,
 2 , 2 , 2 , 2 , 2 , 2 , 2 , 8192 ,8192 ,8192  ]"""
a=0
for i in C :
    print("{},".format(i),end='')
    if(a==100):
        print("")
        a=0
    a=a+1
#print(C)
#print(len(C))


#plt.plot(X,Signal,'ro')
plt.plot(C)

#print(Signal)
plt.show()