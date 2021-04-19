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
    signpermission=[]
    three=0
    three1=0
    up=[['DELETE_PACKAGES', -1], ['BROADCAST_WAP_PUSH', -1], ['BROADCAST_SMS', -1], ['WRITE_SECURE_SETTINGS', -1], ['RECEIVE_MMS', -1], ['WRITE_APN_SETTINGS', -1], ['CLEAR_APP_CACHE', -1], ['RECEIVE_WAP_PUSH', -1], ['SEND_RESPOND_VIA_MESSAGE', -1], ['DIAGNOSTIC', -1], ['BIND_APPWIDGET', -1], ['CHANGE_NETWORK_STATE', 0], ['FACTORY_TEST', 0], ['CALL_PHONE', 0], ['BIND_WALLPAPER', 0], ['MOUNT_FORMAT_FILESYSTEMS', 0], ['READ_SYNC_STATS', 0], ['BIND_TELECOM_CONNECTION_SERVICE', 0], ['INSTALL_PACKAGES', 0], ['GLOBAL_SEARCH', 0], ['READ_CALENDAR', 0], ['BIND_DEVICE_ADMIN', 0], ['CHANGE_CONFIGURATION', 0], ['READ_LOGS', 0], ['MOUNT_UNMOUNT_FILESYSTEMS', 0], ['SET_WALLPAPER', 0], ['GET_TASKS', 0], ['SET_ALARM', 0], ['SEND_SMS', 0], ['WRITE_CONTACTS', 0], ['ACCESS_NETWORK_STATE', 0], ['WAKE_LOCK', 0], ['RESTART_PACKAGES', 0], ['VIBRATE', 0], ['READ_SYNC_SETTINGS', 0], ['UPDATE_DEVICE_STATS', 0], ['ACCESS_COARSE_LOCATION', 0], ['CHANGE_WIFI_MULTICAST_STATE', 0], ['SET_TIME_ZONE', 0], ['BIND_SCREENING_SERVICE', 0], ['KILL_BACKGROUND_PROCESSES', 0], ['INSTALL_LOCATION_PROVIDER', 0], ['GET_ACCOUNTS', 0], ['PERSISTENT_ACTIVITY', 0], ['READ_SMS', 0], ['RECEIVE_BOOT_COMPLETED', 0], ['SET_WALLPAPER_HINTS', 0], ['LOCATION_HARDWARE', 0], ['NFC', 0], ['MANAGE_DOCUMENTS', 0], ['BLUETOOTH_ADMIN', 0], ['PACKAGE_USAGE_STATS', 0], ['ACCESS_LOCATION_EXTRA_COMMANDS', 0], ['DISABLE_KEYGUARD', 0], ['RECEIVE_SMS', 0], ['CAMERA', 0], ['BODY_SENSORS', 0], ['MEDIA_CONTENT_CONTROL', 0], ['WRITE_CALENDAR', 0], ['BIND_INPUT_METHOD', 0], ['ACCESS_WIFI_STATE', 0], ['BROADCAST_STICKY', 0], ['CALL_PRIVILEGED', 0], ['WRITE_EXTERNAL_STORAGE', 0], ['WRITE_SETTINGS', 0], ['READ_EXTERNAL_STORAGE', 0], ['BIND_VPN_SERVICE', 0], ['BIND_ACCESSIBILITY_SERVICE', 0], ['INTERNET', 0], ['SET_DEBUG_APP', 0], ['BIND_PRINT_SERVICE', 0], ['UNINSTALL_SHORTCUT', 0], ['BATTERY_STATS', 0], ['SYSTEM_ALERT_WINDOW', 0], ['ACCESS_CHECKIN_PROPERTIES', 0], ['SIGNAL_PERSISTENT_PROCESSES', 0], ['RECORD_AUDIO', 0], ['READ_PHONE_STATE', 0], ['CHANGE_COMPONENT_ENABLED_STATE', 0], ['USE_SIP', 0], ['STATUS_BAR', 0], ['BIND_NOTIFICATION_LISTENER_SERVICE', 0], ['MODIFY_AUDIO_SETTINGS', 0], ['CAPTURE_AUDIO_OUTPUT', 0], ['BIND_QUICK_SETTINGS_TILE', 0], ['ACCOUNT_MANAGER', 0], ['WRITE_SYNC_SETTINGS', 0], ['READ_CONTACTS', 0], ['GET_PACKAGE_SIZE', 0], ['SET_PREFERRED_APPLICATIONS', 0], ['WRITE_CALL_LOG', 0], ['READ_CALL_LOG', 0], ['ACCESS_FINE_LOCATION', 0], ['BLUETOOTH', 0], ['TRANSMIT_IR', 0], ['MODIFY_PHONE_STATE', 0], ['DELETE_CACHE_FILES', 0], ['EXPAND_STATUS_BAR', 0], ['PROCESS_OUTGOING_CALLS', 0], ['CHANGE_WIFI_STATE', 0], ['BLUETOOTH_PRIVILEGED', 1], ['WRITE_GSERVICES', 1], ['FOREGROUND_SERVICE', 1], ['GET_ACCOUNTS_PRIVILEGED', 1], ['REBOOT', 1], ['BIND_DREAM_SERVICE', 1], ['INSTALL_SHORTCUT', 1], ['CONTROL_LOCATION_UPDATES', 1], ['USE_FINGERPRINT', 1], ['SET_ALWAYS_FINISH', 1], ['MASTER_CLEAR', 1], ['REORDER_TASKS', 1], ['DUMP', 1], ['BIND_INCALL_SERVICE', 1], ['ANSWER_PHONE_CALLS', 1], ['SET_TIME', 1], ['BIND_REMOTEVIEWS', 1], ['BIND_CHOOSER_TARGET_SERVICE', 1], ['READ_PHONE_NUMBERS', 1], ['BIND_NFC_SERVICE', 1], ['REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 1], ['ACCESS_NOTIFICATION_POLICY', 1], ['REQUEST_INSTALL_PACKAGES', 1]]
    down=[['REQUEST_INSTALL_PACKAGES', 1], ['ACCESS_NOTIFICATION_POLICY', 1],
         ['REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 1], ['BIND_NFC_SERVICE', 1],
         ['READ_PHONE_NUMBERS', 1], ['BIND_CHOOSER_TARGET_SERVICE', 1],
         ['BIND_REMOTEVIEWS', 1], ['SET_TIME', 1],['ANSWER_PHONE_CALLS',1],
         ['BIND_INCALL_SERVICE', 1],['DUMP', 1],['REORDER_TASKS', 1],['MASTER_CLEAR', 1],
         ['SET_ALWAYS_FINISH', 1],['USE_FINGERPRINT', 1],['CONTROL_LOCATION_UPDATES', 1],
         ['INSTALL_SHORTCUT', 1],['BIND_DREAM_SERVICE', 1],['REBOOT',1],
         ['GET_ACCOUNTS_PRIVILEGED', 1],['FOREGROUND_SERVICE', 1],['WRITE_GSERVICES', 1],
         ['BLUETOOTH_PRIVILEGED', 1],['CHANGE_WIFI_STATE', 0],['PROCESS_OUTGOING_CALLS',
         0],['EXPAND_STATUS_BAR', 0],['DELETE_CACHE_FILES', 0],['MODIFY_PHONE_STATE', 0],
         ['TRANSMIT_IR', 0],['BLUETOOTH', 0],['ACCESS_FINE_LOCATION', 0],['READ_CALL_LOG',
         0],['WRITE_CALL_LOG', 0],['SET_PREFERRED_APPLICATIONS',0],['GET_PACKAGE_SIZE',
         0],['READ_CONTACTS', 0],['WRITE_SYNC_SETTINGS', 0],['ACCOUNT_MANAGER', 0],
         ['BIND_QUICK_SETTINGS_TILE', 0],['CAPTURE_AUDIO_OUTPUT', 0],
         ['MODIFY_AUDIO_SETTINGS', 0],['BIND_NOTIFICATION_LISTENER_SERVICE', 0],
         ['STATUS_BAR', 0],['USE_SIP', 0],['CHANGE_COMPONENT_ENABLED_STATE', 0],
         ['READ_PHONE_STATE', 0],['RECORD_AUDIO', 0],['SIGNAL_PERSISTENT_PROCESSES', 0],
         ['ACCESS_CHECKIN_PROPERTIES', 0],['SYSTEM_ALERT_WINDOW', 0],['BATTERY_STATS',
         0],['UNINSTALL_SHORTCUT', 0],['BIND_PRINT_SERVICE', 0],['SET_DEBUG_APP', 0],['INTERNET', 0],['BIND_ACCESSIBILITY_SERVICE', 0],['BIND_VPN_SERVICE', 0],['READ_EXTERNAL_STORAGE', 0],['WRITE_SETTINGS', 0],['WRITE_EXTERNAL_STORAGE', 0],['CALL_PRIVILEGED', 0],['BROADCAST_STICKY', 0],['ACCESS_WIFI_STATE', 0],['BIND_INPUT_METHOD', 0],['WRITE_CALENDAR', 0],['MEDIA_CONTENT_CONTROL', 0],['BODY_SENSORS', 0],['CAMERA', 0],['RECEIVE_SMS', 0],['DISABLE_KEYGUARD', 0],['ACCESS_LOCATION_EXTRA_COMMANDS', 0],['PACKAGE_USAGE_STATS', 0],['BLUETOOTH_ADMIN', 0],['MANAGE_DOCUMENTS', 0],['NFC', 0],['LOCATION_HARDWARE', 0],['SET_WALLPAPER_HINTS', 0],['RECEIVE_BOOT_COMPLETED', 0],['READ_SMS', 0],['PERSISTENT_ACTIVITY', 0],['GET_ACCOUNTS', 0],['INSTALL_LOCATION_PROVIDER', 0],['KILL_BACKGROUND_PROCESSES', 0],['BIND_SCREENING_SERVICE', 0],['SET_TIME_ZONE', 0],['CHANGE_WIFI_MULTICAST_STATE', 0],['ACCESS_COARSE_LOCATION', 0],['UPDATE_DEVICE_STATS', 0],['READ_SYNC_SETTINGS', 0],['VIBRATE', 0],['RESTART_PACKAGES', 0],['WAKE_LOCK', 0],['ACCESS_NETWORK_STATE', 0],['WRITE_CONTACTS', 0],['SEND_SMS', 0],['SET_ALARM', 0],['GET_TASKS', 0],['SET_WALLPAPER', 0],['MOUNT_UNMOUNT_FILESYSTEMS', 0],['READ_LOGS', 0],['CHANGE_CONFIGURATION', 0],['BIND_DEVICE_ADMIN', 0],['READ_CALENDAR', 0],['GLOBAL_SEARCH', 0],['INSTALL_PACKAGES', 0],['BIND_TELECOM_CONNECTION_SERVICE', 0],['READ_SYNC_STATS', 0],['MOUNT_FORMAT_FILESYSTEMS', 0],['BIND_WALLPAPER', 0],['CALL_PHONE', 0],['FACTORY_TEST', 0],['CHANGE_NETWORK_STATE', 0],['BIND_APPWIDGET', -1],['DIAGNOSTIC', -1],['SEND_RESPOND_VIA_MESSAGE', -1],['RECEIVE_WAP_PUSH', -1],['CLEAR_APP_CACHE', -1],['WRITE_APN_SETTINGS', -1],['RECEIVE_MMS', -1],['WRITE_SECURE_SETTINGS', -1],['BROADCAST_SMS', -1],['BROADCAST_WAP_PUSH', -1],['DELETE_PACKAGES', -1]]
    for i in up:
        signpermission.append(i[0])
        three=three+1
        if three==63:
            break
    for j in down:
        signpermission.append(j[0])
        three1=three1+1
        if three1==63:
            print(signpermission)
            print(len(signpermission))
            break
    # signpermission=['WRITE_EXTERNAL_STORAGE', 'ACCESS_MEDIA_LOCATION', 'ACCESS_BACKGROUND_LOCATION', 'BLUETOOTH', 'EXPAND_STATUS_BAR', 'CALL_PRIVILEGED', 'GLOBAL_SEARCH', 'DISABLE_KEYGUARD', 'BIND_TELECOM_CONNECTION_SERVICE', 'BIND_DREAM_SERVICE', 'REQUEST_DELETE_PACKAGES', 'BIND_CARRIER_MESSAGING_SERVICE', 'RECEIVE_WAP_PUSH', 'SET_TIME_ZONE', 'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS', 'BIND_CARRIER_SERVICES', 'MEDIA_CONTENT_CONTROL', 'INSTALL_PACKAGES', 'BROADCAST_WAP_PUSH', 'CAPTURE_AUDIO_OUTPUT', 'BIND_VOICE_INTERACTION', 'ACCESS_NETWORK_STATE', 'INSTALL_SHORTCUT', 'BIND_TEXT_SERVICE', 'BROADCAST_PACKAGE_REMOVED', 'ACCESS_NOTIFICATION_POLICY', 'READ_SYNC_STATS', 'SET_PROCESS_LIMIT', 'CHANGE_COMPONENT_ENABLED_STATE', 'ACCESS_CHECKIN_PROPERTIES', 'RECORD_AUDIO', 'MANAGE_OWN_CALLS', 'SIGNAL_PERSISTENT_PROCESSES', 'KILL_BACKGROUND_PROCESSES', 'ACCESS_FINE_LOCATION', 'READ_PHONE_STATE', 'WRITE_CONTACTS', 'WRITE_GSERVICES', 'QUERY_ALL_PACKAGES', 'BIND_NOTIFICATION_LISTENER_SERVICE', 'MOUNT_FORMAT_FILESYSTEMS', 'REORDER_TASKS', 'BIND_VR_LISTENER_SERVICE', 'RECEIVE_BOOT_COMPLETED', 'RECEIVE_MMS', 'BROADCAST_STICKY', 'DELETE_CACHE_FILES', 'BIND_NFC_SERVICE', 'SET_PREFERRED_APPLICATIONS', 'SEND_SMS', 'RECEIVE_SMS', 'MASTER_CLEAR', 'SET_WALLPAPER_HINTS', 'BIND_PRINT_SERVICE', 'READ_LOGS', 'BIND_REMOTEVIEWS', 'REQUEST_INSTALL_PACKAGES', 'STATUS_BAR', 'BIND_APPWIDGET', 'WRITE_APN_SETTINGS', 'SEND_RESPOND_VIA_MESSAGE', 'BIND_INCALL_SERVICE', 'BIND_CHOOSER_TARGET_SERVICE', 'CALL_PHONE', 'VIBRATE', 'USE_FINGERPRINT', 'USE_FULL_SCREEN_INTENT', 'WRITE_SECURE_SETTINGS', 'SET_ALWAYS_FINISH', 'WRITE_SYNC_SETTINGS', 'BIND_QUICK_SETTINGS_TILE', 'CONTROL_LOCATION_UPDATES', 'BLUETOOTH_ADMIN', 'WRITE_SETTINGS', 'SET_ANIMATION_SCALE', 'FACTORY_TEST', 'ANSWER_PHONE_CALLS', 'PERSISTENT_ACTIVITY', 'GET_ACCOUNTS_PRIVILEGED', 'READ_PRECISE_PHONE_STATE', 'READ_CALENDAR', 'ACTIVITY_RECOGNITION', 'USE_SIP', 'READ_EXTERNAL_STORAGE', 'GET_TASKS', 'READ_INPUT_STATE', 'BIND_VPN_SERVICE', 'RESTART_PACKAGES', 'READ_SMS', 'SET_ALARM', 'ACCOUNT_MANAGER', 'BIND_MIDI_DEVICE_SERVICE', 'READ_PHONE_NUMBERS', 'CHANGE_WIFI_STATE', 'BIND_WALLPAPER', 'MOUNT_UNMOUNT_FILESYSTEMS', 'INSTALL_LOCATION_PROVIDER', 'MANAGE_DOCUMENTS', 'INSTANT_APP_FOREGROUND_SERVICE', 'SYSTEM_ALERT_WINDOW', 'CHANGE_CONFIGURATION', 'BIND_DEVICE_ADMIN', 'BODY_SENSORS', 'BATTERY_STATS', 'INTERNET', 'BROADCAST_SMS', 'CLEAR_APP_CACHE', 'USE_BIOMETRIC', 'PACKAGE_USAGE_STATS', 'BIND_ACCESSIBILITY_SERVICE', 'TRANSMIT_IR', 'SET_DEBUG_APP', 'BIND_INPUT_METHOD', 'DELETE_PACKAGES', 'REBOOT', 'BIND_SCREENING_SERVICE', 'CAMERA', 'ACCESS_WIFI_STATE', 'GET_ACCOUNTS', 'READ_CONTACTS', 'ACCESS_COARSE_LOCATION', 'READ_CALL_LOG', 'CHANGE_WIFI_MULTICAST_STATE', 'UPDATE_DEVICE_STATS', 'MODIFY_AUDIO_SETTINGS', 'GET_PACKAGE_SIZE', 'BIND_CONDITION_PROVIDER_SERVICE', 'NFC', 'UNINSTALL_SHORTCUT', 'MODIFY_PHONE_STATE', 'READ_SYNC_SETTINGS', 'WAKE_LOCK', 'BLUETOOTH_PRIVILEGED', 'ACCESS_LOCATION_EXTRA_COMMANDS', 'SET_TIME', 'WRITE_CALENDAR', 'WRITE_CALL_LOG', 'SET_WALLPAPER', 'DUMP', 'CHANGE_NETWORK_STATE', 'DIAGNOSTIC', 'PROCESS_OUTGOING_CALLS', 'LOCATION_HARDWARE', 'FOREGROUND_SERVICE', 'BIND_TV_INPUT']
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
    np.savetxt('123筛选数据集.txt', dataMat, fmt='%d', delimiter='\t')



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
    fh = open(r'E:\机器学习\SigPermission\123筛选数据集.csv', "w+", newline='')
    writer = csv.writer(fh)
    data = open(r'E:\机器学习\SigPermission\123筛选数据集.txt')
    res = []
    for i in data:
        d = [x for x in i.strip().split('\t')]
        # print(d)
        res.append(d)
    print(res)
    writer.writerows(res)
    data.close()
    fh.close()
