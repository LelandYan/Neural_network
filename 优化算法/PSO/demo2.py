# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/3 14:08'
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fun(x, y):
    return x ** 2 + y ** 2 - 10 * np.cos(2 * np.pi * x) - 10 * np.cos(2 * np.pi * y) + 20


# 绘制目标函数的曲线图
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x, y)
z = fun(x, y)
fig = plt.figure()  # 定义新的三维坐标轴
ax3 = plt.axes(projection='3d')
ax3.plot_surface(x, y, z,cmap='rainbow')
# plt.show()
########################

# 参数的初始化
c1 = 1.49445
c2 = 1.49445

max_gen = 5 # 进化次数
size_pop = 20 # 种群规模

# 速度范围
V_max = 1
V_min = -1

pop_max = 5
pop_min = -5




pop = np.zeros((size_pop, 2),dtype=np.float)
V = np.zeros((size_pop, 2))
fitness = np.zeros(size_pop)
# 产生初始粒子和速度
for i in range(size_pop):
    # 随机产生一个种群
    pop[i, :] = np.random.rand(1,2)*5  # 初始化种群
    V[i, :] = np.random.rand(1,2) # 初始化速度
    fitness[i] = fun(pop[i,0],pop[i,1]) # 计算适应度

# 个体极值和群体极值
best_index = np.argmax(fitness)
best_fitness = fitness[best_index]
z_best = pop[best_index,:].copy() # 全局最佳
g_best = pop # 个体最佳
fitness_g_best = fitness # 个体最佳适应度值
fitness_z_best = best_fitness # 全局最佳适应度值
yy = np.zeros(max_gen)
# 迭代寻优
for i in range(max_gen):
    for j in range(size_pop):
        # 速度更新
        V[j,:] = V[j,:] + c1 * np.random.rand()*(g_best[j,:] - pop[j,:]) + c2 * np.random.rand() * (z_best - pop[j,:])
        V[j,np.where(V[j,:]>V_max)] = V_max
        V[j,np.where(V[j,:]<V_min)] = V_min
        # 种群更新
        pop[j,:] = pop[j,:] + V[j,:]
        pop[j,np.where(pop[j,:] > pop_max)] = pop_max
        pop[j,np.where(pop[j,:] < pop_min)] = pop_min
        # 适应度跟新
        fitness[j] = fun(pop[j,0],pop[j,1])
    for j in range(size_pop):
        # 个体最优更新
        if fitness[j] > fitness_g_best[j]:
            g_best[j,:] = pop[j,:]
            fitness_g_best[j] = fitness[j]

        # 群体最优更新
        if fitness[j] > fitness_z_best:
            z_best = pop[j,:].copy()
            fitness_z_best = fitness[j].copy()
    # print("AAA",z_best, fitness_z_best)
    yy[i] = fitness_z_best
print(z_best, fitness_z_best)
# plt.plot(z_best,fitness_z_best,"r*")
# plt.show()
#
plt.figure()
plt.plot(np.arange(len(yy)),yy)
plt.show()
