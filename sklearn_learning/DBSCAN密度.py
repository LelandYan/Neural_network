# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/3 16:27'
import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt

mac2id = dict()
onlinetimes = []
f = open("time.txt",encoding="utf-8")
for line in f:
    mac = line.split(",")[2]
    onlinetime = int(line.split(",")[6])
    starttime = int(line.split(",")[4].split(" ")[1].split(":")[0])
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime,onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime,onlinetime)]
real_X = np.array(onlinetimes).reshape((-1,2))

X = real_X[:,0:1]
db = skc.DBSCAN(eps=0.01,min_samples=20).fit(X)
labels = db.labels_

print("Labels:")
print(labels)
ratio = len(labels[labels[:] == -1]) / len(labels)
print(f"Noise ratio:{ratio}")

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Estimated number of clusters{n_clusters_}")
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

for i in range(n_clusters_):
    print('Cluster ', i, ':')
    print(list(X[labels == i].flatten()))

plt.hist(X, 24)
plt.show()