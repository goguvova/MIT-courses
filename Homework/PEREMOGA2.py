# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:27:30 2018

@author: Vova
"""
"""
for n in range(5):
    print(n)

n=0
while n < 5:
    print(n)
    n+=1
"""
"""
import math
ans = 0
neg_flag = False
x = float(input("Enter an integer: "))
if x < 0:
    neg_flag = True
    
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print("Square root of", x, "is", math.sqrt(x))
    if neg_flag==True:
      print("Just checking... did you mean", -x, "?")
"""
import math
ans = 0
x= float(input("Enter an integer: "))
if x < 0:
     print("Just checking... did you mean", -x, "?")
else:
     print("Square root of", x, "is", math.sqrt(x))