import pandas as pd
import numpy as np
import csv
data=pd.read_csv("归一化Intent和四大组件删除特征和为1与质心的欧式距离.csv",header=None)
X=data.values[:,0:]
h_zuobiao=X.shape[0]
z_zuobiao=X.shape[1]
dataMat=np.zeros(X.shape)
print (h_zuobiao,z_zuobiao)
for i in range(h_zuobiao):
    for j in range(z_zuobiao):
            dataMat[i][j]=X[i][j]/(187.08494-2.3077662)
print (dataMat.shape)
np.savetxt('Intent和四大组件删除特征和为1与质心的欧式距离相似度.txt', dataMat, fmt='%f', delimiter='\t')
fh = open(r'Intent和四大组件删除特征和为1与质心的欧式距离相似度.csv', "w+", newline='')
writer = csv.writer(fh)
data = open(r'Intent和四大组件删除特征和为1与质心的欧式距离相似度.txt')
res = []
for i in data:
    d = [x for x in i.strip().split('\t')]
    # print(d)
    res.append(d)
# print(res)
writer.writerows(res)
data.close()
fh.close()
