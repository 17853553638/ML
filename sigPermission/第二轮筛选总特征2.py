import pandas as pd
import numpy as np
import re
import Generating_data_sets
import csv
def change(dataSet, data):
    count1 = len(dataSet)
    count2 = len(data)
    # print(count2)
    # print(np.shape(data))
    # print(dataSet)
    # print(data)
    file = open('result.txt', 'a')
    for i in range(count1):
        temp = dataSet[i] + ':'
        for j in range(count2):
            if dataSet[i] == data[j][0]:
                temp = temp + data[j][1] + ','
        temp += '\n'
        file.writelines(temp)
    file.close()


def createMat(dataSet, data, num):
    count1 = len(dataSet)
    count2 = len(data)
    feature=[]
    feature1=[]
    feature2=[]

    signpermission=['CALL_PHONE','CLEAR_APP_CACHE','REQUEST_INSTALL_PACKAGES','SET_WALLPAPER','CHANGE_NETWORK_STATE','RECEIVE_MMS','ACCESS_COARSE_LOCATION','CHANGE_CONFIGURATION','READ_CONTACTS','WRITE_CONTACTS','WRITE_APN_SETTINGS','READ_CALL_LOG','KILL_BACKGROUND_PROCESSES','MOUNT_UNMOUNT_FILESYSTEMS','PROCESS_OUTGOING_CALLS','BLUETOOTH','WRITE_SYNC_SETTINGS','READ_LOGS','READ_SYNC_SETTINGS','SEND_SMS','BROADCAST_SMS','EXPAND_STATUS_BAR','GET_PACKAGE_SIZE','CHANGE_WIFI_MULTICAST_STATE','ACCESS_FINE_LOCATION','WAKE_LOCK','RESTART_PACKAGES','MODIFY_AUDIO_SETTINGS','WRITE_SECURE_SETTINGS','CHANGE_WIFI_STATE']
    dataMat = np.zeros((num, count1))
    f = open('data总.txt', 'r')
    index = 0
    for line in f.readlines():
        lineArr = line.strip().split('@')
        count3 = len(lineArr)
        dataStr = []
        dataTemp = []
        strings=[]
        # 第一个for读取数据
        for i in range(1, count3):
                tempStr = re.findall('(.+?):', lineArr[i])
                tempNum = re.findall('(\d+)', lineArr[i])
                # dataStr.extend(tempStr)
                if tempStr+tempNum!=[]:
                    dataTemp.append(tempStr+tempNum)
        # 第二个for 获取数据
        # 下面写入矩阵
        for m in range(count1):
            for k in range(np.shape(dataTemp)[0]):
                if dataSet[m] == dataTemp[k][0] and dataSet[m] in signpermission:
                    dataMat[index][m] = dataTemp[k][1]
            feature.append(dataSet[m])
        index += 1
    print(feature)
    # np.savetxt('2828筛选22个权限.txt', dataMat, fmt='%d', delimiter='\t')
    print (np.shape(dataMat))
    data1=[]
    print (count)
    print (count1)
    sum = 0
    for w in range(count1):
        for v in range(count):
                sum += dataMat[v][w]
        # print (sum)
        if sum ==0:
            data1.append(w)
            feature2.append(feature[w])
            #print (data1)
        else:
            # print(feature[w])
            feature1.append(feature[w])
        sum = 0
    print(feature1)
    print(len(feature1))
    # print(feature2)
    print(np.shape(dataMat))
    dataMat = np.delete(dataMat,data1,1)
    np.savetxt('第三轮30个权限数据集.txt', dataMat, fmt='%d', delimiter='\t')



if __name__ == '__main__':
    fileName = "E:\机器学习\SigPermission\新的数据集permission+malware.csv"
    fileFolder = fileName[0:-4]
    file = pd.read_csv(fileName, encoding='utf-8', sep='\t', header=None) # 如果数据间是标准化格式用“\t”,否则用"\s+"
    # print(file.iloc[0:3, :])
    fileArray = np.array(file)
    # print(type(fileArray[0]))
    count = np.shape(fileArray)[0]
    dataStr = []
    data = []
    saveFile = open('data总.txt', 'a')
    for j in range(count):
        fileLine = fileArray[j]
        linArr = str(fileLine)
        lineSplit = linArr.strip().split(',')
        num = len(lineSplit)
        print(fileLine)
        # print(num)
        out = str(j+1) + ' '
        for i in range(num):
            tempStr = re.findall('permission.(\w+)', lineSplit[i])
            tempNum = re.findall('(\d+)', lineSplit[i])
            if tempNum!=['0']:
                tempNum=['1']
            dataStr.extend(tempStr)
            if tempStr+tempNum !=[] and tempStr+tempNum!=['1'] :
                data.append(tempStr + tempNum)
        # 获取data.txt后注释掉(到saveFile.close)
            if len(tempStr) != 0:
                out = out + tempStr[0] + ':' + tempNum[0] + '@'
        out += '\n'
        print(out)
        saveFile.writelines(out)

    saveFile.close()
    dataSet = list(set(dataStr))
    print(dataSet)
    # print(type(dataSet))
    # change(dataSet, data)
    change(dataSet, data)
    createMat(dataSet, data, count)
    fh = open(r'E:\机器学习\SigPermission\第三轮30个权限数据集.csv', "w+", newline='')
    writer = csv.writer(fh)
    data = open(r'E:\机器学习\SigPermission\第三轮30个权限数据集.txt')
    res = []
    for i in data:
        d = [x for x in i.strip().split('\t')]
        # print(d)
        res.append(d)
    print(res)
    writer.writerows(res)
    data.close()
    fh.close()
