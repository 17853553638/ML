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

    signpermission=['WRITE_EXTERNAL_STORAGE', 'ACCESS_MEDIA_LOCATION', 'ACCESS_BACKGROUND_LOCATION', 'BLUETOOTH', 'EXPAND_STATUS_BAR', 'CALL_PRIVILEGED', 'GLOBAL_SEARCH', 'DISABLE_KEYGUARD', 'BIND_TELECOM_CONNECTION_SERVICE', 'BIND_DREAM_SERVICE', 'REQUEST_DELETE_PACKAGES', 'BIND_CARRIER_MESSAGING_SERVICE', 'RECEIVE_WAP_PUSH', 'SET_TIME_ZONE', 'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'BIND_CARRIER_SERVICES', 'MEDIA_CONTENT_CONTROL', 'INSTALL_PACKAGES', 'BROADCAST_WAP_PUSH', 'CAPTURE_AUDIO_OUTPUT', 'BIND_VOICE_INTERACTION', 'ACCESS_NETWORK_STATE', 'INSTALL_SHORTCUT', 'BIND_TEXT_SERVICE', 'BROADCAST_PACKAGE_REMOVED', 'ACCESS_NOTIFICATION_POLICY', 'READ_SYNC_STATS', 'SET_PROCESS_LIMIT', 'CHANGE_COMPONENT_ENABLED_STATE', 'ACCESS_CHECKIN_PROPERTIES', 'RECORD_AUDIO', 'MANAGE_OWN_CALLS', 'SIGNAL_PERSISTENT_PROCESSES', 'KILL_BACKGROUND_PROCESSES', 'ACCESS_FINE_LOCATION', 'READ_PHONE_STATE', 'WRITE_CONTACTS', 'WRITE_GSERVICES', 'QUERY_ALL_PACKAGES', 'BIND_NOTIFICATION_LISTENER_SERVICE', 'MOUNT_FORMAT_FILESYSTEMS', 'REORDER_TASKS', 'BIND_VR_LISTENER_SERVICE', 'RECEIVE_BOOT_COMPLETED', 'RECEIVE_MMS', 'BROADCAST_STICKY', 'DELETE_CACHE_FILES', 'BIND_NFC_SERVICE', 'SET_PREFERRED_APPLICATIONS', 'SEND_SMS', 'RECEIVE_SMS', 'MASTER_CLEAR', 'SET_WALLPAPER_HINTS', 'BIND_PRINT_SERVICE', 'READ_LOGS', 'BIND_REMOTEVIEWS', 'REQUEST_INSTALL_PACKAGES', 'STATUS_BAR', 'BIND_APPWIDGET', 'WRITE_APN_SETTINGS', 'SEND_RESPOND_VIA_MESSAGE', 'BIND_INCALL_SERVICE', 'BIND_CHOOSER_TARGET_SERVICE', 'CALL_PHONE', 'VIBRATE', 'USE_FINGERPRINT', 'USE_FULL_SCREEN_INTENT', 'WRITE_SECURE_SETTINGS', 'SET_ALWAYS_FINISH', 'WRITE_SYNC_SETTINGS', 'BIND_QUICK_SETTINGS_TILE', 'CONTROL_LOCATION_UPDATES', 'BLUETOOTH_ADMIN', 'WRITE_SETTINGS', 'SET_ANIMATION_SCALE', 'FACTORY_TEST', 'ANSWER_PHONE_CALLS', 'PERSISTENT_ACTIVITY', 'GET_ACCOUNTS_PRIVILEGED', 'READ_PRECISE_PHONE_STATE', 'READ_CALENDAR', 'ACTIVITY_RECOGNITION', 'USE_SIP', 'READ_EXTERNAL_STORAGE', 'GET_TASKS', 'READ_INPUT_STATE', 'BIND_VPN_SERVICE', 'RESTART_PACKAGES', 'READ_SMS', 'SET_ALARM', 'ACCOUNT_MANAGER', 'BIND_MIDI_DEVICE_SERVICE', 'READ_PHONE_NUMBERS', 'CHANGE_WIFI_STATE', 'BIND_WALLPAPER', 'MOUNT_UNMOUNT_FILESYSTEMS', 'INSTALL_LOCATION_PROVIDER', 'MANAGE_DOCUMENTS', 'INSTANT_APP_FOREGROUND_SERVICE', 'SYSTEM_ALERT_WINDOW', 'CHANGE_CONFIGURATION', 'BIND_DEVICE_ADMIN', 'BODY_SENSORS', 'BATTERY_STATS', 'INTERNET', 'BROADCAST_SMS', 'CLEAR_APP_CACHE', 'USE_BIOMETRIC', 'PACKAGE_USAGE_STATS', 'BIND_ACCESSIBILITY_SERVICE', 'TRANSMIT_IR', 'SET_DEBUG_APP', 'BIND_INPUT_METHOD', 'DELETE_PACKAGES', 'REBOOT', 'BIND_SCREENING_SERVICE', 'CAMERA', 'ACCESS_WIFI_STATE', 'GET_ACCOUNTS', 'READ_CONTACTS', 'ACCESS_COARSE_LOCATION', 'READ_CALL_LOG', 'CHANGE_WIFI_MULTICAST_STATE', 'UPDATE_DEVICE_STATS', 'MODIFY_AUDIO_SETTINGS', 'GET_PACKAGE_SIZE', 'BIND_CONDITION_PROVIDER_SERVICE', 'NFC', 'UNINSTALL_SHORTCUT', 'MODIFY_PHONE_STATE', 'READ_SYNC_SETTINGS', 'WAKE_LOCK', 'BLUETOOTH_PRIVILEGED', 'ACCESS_LOCATION_EXTRA_COMMANDS', 'SET_TIME', 'WRITE_CALENDAR', 'WRITE_CALL_LOG', 'SET_WALLPAPER', 'DUMP', 'CHANGE_NETWORK_STATE', 'DIAGNOSTIC', 'PROCESS_OUTGOING_CALLS', 'LOCATION_HARDWARE', 'FOREGROUND_SERVICE', 'BIND_TV_INPUT']
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

    signpermission=['WRITE_EXTERNAL_STORAGE', 'ACCESS_MEDIA_LOCATION', 'ACCESS_BACKGROUND_LOCATION', 'BLUETOOTH', 'EXPAND_STATUS_BAR', 'CALL_PRIVILEGED', 'GLOBAL_SEARCH', 'DISABLE_KEYGUARD', 'BIND_TELECOM_CONNECTION_SERVICE', 'BIND_DREAM_SERVICE', 'REQUEST_DELETE_PACKAGES', 'BIND_CARRIER_MESSAGING_SERVICE', 'RECEIVE_WAP_PUSH', 'SET_TIME_ZONE', 'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'BIND_CARRIER_SERVICES', 'MEDIA_CONTENT_CONTROL', 'INSTALL_PACKAGES', 'BROADCAST_WAP_PUSH', 'CAPTURE_AUDIO_OUTPUT', 'BIND_VOICE_INTERACTION', 'ACCESS_NETWORK_STATE', 'INSTALL_SHORTCUT', 'BIND_TEXT_SERVICE', 'BROADCAST_PACKAGE_REMOVED', 'ACCESS_NOTIFICATION_POLICY', 'READ_SYNC_STATS', 'SET_PROCESS_LIMIT', 'CHANGE_COMPONENT_ENABLED_STATE', 'ACCESS_CHECKIN_PROPERTIES', 'RECORD_AUDIO', 'MANAGE_OWN_CALLS', 'SIGNAL_PERSISTENT_PROCESSES', 'KILL_BACKGROUND_PROCESSES', 'ACCESS_FINE_LOCATION', 'READ_PHONE_STATE', 'WRITE_CONTACTS', 'WRITE_GSERVICES', 'QUERY_ALL_PACKAGES', 'BIND_NOTIFICATION_LISTENER_SERVICE', 'MOUNT_FORMAT_FILESYSTEMS', 'REORDER_TASKS', 'BIND_VR_LISTENER_SERVICE', 'RECEIVE_BOOT_COMPLETED', 'RECEIVE_MMS', 'BROADCAST_STICKY', 'DELETE_CACHE_FILES', 'BIND_NFC_SERVICE', 'SET_PREFERRED_APPLICATIONS', 'SEND_SMS', 'RECEIVE_SMS', 'MASTER_CLEAR', 'SET_WALLPAPER_HINTS', 'BIND_PRINT_SERVICE', 'READ_LOGS', 'BIND_REMOTEVIEWS', 'REQUEST_INSTALL_PACKAGES', 'STATUS_BAR', 'BIND_APPWIDGET', 'WRITE_APN_SETTINGS', 'SEND_RESPOND_VIA_MESSAGE', 'BIND_INCALL_SERVICE', 'BIND_CHOOSER_TARGET_SERVICE', 'CALL_PHONE', 'VIBRATE', 'USE_FINGERPRINT', 'USE_FULL_SCREEN_INTENT', 'WRITE_SECURE_SETTINGS', 'SET_ALWAYS_FINISH', 'WRITE_SYNC_SETTINGS', 'BIND_QUICK_SETTINGS_TILE', 'CONTROL_LOCATION_UPDATES', 'BLUETOOTH_ADMIN', 'WRITE_SETTINGS', 'SET_ANIMATION_SCALE', 'FACTORY_TEST', 'ANSWER_PHONE_CALLS', 'PERSISTENT_ACTIVITY', 'GET_ACCOUNTS_PRIVILEGED', 'READ_PRECISE_PHONE_STATE', 'READ_CALENDAR', 'ACTIVITY_RECOGNITION', 'USE_SIP', 'READ_EXTERNAL_STORAGE', 'GET_TASKS', 'READ_INPUT_STATE', 'BIND_VPN_SERVICE', 'RESTART_PACKAGES', 'READ_SMS', 'SET_ALARM', 'ACCOUNT_MANAGER', 'BIND_MIDI_DEVICE_SERVICE', 'READ_PHONE_NUMBERS', 'CHANGE_WIFI_STATE', 'BIND_WALLPAPER', 'MOUNT_UNMOUNT_FILESYSTEMS', 'INSTALL_LOCATION_PROVIDER', 'MANAGE_DOCUMENTS', 'INSTANT_APP_FOREGROUND_SERVICE', 'SYSTEM_ALERT_WINDOW', 'CHANGE_CONFIGURATION', 'BIND_DEVICE_ADMIN', 'BODY_SENSORS', 'BATTERY_STATS', 'INTERNET', 'BROADCAST_SMS', 'CLEAR_APP_CACHE', 'USE_BIOMETRIC', 'PACKAGE_USAGE_STATS', 'BIND_ACCESSIBILITY_SERVICE', 'TRANSMIT_IR', 'SET_DEBUG_APP', 'BIND_INPUT_METHOD', 'DELETE_PACKAGES', 'REBOOT', 'BIND_SCREENING_SERVICE', 'CAMERA', 'ACCESS_WIFI_STATE', 'GET_ACCOUNTS', 'READ_CONTACTS', 'ACCESS_COARSE_LOCATION', 'READ_CALL_LOG', 'CHANGE_WIFI_MULTICAST_STATE', 'UPDATE_DEVICE_STATS', 'MODIFY_AUDIO_SETTINGS', 'GET_PACKAGE_SIZE', 'BIND_CONDITION_PROVIDER_SERVICE', 'NFC', 'UNINSTALL_SHORTCUT', 'MODIFY_PHONE_STATE', 'READ_SYNC_SETTINGS', 'WAKE_LOCK', 'BLUETOOTH_PRIVILEGED', 'ACCESS_LOCATION_EXTRA_COMMANDS', 'SET_TIME', 'WRITE_CALENDAR', 'WRITE_CALL_LOG', 'SET_WALLPAPER', 'DUMP', 'CHANGE_NETWORK_STATE', 'DIAGNOSTIC', 'PROCESS_OUTGOING_CALLS', 'LOCATION_HARDWARE', 'FOREGROUND_SERVICE', 'BIND_TV_INPUT']
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
    print("良性样本每个特征对应特征和",B_Feature_sum)
    # print("良性样本个特征对应特征和长度",len(B_Feature_sum))
    public_per=[]
    SPR=[]
    feature_SPR=[]
    M_Feature_S_count=len(M_Feature_S)
    B_Feature_sum_count=len(B_Feature_sum)
    for M_j_per in range(M_Feature_S_count):
        for B_j_per in range(B_Feature_sum_count):
            B_Feature_Str = re.findall('(\w+):', B_Feature_sum[B_j_per])
            B_sum = re.findall('-?\d+\.?\d*e?-?\d*?', B_Feature_sum[B_j_per])
            B_sum_number=float(B_sum[0])
            M_Feature_Str = re.findall('(\w+):', M_Feature_S[M_j_per])
            M_S = re.findall('-?\d+\.?\d*e?-?\d*?', M_Feature_S[M_j_per])
            M_S_number=float(M_S[0])
            if B_Feature_Str==M_Feature_Str:
                public_per.append(B_Feature_Str)
                R_P=(B_sum_number- M_S_number)/(B_sum_number+M_S_number)
                if(R_P>0.5):
                    SPR.append(1)
                elif R_P<-0.5:
                    SPR.append(-1)
                elif (R_P<0.5and R_P>-0.5):
                    SPR.append(0)

                feature_SPR.append(B_Feature_Str+SPR)
                SPR=[]
    print("样本权限",public_per)
    print("权限数目",len(public_per))
    print("计算权限速率",SPR)
    print("特征和权限速率",feature_SPR)
    print("特征和权限速率数目",len(feature_SPR))
    print("升序排列",sorted(feature_SPR,key=lambda x:x[1]))
    print("降序排列",sorted(feature_SPR,key=lambda x:x[1],reverse=True))
