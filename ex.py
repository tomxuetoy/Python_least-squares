# -*- coding: utf-8 -*-

import math
from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)               # 1*1 grid, and the first subplot
x = [1.1,2.1212,3.23,5.3434,8.12]       # the raw data
y = [2.34,4.32323,8.323,12.3434,18.02]
ax.loglog(x,y,"bo")                     # plot x and y using blue circle markers

lnx = [math.log(f,math.e) for f in x]   # 对x进行对数转换, e为底 
lny = [math.log(f,math.e) for f in y]   # 对y进行对数转换, e为底

a = np.mat([lnx,[1]*len(x)]).T          # 自变量矩阵a
b = np.mat(lny).T                       # 因变量矩阵b
print "a=" 
print a
print "b="
print b

(t,res,rank,s) = linalg.lstsq(a,b)      # Return the least-squares solution to a linear matrix equation
print "t="
print t 

r = t[0][0]
c = t[1][0]

x_ = x
y_ = [math.e**(r*a+c) for a in lnx]    # 根据求得的系数求出y
ax.loglog(x_,y_,"r-")                  # 绘制拟合的曲线图, "r-" mean red and solid line style

plt.show()
