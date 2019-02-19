# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:48:24 2018

@author: Vova
"""

import time
def c_to_f(c):
    return c*9/5 + 32

#t0=time.clock()
#c_to_f(1000)
#t1=time.clock() -t0
#print("t=",t0,":",t1,"s,")


def mysum(x):
    total =0
    for i in range(x+1):
        total+=1
    return total
s=mysum(3)
#print(s)


def if_e_in_L(L,e):
    for i in L:
        if i == e:
            return True
    else:
        return False



#for i in range(5):
#    print("A")
#for i in range(4):
#    print("B")
        
    
for i in range(3):
    for s in range(3):
        print("a")
