# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/5 19:42'
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
# 导入数据
city = loadmat("citys_data.mat")["citys"]
# 计算城市之间的相互距离
n = city.shape[0]
D = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i != j:
            D[i,j] = np.sqrt(np.sum((city[i,:]-city[j,:])**2))
        else:
            D[i,j] = 1e-4
# 初始化参数
m = 50 # 蚂蚁数量
alpha = 1 # 信息素重要程度因子
beta = 5 # 启发函数重要程度因子
rho = 0.1 # 信息素挥发因子
Q = 1 # 常系数
Eta = 1 / D # 启发函数
Tau = np.ones((n,n)) # 信息素矩阵
Table = np.zeros((m,n)) # 路径记录表
iter = 0 # 迭代次数初值
iter_max = 10 # 最大的迭代次数
Route_best = np.zeros((iter_max,n)) # 最佳路径
Length_best = np.zeros((iter_max,1),dtype=np.float) # 各代最佳路径的长度
Length_ave = np.zeros((iter_max,1)) # 各代路径的平均长度

# 迭代寻找最佳路径
while iter < iter_max:
    # 随机产生各个蚂蚁的起点城市
    start = np.zeros((m,1))
    for i in range(m):
        start[i,:] = np.random.choice(n)
    Table[:,0] = start[:,0]

    # 逐个蚂蚁路径选择
    for i in range(m):
        for j in range(1,n):
            city_index = set(np.arange(n))
            tabu = set(Table[i,0:j]) # 已经访问的城市的集合
            # allow_index = np.where(city_index!=tabu)[0]
            allow_index = list(city_index.difference(tabu))
            tabu = list(tabu)
            city_index = np.array(list(city_index))
            allow = city_index[allow_index]
            P = allow.copy()
            # 计算城市间转移概
            p = np.array([0.0 for _ in range(len(allow))])
            for k in range(len(allow)):
                p[k] = (Tau[int(tabu[-1]),allow[k]]**alpha) * (Eta[int(tabu[-1]),allow[k]]**beta)
            p = p / np.sum(p)
            # 采用轮盘赌法选择下一个访问城市
            Pc = np.cumsum(p)
            target_index = np.where(Pc >= np.random.rand())[0]
            target = allow[target_index[0]]
            Table[i,j] = target
    # 计算各个蚂蚁的路径距离
    Length = np.zeros((m,1))
    for i in range(m):
        Route = Table[i,:]
        for j in range(n-1):
            Length[i,:] = Length[i,:] + D[int(Route[j]),int(Route[j+1])]
        Length[i,:] = Length[i,:] + D[int(Route[n-1]),int(Route[0])]
    # 计算最短路径距离以及平均距离
    if iter==0:
        min_index = np.argmin(Length)
        min_Length = Length[min_index,0]
        Length_best[iter,0] = min_Length
        Length_ave[iter,0] = np.mean(Length)
        Route_best[iter,:] = Table[min_index,:]
    else:
        min_index = np.argmin(Length)
        min_Length = Length[min_index, 0]
        Length_best[iter,0] = min(Length_best[iter-1,0],min_Length)
        Length_ave[iter,0] = np.mean(Length)
        if Length_best[iter,0] == min_Length:
            Route_best[iter,:] = Table[min_index,:]
        else:
            Route_best[iter,:] = Route_best[iter-1,:]
    # 更新信息素
    Delta_Tau = np.zeros((n,n))
    # 诸葛蚂蚁计算
    for i in range(m):
        for j in range(n-1):
            Delta_Tau[int(Table[i,j]),int(Table[i,j+1])] = Delta_Tau[int(Table[i,j]),int(Table[i,j+1])] + Q / Length[i,0]
        Delta_Tau[int(Table[i,n-1]),int(Table[i,0])] = Delta_Tau[int(Table[i,n-1]),int(Table[i,0])] + Q / Length[i,0]
    Tau = (1- rho) * Tau + Delta_Tau
    # 迭代次数增加
    iter += 1
    Table = np.zeros((m,n))

# 结果显示
index = np.argmin(Length_best)
Shortest_Length = Length_best[index,0]
Shortest_Route = Route_best[index,:]
print("最短距离：",Shortest_Length)
print("最短路径: ",Shortest_Route,Shortest_Route[0])

# 绘图
