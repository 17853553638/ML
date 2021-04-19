import pandas as pd
import numpy as np
import csv
data=pd.read_csv("Intent和四大组件删除特征和为1与质心的欧式距离相似度.csv",header=None)
X=data.values[:,0:]
h_zuobiao=X.shape[0]
z_zuobiao=X.shape[1]
dataMat=np.zeros(X.shape)
print (h_zuobiao,z_zuobiao)
for i in range(h_zuobiao):
    for j in range(z_zuobiao):
        if(X[i][j]>0.5):
            dataMat[i][j]=1
        else:
            dataMat[i][j]=0
print (dataMat.shape)
np.savetxt('Intent和四大组件删除特征和为1与质心的欧式距离相似度转换01.txt', dataMat, fmt='%f', delimiter='\t')
fh = open(r'Intent和四大组件删除特征和为1与质心的欧式距离相似度转换01.csv', "w+", newline='')
writer = csv.writer(fh)
data = open(r'Intent和四大组件删除特征和为1与质心的欧式距离相似度转换01.txt')
res = []
for i in data:
    d = [x for x in i.strip().split('\t')]
    # print(d)
    res.append(d)
# print(res)
writer.writerows(res)
data.close()
fh.close()
