# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/6 16:34'
import numpy as np
import pandas as pd
import datetime
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns

# 设置显示图的大小
sns.set(rc={"figure.figsize":(12,5)})
plt.figure(figsize=(12,5))


# 导入数据
train = pd.read_csv(r"E:\problem_b\train_set2.csv",nrows=10000000)
test = pd.read_csv(r"E:\problem_b\test_set.csv")

variables = ["ip","app","device","os","channel"]
for v in variables:
    train[v] = train[v].astype("category")
    test[v] = test[v].astype("category")

train["click_time"] = pd.to_datetime(train["click_time"])
train["attributed_time"] = pd.to_datetime(train["attributed_time"])
test["click_time"] = pd.to_datetime(test["click_time"])

train["is_attributed"] = train["is_attributed"].astype("category")

# 绘图 探索各个特征直接的数量大小关系
# plt.figure(figsize=(10,6))
# cols = ["ip","app","device","os","channel"]
# uniques = [len(train[col].unique()) for col in cols]
# sns.set(font_scale=1.2)
# ax = sns.barplot(cols,uniques,log=True)
# ax.set(xlabel="Feature",ylabel="log(unique count)",title="Number of unique values per feature(from 10,000,000 samples)")
# for p,uniq in zip(ax.patches,uniques):
#     height = p.get_height()
#     ax.text(p.get_x() + p.get_width()/2,height+10,uniq,ha="center")
#
# plt.show()
test["click_id"] = test["click_id"].astype("category")

# 绘图 探索
# plt.figure(figsize=(6,6))
# mean = (train.is_attributed.values == 1).mean()
# ax = sns.barplot(["App Downloaded(1)","Not Downloaded(0)"],[mean,1-mean])
# ax.set(ylabel="Proportion",title="App Downloaded vs Not Downloaded")
# for p,uniq in zip(ax.patches,[mean,1-mean]):
#     height = p.get_height()
#     ax.text(p.get_x() + p.get_width()/2,height+0.01,'{}%'.format(round(uniq * 100, 2)),
#             ha="center")
# plt.show()

temp = train["ip"].value_counts().reset_index(name="counts")
temp.columns = ["ip","counts"]
train = train.merge(temp,on="ip",how="left")
train["is_attributed"] = train["is_attributed"].astype(int)


# 以ip为参照进行探索
# proportion = train[["ip","is_attributed"]].groupby("ip",as_index=False).mean().sort_values("is_attributed",ascending=False)
# counts = train[["ip","is_attributed"]].groupby("ip",as_index=False).count().sort_values("is_attributed",ascending=False)
# merge = counts.merge(proportion,on="ip",how="left")
# merge.columns = ["ip","click_count","prop_downloaded"]
# ax = merge[:300].plot(secondary_y="prop_downloaded")
# plt.title("Conversion Rates over Counts of 300 Most Popular IPs")
# ax.set(ylabel="Count of clicks")
# plt.ylabel("Proportion Downloaded")
# plt.show()
#
# print("Conversion Rates over Counts of Most Popular IPs")
# print(merge[:20])

# 以app为参照进行探索
# proportion = train[["app","is_attributed"]].groupby("app",as_index=False).mean().sort_values("is_attributed",ascending=False)
# counts = train[["app","is_attributed"]].groupby("app",as_index=False).count().sort_values("is_attributed",ascending=False)
# merge = counts.merge(proportion,on="app",how="left")
# merge.columns = ["app","click_count","prop_downloaded"]
# ax = merge[:100].plot(secondary_y='prop_downloaded')
# plt.title('Conversion Rates over Counts of 100 Most Popular Apps')
# ax.set(ylabel='Count of clicks')
# plt.ylabel('Proportion Downloaded')
# plt.show()
#
# print('Counversion Rates over Counts of Most Popular Apps')
# print(merge[:20])

train_smp = pd.read_csv(r"E:\problem_b\train_set1.csv")
# print(train_smp.head(7))

train_smp["click_time"] = pd.to_datetime(train_smp["click_time"])
train_smp["attributed_time"] = pd.to_datetime(train_smp["attributed_time"])

# round the time to nearest hour
# train_smp["click_rnd"] = train_smp["click_time"].dt.round("H")
# train_smp[["click_rnd","is_attributed"]].groupby(["click_rnd"],as_index=True).count().plot()
# plt.title("HOURLY CLICK FREQUENCY")
# plt.ylabel("Number of Clicks")
#
# train_smp[["click_rnd","is_attributed"]].groupby(["click_rnd"],as_index=True).mean().plot()
# plt.title("HOURLY CONVERSION RATIO")
# plt.ylabel("Converted Ratio")
# plt.show()

train_smp["click_hour"] = train_smp["click_time"].dt.hour

train_smp["timePass"] = train_smp["attributed_time"] - train_smp["click_time"]

train["timePass"] = train["attributed_time"] - train["click_time"]









