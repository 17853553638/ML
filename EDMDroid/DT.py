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

        for j in range(1,21):
            # dt_filename='subsets1/'+str(i)+'/train/'+str(j+8)+'.csv'
            # dt_filename='A/' + str(i) + '/train.csv'
            dt_filename = 'A Rotation/' + str(i) + '/train/' + str(j) + '.csv'
            # DT 训练数据
            dt_data = pd.read_csv(dt_filename, header=None)
            array = dt_data.values
            dataInfo = dt_data.shape[1]
            dt_trainX = array[:, 1:dataInfo]
            dt_trainy = array[:, 0]
            scaler = StandardScaler()
            scaler.fit(dt_trainX)
            dt_trainX_scaled = scaler.transform(dt_trainX)

                # dt_filename5 = 'subsets1/' + str(i) + '/test/' + str(j + 8) + '.csv'
            # dt_filename5 ='A Rotation/' + str(i) + '/test.csv'
            dt_filename5 = 'A Rotation/' + str(i) + '/test/' + str(j) + '.csv'
                # dt 测试数据
            dt_data2 = pd.read_csv(dt_filename5, header=None)
            array2 = dt_data2.values
            dataInfo2 = dt_data2.shape[1]
            dt_testX = array2[:, 1:dataInfo2]
            dt_testy = array2[:, 0]
            scaler.fit(dt_testX)
            dt_testX_scaled = scaler.transform(dt_testX)


            dt_model = DecisionTreeClassifier(max_depth=9,random_state=666)

            print("DT")
            dt_model.fit(dt_trainX, dt_trainy)
            print(dt_model.score(dt_testX, dt_testy))
            pred = dt_model.predict(dt_testX)

            score = indicator(pred, dt_testy)
            Accuracy, Precision, Recall, F_meature = score.getMetrics()
            Specific = score.getSpecific()
            TPR, FPR = score.getfprtpr()
            AUC, x, y = score.getAuc()
            sumx += x
            sumy += y
            MCC = score.getMCC()
            sumAccuracy += Accuracy
            print(classification_report(dt_testy, pred))
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

    print("Average Accuracy:", sumAccuracy / 100)
    print("Average Precision:", sumPrecision / 100)
    print("Average Recall:", sumRecall / 100)
    print("Average F-meature:", sumF_meature /100)
    print("Average Specific:", sumSpecific / 100)
    print("Average MCC:", sumMCC / 100)
    print("Average AUC:", sumAUC / 100)
    print("Average TPR:", sumTPR / 100)
    print("Average FPR:", sumFPR / 100)
    x = sumx / 100
    y = sumy / 100
    plt.plot(x, y, lw=0.5)
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)
    plt.legend(label)
    plt.title(" dt ")
    plt.show()