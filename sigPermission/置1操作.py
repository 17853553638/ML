import pandas as pd
import numpy as np
from numpy import delete
import re
if __name__ == '__main__':
    fileName = "22个权限的新数据集.csv"
    # fileName1="E:\机器学习\数据\查看二次汇总的特征副本.csv"
    data = pd.read_csv(fileName,header=None) # 如果数据间是标准化格式用“\t”,否则用"\s+"
    # data1=pd.read_csv(fileName1,header=None)
    array = data.values
    # array1=data1.values
    dataInfo = data.shape[1]
    # dataInfo1=data1.shape[1]
    # X1= array1[:, 1:dataInfo1]
    X = array[:, 1:dataInfo]
    col = np.shape(X)[0]
    row = np.shape(X)[1]
    for i in range(col):
        for j in range(row):
            if X[i][j]!=0:
                X[i][j]=1
    # np.savetxt('置1.txt', X, fmt='%d', delimiter='\t')
    print (col,row)
    # print(type(fileArray[0]))
    data2=[]
    sum = 0
    for w in range(row):
        for v in range(col):
            sum += X[v][w]
        print (sum)
        if sum <0:
            data2.append(w)
            # print (data1)
        sum=0
    # X = np.delete(X, data2, 1)
    # X1=np.delete(X1,data2,1)
    np.savetxt('置1后22个权限的新数据集.txt', X, fmt='%d', delimiter='\t')
    # np.savetxt('不置1权限1筛选后的二次汇总.txt', X1, fmt='%d', delimiter='\t')

