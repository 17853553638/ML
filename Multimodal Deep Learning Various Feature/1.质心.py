import numpy as np
import pandas as pd
import csv
from sklearn.preprocessing import MinMaxScaler
def cal_Cmass(data):
#     input:data(ndarray):数据样本
#     output:mass(ndarray):数据样本质心
    Cmass=np.mean(data,axis=0)
    return Cmass
def distance(x, y, p=2):
    # input:x(ndarray):第一个样本的坐标
    #       y(ndarray):第二个样本的坐标
    #       p(int):等于1时为曼哈顿距离，等于2时为欧氏距离
    # output:distance(float):x到y的距离
    dis2 = np.sum(np.abs(x-y)**p) # 计算
    dis = np.power(dis2,1/p)
    return dis
def sorted_list(data,Cmass):
    # input:data(ndarray):数据样本
    #       Cmass(ndarray):数据样本质心
    # output:dis_list(list):排好序的样本到质心距离
    dis_list = np.zeros(data.shape)
    print (data.shape)
    h_biao=data.shape[0]
    z_biao=data.shape[1]
    print (h_biao,z_biao)
    for i in range(h_biao):  # 遍历data数据，与质心cmass求距离
        for j in range(z_biao):
            dis_list[i][j]=distance(Cmass,data[i][j])
    # dis_list = sorted(dis_list)      # 排序
    return dis_list
data=pd.read_csv("D:/fh/机器学习/服务器上代码/Intent和四大组件的数据集标签删除特征和为1.csv",header=None)
mm=MinMaxScaler()
mm_data=mm.fit_transform(data)

y=mm_data[:,0]
X=mm_data[:,1:]
print (X)
cmass=cal_Cmass(X)
print(cmass)
print (np.shape(cmass))
list=sorted_list(X,cmass)
print (np.shape(list))
# print (list)
np.savetxt('归一化Intent和四大组件删除特征和为1与质心的欧式距离.txt', list, fmt='%f', delimiter='\t')
fh = open(r'归一化Intent和四大组件删除特征和为1与质心的欧式距离.csv', "w+", newline='')
writer = csv.writer(fh)
data = open(r'归一化Intent和四大组件删除特征和为1与质心的欧式距离.txt')
res = []
for i in data:
    d = [x for x in i.strip().split('\t')]
    # print(d)
    res.append(d)
# print(res)
writer.writerows(res)
data.close()
fh.close()