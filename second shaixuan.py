import pandas as pd
import numpy as np
import re


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


def createMaliciousMat(dataSet, data, num):
    count1 = len(dataSet)
    feature=[]
    feature1=[]
    feature2=[]

    signpermission=['DELETE_PACKAGES', 'BROADCAST_WAP_PUSH', 'BROADCAST_SMS', 'WRITE_SECURE_SETTINGS', 'RECEIVE_MMS', 'WRITE_APN_SETTINGS', 'CLEAR_APP_CACHE', 'RECEIVE_WAP_PUSH', 'SEND_RESPOND_VIA_MESSAGE', 'DIAGNOSTIC', 'BIND_APPWIDGET', 'CHANGE_NETWORK_STATE', 'FACTORY_TEST', 'CALL_PHONE', 'BIND_WALLPAPER', 'MOUNT_FORMAT_FILESYSTEMS', 'READ_SYNC_STATS', 'BIND_TELECOM_CONNECTION_SERVICE', 'INSTALL_PACKAGES', 'GLOBAL_SEARCH', 'READ_CALENDAR', 'BIND_DEVICE_ADMIN', 'CHANGE_CONFIGURATION', 'READ_LOGS', 'MOUNT_UNMOUNT_FILESYSTEMS', 'SET_WALLPAPER', 'GET_TASKS', 'SET_ALARM', 'SEND_SMS', 'WRITE_CONTACTS', 'ACCESS_NETWORK_STATE', 'WAKE_LOCK', 'RESTART_PACKAGES', 'VIBRATE', 'READ_SYNC_SETTINGS', 'UPDATE_DEVICE_STATS', 'ACCESS_COARSE_LOCATION', 'CHANGE_WIFI_MULTICAST_STATE', 'SET_TIME_ZONE', 'BIND_SCREENING_SERVICE', 'KILL_BACKGROUND_PROCESSES', 'INSTALL_LOCATION_PROVIDER', 'REQUEST_INSTALL_PACKAGES', 'ACCESS_NOTIFICATION_POLICY', 'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'BIND_NFC_SERVICE', 'READ_PHONE_NUMBERS', 'BIND_CHOOSER_TARGET_SERVICE', 'BIND_REMOTEVIEWS', 'SET_TIME', 'ANSWER_PHONE_CALLS', 'BIND_INCALL_SERVICE', 'DUMP', 'REORDER_TASKS', 'MASTER_CLEAR', 'SET_ALWAYS_FINISH', 'USE_FINGERPRINT', 'CONTROL_LOCATION_UPDATES', 'INSTALL_SHORTCUT', 'BIND_DREAM_SERVICE', 'REBOOT', 'GET_ACCOUNTS_PRIVILEGED', 'FOREGROUND_SERVICE', 'WRITE_GSERVICES', 'BLUETOOTH_PRIVILEGED', 'CHANGE_WIFI_STATE', 'PROCESS_OUTGOING_CALLS', 'EXPAND_STATUS_BAR', 'DELETE_CACHE_FILES', 'MODIFY_PHONE_STATE', 'TRANSMIT_IR', 'BLUETOOTH', 'ACCESS_FINE_LOCATION', 'READ_CALL_LOG', 'WRITE_CALL_LOG', 'SET_PREFERRED_APPLICATIONS', 'GET_PACKAGE_SIZE', 'READ_CONTACTS', 'WRITE_SYNC_SETTINGS', 'ACCOUNT_MANAGER', 'BIND_QUICK_SETTINGS_TILE', 'CAPTURE_AUDIO_OUTPUT', 'MODIFY_AUDIO_SETTINGS', 'BIND_NOTIFICATION_LISTENER_SERVICE']
    dataMat = np.zeros((num, count1))
    f = open('恶意data.txt', 'r')
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
    # np.savetxt('筛选22个权限.txt', dataMat, fmt='%d', delimiter='\t')
    print (np.shape(dataMat))
    data1=[]
    print (count)
    print (count1)
    S_Malicious = []
    size_M = 2013
    size_B = 815
    M_ij = 0
    M_Feature_S=[]
    for w in range(count1):
        for v in range(2013):
                M_ij += dataMat[v][w]
        print (M_ij)
        if M_ij ==0:
            data1.append(w)
            feature2.append(feature[w])
            #print (data1)
        else:
            print(feature[w])
            feature1.append(feature[w])
            S_Malicious=str((M_ij / size_M) * size_B)
            M_Feature_S.append(feature[w]+':'+S_Malicious)
        M_ij = 0
    print("恶意样本特征名称",feature1)
    print("恶意样本特征支持度",S_Malicious)
    print(np.shape(dataMat))
    dataMat = np.delete(dataMat,data1,1)
    np.savetxt('恶意权限数据集.txt', dataMat, fmt='%d', delimiter='\t')

    return feature1,dataMat,M_Feature_S
    # for i in range(count1): # 属性
    #     dataMat[0][i] = i
    # for i in range(count1):
    #     for j in range(count2):
    #         if dataSet[i] == data[j][0]:
    #             dataMat[i][1]
def createBenginMat(dataSet, data, num):
    count1 = len(dataSet)
    feature=[]
    feature1=[]
    feature2=[]

    signpermission=['DELETE_PACKAGES', 'BROADCAST_WAP_PUSH', 'BROADCAST_SMS', 'WRITE_SECURE_SETTINGS', 'RECEIVE_MMS', 'WRITE_APN_SETTINGS', 'CLEAR_APP_CACHE', 'RECEIVE_WAP_PUSH', 'SEND_RESPOND_VIA_MESSAGE', 'DIAGNOSTIC', 'BIND_APPWIDGET', 'CHANGE_NETWORK_STATE', 'FACTORY_TEST', 'CALL_PHONE', 'BIND_WALLPAPER', 'MOUNT_FORMAT_FILESYSTEMS', 'READ_SYNC_STATS', 'BIND_TELECOM_CONNECTION_SERVICE', 'INSTALL_PACKAGES', 'GLOBAL_SEARCH', 'READ_CALENDAR', 'BIND_DEVICE_ADMIN', 'CHANGE_CONFIGURATION', 'READ_LOGS', 'MOUNT_UNMOUNT_FILESYSTEMS', 'SET_WALLPAPER', 'GET_TASKS', 'SET_ALARM', 'SEND_SMS', 'WRITE_CONTACTS', 'ACCESS_NETWORK_STATE', 'WAKE_LOCK', 'RESTART_PACKAGES', 'VIBRATE', 'READ_SYNC_SETTINGS', 'UPDATE_DEVICE_STATS', 'ACCESS_COARSE_LOCATION', 'CHANGE_WIFI_MULTICAST_STATE', 'SET_TIME_ZONE', 'BIND_SCREENING_SERVICE', 'KILL_BACKGROUND_PROCESSES', 'INSTALL_LOCATION_PROVIDER', 'REQUEST_INSTALL_PACKAGES', 'ACCESS_NOTIFICATION_POLICY', 'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'BIND_NFC_SERVICE', 'READ_PHONE_NUMBERS', 'BIND_CHOOSER_TARGET_SERVICE', 'BIND_REMOTEVIEWS', 'SET_TIME', 'ANSWER_PHONE_CALLS', 'BIND_INCALL_SERVICE', 'DUMP', 'REORDER_TASKS', 'MASTER_CLEAR', 'SET_ALWAYS_FINISH', 'USE_FINGERPRINT', 'CONTROL_LOCATION_UPDATES', 'INSTALL_SHORTCUT', 'BIND_DREAM_SERVICE', 'REBOOT', 'GET_ACCOUNTS_PRIVILEGED', 'FOREGROUND_SERVICE', 'WRITE_GSERVICES', 'BLUETOOTH_PRIVILEGED', 'CHANGE_WIFI_STATE', 'PROCESS_OUTGOING_CALLS', 'EXPAND_STATUS_BAR', 'DELETE_CACHE_FILES', 'MODIFY_PHONE_STATE', 'TRANSMIT_IR', 'BLUETOOTH', 'ACCESS_FINE_LOCATION', 'READ_CALL_LOG', 'WRITE_CALL_LOG', 'SET_PREFERRED_APPLICATIONS', 'GET_PACKAGE_SIZE', 'READ_CONTACTS', 'WRITE_SYNC_SETTINGS', 'ACCOUNT_MANAGER', 'BIND_QUICK_SETTINGS_TILE', 'CAPTURE_AUDIO_OUTPUT', 'MODIFY_AUDIO_SETTINGS', 'BIND_NOTIFICATION_LISTENER_SERVICE']
    dataMat = np.zeros((num, count1))
    f = open('良性data.txt', 'r')
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
    # np.savetxt('筛选22个权限.txt', dataMat, fmt='%d', delimiter='\t')
    print (np.shape(dataMat))
    data1=[]
    print (count)
    print (count1)
    B_ij=0
    B_ij_list=[]
    B_Feature_sum=[]
    for w in range(count1):
        for v in range(815):
                B_ij += dataMat[v][w]

        print (B_ij)
        if B_ij ==0:
            data1.append(w)
            feature2.append(feature[w])
            #print (data1)
        else:
            print(feature[w])
            feature1.append(feature[w])
            B_ij_list.append(B_ij)
            B_Feature_sum.append(feature[w]+':'+str(B_ij))
        B_ij = 0
    print("良性样本特征名称",feature1)
    print(feature2)
    print(np.shape(dataMat))
    dataMat = np.delete(dataMat,data1,1)
    np.savetxt('良性权限数据集.txt', dataMat, fmt='%d', delimiter='\t')
    return feature1,dataMat,B_Feature_sum
if __name__ == '__main__':
    fileName = "E:\机器学习\SigPermission\新的数据集permission+malware.csv"
    fileFolder = fileName[0:-4]
    file = pd.read_csv(fileName, encoding='utf-8', sep='\t', header=None) # 如果数据间是标准化格式用“\t”,否则用"\s+"
    # print(file.iloc[0:3, :])
    fileArray = np.array(file)
    # print(type(fileArray[0]))
    count = np.shape(fileArray)[0]
    maliciousdataStr = []
    bengindataStr=[]
    maliciousdata = []
    bengindata=[]
    benginFeature=[]
    maliciousFeature=[]

    saveFile = open('恶意data.txt', 'a')
    for j in range(0,2013):
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
            maliciousdataStr.extend(tempStr)
            if tempStr+tempNum !=[] and tempStr+tempNum!=['1'] :
                maliciousdata.append(tempStr + tempNum)
        # 获取data.txt后注释掉(到saveFile.close)
            if len(tempStr) != 0:
                out = out + tempStr[0] + ':' + tempNum[0] + '@'
        out += '\n'
        print(out)
        saveFile.writelines(out)
    saveFile.close()
    dataSet = list(set(maliciousdataStr))
    print(dataSet)
    # print(type(dataSet))
    # change(dataSet, data)
    change(dataSet, maliciousdata)
    maliciousFeature,maliciousDataMat,M_Feature_S=createMaliciousMat(dataSet, maliciousdata, 2013)
    saveFile = open('良性data.txt', 'a')
    for j in range(2013,2828):
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
            bengindataStr.extend(tempStr)
            if tempStr+tempNum !=[] and tempStr+tempNum!=['1'] :
                bengindata.append(tempStr + tempNum)
        # 获取data.txt后注释掉(到saveFile.close)
            if len(tempStr) != 0:
                out = out + tempStr[0] + ':' + tempNum[0] + '@'
        out += '\n'
        print(out)
        saveFile.writelines(out)
    saveFile.close()
    dataSet = list(set(bengindataStr))
    print(dataSet)
    # print(type(dataSet))
    # change(dataSet, data)
    #change(dataSet, bengindata)
    benginFeature,benginDataMat,B_Feature_sum=createBenginMat(dataSet, bengindata, 815)
    # print("良性特征",benginFeature)
    # print("恶意特征", maliciousFeature)
    # print("良性矩阵",benginDataMat)
    # print("恶意矩阵",maliciousDataMat)
    print("恶意样本每个特征对应的支持度",M_Feature_S)
    # print("恶意样本每个特征对应的支持度长度",len(M_Feature_S))
    # print("良性样本每个特征对应特征和",B_Feature_sum)
    # print("良性样本个特征对应特征和长度",len(B_Feature_sum))
    M_Feature_S_count = len(M_Feature_S)
    feature_Sup = []
    Float_M_S=[]
    for M_j_per in range(M_Feature_S_count):
        M_Feature_Str = re.findall('(\w+):', M_Feature_S[M_j_per])
        M_S = re.findall('-?\d+\.?\d*e?-?\d*?', M_Feature_S[M_j_per])
        Float_M_S.append(float(M_S[0]))
        feature_Sup.append(M_Feature_Str+Float_M_S)
        Float_M_S=[]
    print("降序排列", sorted(feature_Sup, key=lambda x: x[1], reverse=True))
    # print("升序排列",sorted(feature_SPR,key=lambda x:x[1]))
    # print("降序排列",sorted(feature_SPR,key=lambda x:x[1],reverse=True))
