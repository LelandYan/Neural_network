# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/3 14:08'
import numpy as np
import matplotlib.pyplot as plt

# 绘制目标函数的曲线图
x = np.arange(1, 2, 0.01)
y = np.sin(10 * np.pi * x) / x
plt.figure()
plt.plot(x,y)
plt.grid()
plt.show()
########################

# 参数的初始化
c1 = 1.49445
c2 = 1.49445

max_gen = 50
size_pop = 10

# 速度范围
V_max = 0.5
V_min = -0.5

pop_max = 2
pop_min = 1

pop = np.zeros((size_pop,1))
V = np.zeros((size_pop,1))
# 产生初始粒子和速度
for i in range(size_pop):
    # 随机产生一个种群
    pop[i,:] = (np.random.rand(1) + 1) / 2 + 1
    V[i,:] = 0.5 * np.random.rand(1)
    