import pandas as pd
import numpy as np
data=pd.read_csv("Intent和四大组件删除特征和为1与质心的欧式距离相似度.csv",header=None)
X=data.values[:,0:]
h_zuobiao=X.shape[0]
z_zuobiao=X.shape[1]
print (h_zuobiao,z_zuobiao)
for i in range(h_zuobiao):
    for j in range(z_zuobiao-1):
        if(X[i][j]>X[i][j+1]):
            max=X[i][j]
print (max)