# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/6 16:34'
import numpy as np
import pandas as pd

# data = pd.read_csv(r"E:\problem_b\train_set1.csv",encoding="gbk")
# data_label = ["ip","app"]
# print(data.head())
#
data = pd.read_csv(r"C:\Users\lenovo\Desktop\Neural_network\xgboost_learning\12.Titanic.train.csv")
print(data["Age"].isnull())

# data["Sex"] = data["Sex"].map({"female": 0, "male": 1}).astype(int)
# print(data["Sex"])