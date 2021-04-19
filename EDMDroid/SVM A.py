import numpy as np
from indicator import indicator
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier

if __name__ == '__main__':
    sumPrecision = 0
    sumRecall = 0
    sumF_meature = 0
    sumAUC = 0
    sumAccuracy = 0
    sumSpecific = 0
    sumMCC = 0
    sumTPR = 0
    sumFPR = 0
    sumx = 0
    sumy = 0

    label = ['fold1', 'fold2', 'fold3', 'fold4', 'fold5', 'Average']
    for i in range(1,6):
        print("第%d折的结果"% i)
        # svm_filename='subsets1/'+str(i)+'/train/'+str(j+16)+'.csv'
        svm_filename='AB/' + str(i) + '/train.csv'
        # svm_filename = 'AB1 Rotation/' + str(i) + '/train/' + str(j) + '.csv'
        # svm 训练数据
        svm_data = pd.read_csv(svm_filename, header=None)
        array = svm_data.values
        dataInfo = svm_data.shape[1]
        svm_trainX = array[:, 1:dataInfo]
        svm_trainy = array[:, 0]
        scaler = StandardScaler()
        scaler.fit(svm_trainX)
        svm_trainX_scaled = scaler.transform(svm_trainX)





        # svm_filename5 = 'subsets1/' + str(i) + '/test/' + str(j + 16) + '.csv'
        svm_filename5 ='AB/' + str(i) + '/test.csv'
        # svm_filename5 = 'AB1 Rotation/' + str(i) + '/test/' + str(j) + '.csv'
        # svm 测试数据
        svm_data2 = pd.read_csv(svm_filename5, header=None)
        array2 = svm_data2.values
        dataInfo2 = svm_data2.shape[1]
        svm_testX = array2[:, 1:dataInfo2]
        svm_testy = array2[:, 0]
        scaler.fit(svm_testX)
        svm_testX_scaled = scaler.transform(svm_testX)


        svm_model =SVC(gamma='auto', kernel='poly', degree=1, max_iter=-1, probability=True)

        print("svm")
        svm_model.fit(svm_trainX_scaled, svm_trainy)
        print(svm_model.score(svm_testX_scaled, svm_testy))
        pred = svm_model.predict(svm_testX_scaled)

        score = indicator(pred, svm_testy)
        Accuracy, Precision, Recall, F_meature = score.getMetrics()
        Specific = score.getSpecific()
        TPR, FPR = score.getfprtpr()
        AUC, x, y = score.getAuc()
        sumx += x
        sumy += y
        MCC = score.getMCC()
        sumAccuracy += Accuracy
        print(classification_report(svm_testy, pred))
        print("Accuracy:", Accuracy)
        print("Precison:", Precision)
        print("Recall:", Recall)
        print("F-meature:", F_meature)
        print("Specific:", Specific)
        print("MCC:", MCC)
        print("AUC:", AUC)
        print("TPR:", TPR)
        print("FPR:", FPR)
        sumPrecision += Precision
        sumRecall += Recall
        sumF_meature += F_meature
        sumAUC += AUC
        sumSpecific += Specific
        sumMCC += MCC
        sumTPR += TPR
        sumFPR += FPR
        plt.plot(x, y, lw=0.5)
        print('------------------------------')
    print("Average Accuracy:", sumAccuracy / 5)
    print("Average Precision:", sumPrecision / 5)
    print("Average Recall:", sumRecall / 5)
    print("Average F-meature:", sumF_meature / 5)
    print("Average Specific:", sumSpecific / 5)
    print("Average MCC:", sumMCC / 5)
    print("Average AUC:", sumAUC / 5)
    print("Average TPR:", sumTPR / 5)
    print("Average FPR:", sumFPR / 5)
    x = sumx / 5
    y = sumy / 5
    plt.plot(x, y, lw=0.5)
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)
    plt.legend(label)
    plt.title(" svm ")
    plt.show()