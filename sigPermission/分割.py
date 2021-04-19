import csv
fh = open(r'E:\机器学习\SigPermission\良性权限数据集.csv',"w+",newline='')
writer = csv.writer(fh)
data = open(r'E:\机器学习\SigPermission\良性权限数据集.txt')
res = []
for i in data:
    d = [x for x in i.strip().split('\t')]
    # print(d)
    res.append(d)
print(res)
writer.writerows(res)
data.close()
fh.close()
